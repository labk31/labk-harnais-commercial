#!/usr/bin/env python3
"""Boucle d'apprentissage du harnais du commercial.

Le script lit les traces de coaching, en tire des motifs, écrit une fiche par motif
dans le wiki, tient un catalogue et un journal, et mesure l'effet de chaque consigne.
Il n'utilise que la bibliothèque standard, pour rester déployable chez un client
sans installation préalable.

Usage :
    python3 src/wiki_loop.py analyse   [--config ../os/crm/config.json]
    python3 src/wiki_loop.py propose   [--config ...]
    python3 src/wiki_loop.py gate  --regle <identifiant>  [--config ...]
    python3 src/wiki_loop.py rapport   [--config ...]
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

# Dans le harnais LABK, la boucle travaille dans la partie personnelle du commercial.
RACINE_HARNAIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.environ.get("HARNAIS_PERSONNEL", os.path.join(RACINE_HARNAIS, "personnel"))
SUITES_POSITIVES = {"faite"}
SUITES_NEGATIVES = {"refusee", "ignoree"}
SUITES_NEUTRES = {"acceptee", "differee", "sans_reponse", "sans_objet"}


# ---------------------------------------------------------------- utilitaires

def chemin(*morceaux):
    return os.path.join(RACINE, *morceaux)


def charge_config(chemin_config):
    # Un chemin relatif se lit depuis la racine du harnais, comme dans les instructions
    # (« ../os/crm/config.json »), et non depuis la partie personnelle.
    if not os.path.isabs(chemin_config):
        chemin_config = os.path.join(RACINE_HARNAIS, chemin_config)
    if not os.path.exists(chemin_config):
        sys.exit("Configuration introuvable : %s" % chemin_config)
    with open(chemin_config, encoding="utf-8") as f:
        return json.load(f)


def lis_traces(dossier):
    """Retourne la liste des événements, ordonnée par horodatage."""
    plein = chemin(dossier)
    evenements = []
    if not os.path.isdir(plein):
        return evenements
    for nom in sorted(os.listdir(plein)):
        if not nom.endswith(".jsonl"):
            continue
        with open(os.path.join(plein, nom), encoding="utf-8") as f:
            for numero, ligne in enumerate(f, start=1):
                ligne = ligne.strip()
                if not ligne:
                    continue
                try:
                    evenement = json.loads(ligne)
                except json.JSONDecodeError:
                    print("Ligne illisible ignorée : %s:%d" % (nom, numero))
                    continue
                evenement["_fichier"] = nom
                evenements.append(evenement)
    evenements.sort(key=lambda e: e.get("horodatage", ""))
    global _DATE_DES_TRACES
    for e in reversed(evenements):
        date = date_de(e)
        if date is not None:
            _DATE_DES_TRACES = date
            break
    return evenements


def date_de(evenement):
    brut = evenement.get("horodatage", "")
    try:
        return datetime.fromisoformat(brut.replace("Z", "+00:00"))
    except ValueError:
        return None


_DATE_DES_TRACES = None


def maintenant():
    """La date du wiki : celle de la trace la plus récente si elle existe, sinon l'horloge."""
    if _DATE_DES_TRACES is not None:
        return _DATE_DES_TRACES
    return datetime.now(timezone.utc).astimezone()


def slug(texte):
    texte = re.sub(r"[^a-zA-Z0-9]+", "-", texte.lower()).strip("-")
    return texte or "motif"


def ecris(chemin_relatif, contenu):
    plein = chemin(chemin_relatif)
    os.makedirs(os.path.dirname(plein), exist_ok=True)
    with open(plein, "w", encoding="utf-8") as f:
        f.write(contenu)
    return plein


def ajoute(chemin_relatif, contenu):
    plein = chemin(chemin_relatif)
    os.makedirs(os.path.dirname(plein), exist_ok=True)
    with open(plein, "a", encoding="utf-8") as f:
        f.write(contenu)
    return plein


# ------------------------------------------------------------------- mesures

def charge_correspondances():
    """Lit personnel/wiki/correspondances.json : anciennes valeurs de regle vers les nouvelles."""
    plein = chemin("wiki", "correspondances.json")
    if not os.path.exists(plein):
        return {}
    try:
        with open(plein, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        print("Correspondances illisibles, ignorées : %s" % plein)
        return {}


def dernieres_consignes(evenements):
    """Garde, pour chaque consigne, sa dernière ligne seulement.

    Une même consigne peut être écrite deux fois : « acceptee » le matin, puis « faite »
    le lendemain. C'est la dernière ligne qui dit la suite réelle. Une consigne se
    reconnaît à son `consigne_id`, ou à défaut à son jour, son dossier et sa règle ; une ligne qui porte `consigne_du`
    (la date de la consigne d'origine) se rattache à ce jour-là.
    """
    correspondances = charge_correspondances()
    dernieres = {}
    ordre = []
    for e in evenements:
        if e.get("type") != "consigne":
            continue
        if e.get("regle") in correspondances:
            e = dict(e, regle=correspondances[e["regle"]])
        if e.get("consigne_id"):
            cle = ("id", e["consigne_id"])
        else:
            jour = e.get("consigne_du") or (e.get("horodatage") or "")[:10]
            cle = (jour, e.get("dossier_id") or e.get("dossier") or "inconnu", e.get("regle") or "sans_regle")
        if cle not in dernieres:
            ordre.append(cle)
        dernieres[cle] = e
    return [dernieres[c] for c in ordre]


def mesure_regles(evenements, jours_avant_cloture=10):
    """Compte, pour chaque règle citée dans les consignes, les suites obtenues.

    Une consigne que les faits ont rendue inutile (`sans_objet`) ne compte ni pour ni contre.
    Une consigne `acceptee` ou `differee` est encore en cours : elle n'entre pas dans le total
    tant que sa dernière ligne a moins de `jours_avant_cloture` jours. Passé ce délai sans
    nouvelle ligne, elle compte comme non faite : une intention qui ne devient jamais un geste
    n'est pas suivie.
    """
    compteur = defaultdict(lambda: {"total": 0, "positives": 0, "negatives": 0, "neutres": 0,
                                    "silences": 0, "sans_objet": 0, "en_cours": 0})
    reference = maintenant()
    for e in dernieres_consignes(evenements):
        regle = e.get("regle") or "sans_regle"
        suite = (e.get("suite") or "sans_reponse").lower()
        bloc = compteur[regle]
        if suite == "sans_objet":
            bloc["sans_objet"] += 1
            continue
        if suite in ("acceptee", "differee"):
            quand = date_de(e)
            if quand is None or (reference - quand).days < jours_avant_cloture:
                bloc["en_cours"] += 1
                continue
        bloc["total"] += 1
        if suite == "sans_reponse":
            bloc["silences"] += 1
        if suite in SUITES_POSITIVES:
            bloc["positives"] += 1
        elif suite in SUITES_NEGATIVES:
            bloc["negatives"] += 1
        else:
            bloc["neutres"] += 1
    return compteur


def mesure_dossiers(evenements):
    """Compte les passages de chaque dossier, règle par règle."""
    compteur = defaultdict(lambda: {"passages": 0, "positives": 0, "nom": "", "regles": set()})
    for e in dernieres_consignes(evenements):
        if (e.get("suite") or "").lower() == "sans_objet":
            continue
        cle = e.get("dossier_id") or e.get("dossier") or "inconnu"
        bloc = compteur[cle]
        bloc["passages"] += 1
        bloc["nom"] = e.get("dossier") or bloc["nom"] or cle
        bloc["regles"].add(e.get("regle") or "sans_regle")
        if (e.get("suite") or "").lower() in SUITES_POSITIVES:
            bloc["positives"] += 1
    return compteur


def detecte_motifs(evenements, config):
    """Retourne la liste des motifs constatés, chacun avec ses preuves."""
    seuils = config.get("seuils", {})
    minimum = seuils.get("occurrences_minimum_pour_motif", 5)
    motifs = []

    for regle, bloc in mesure_regles(evenements).items():
        if bloc["total"] < minimum:
            continue
        taux_refus = bloc["negatives"] / bloc["total"]
        if taux_refus >= 0.5:
            motifs.append({
                "identifiant": "consigne-refusee-%s" % slug(regle),
                "titre": "La consigne %s est refusée plus d'une fois sur deux" % regle,
                "regle": regle,
                "cause": ("Le commercial refuse cette consigne dans la majorité des cas. "
                          "Soit elle arrive au mauvais moment, soit elle demande une information "
                          "qu'il n'a pas encore, soit elle ne correspond pas à sa réalité de terrain."),
                "preuve": "%d consignes envoyées, %d refusées, %d faites."
                          % (bloc["total"], bloc["negatives"], bloc["positives"]),
                "action": "Proposer au commercial de reformuler la consigne dans ses règles personnelles, ou de la retirer pour lui. Passer par la commande gate avant de trancher. Si la consigne vient de la base, le signaler à LABK.",
            })
        elif bloc["silences"] / bloc["total"] >= 0.6:
            motifs.append({
                "identifiant": "consigne-sans-reponse-%s" % slug(regle),
                "titre": "La consigne %s reste sans réponse" % regle,
                "regle": regle,
                "cause": ("La consigne ne produit ni acceptation ni refus. Une consigne qui ne "
                          "déclenche pas de décision occupe de la place sans rien apporter."),
                "preuve": "%d consignes envoyées, %d sans suite explicite."
                          % (bloc["total"], bloc["silences"]),
                "action": "Rendre la consigne décidable : une seule action, une seule question, une échéance.",
            })

    def regle_la_plus_citee(dossiers):
        compte = defaultdict(int)
        for d in dossiers:
            for r in d["regles"]:
                compte[r] += 1
        return max(sorted(compte), key=lambda r: compte[r]) if compte else "sans_regle"

    passages_max = seuils.get("passages_avant_dossier_bloque", 3)
    bloques = []
    for cle, bloc in mesure_dossiers(evenements).items():
        if bloc["passages"] >= passages_max and bloc["positives"] == 0:
            bloques.append(bloc)
    if bloques:
        exemples = ", ".join(sorted(b["nom"] for b in bloques)[:5])
        motifs.append({
            "identifiant": "dossiers-bloques",
            "titre": "Des dossiers reviennent chaque matin sans qu'une action soit engagée",
            "regle": regle_la_plus_citee(bloques),
            "cause": ("Ces dossiers occupent la place des dossiers du jour sans produire de "
                      "mouvement. Tant qu'ils restent dans la liste, les dossiers vivants passent après."),
            "preuve": "%s cité%s au moins %d fois sans une seule suite positive. Exemples : %s."
                      % ("%d dossier%s" % (len(bloques), "s" if len(bloques) > 1 else ""),
                         "s" if len(bloques) > 1 else "", passages_max, exemples),
            "action": ("Au bout de %d passages, proposer au commercial une action datée ou une sortie "
                       "motivée ; c'est lui qui choisit, et s'il garde le dossier tel quel, on l'écrit "
                       "comme sa décision." % passages_max),
        })

    return motifs


def rythme_hebdomadaire(evenements):
    """Compte les consignes faites par semaine, pour lire la pente."""
    par_semaine = defaultdict(int)
    for e in dernieres_consignes(evenements):
        if (e.get("suite") or "").lower() not in SUITES_POSITIVES:
            continue
        d = date_de(e)
        if d is None:
            continue
        annee, semaine, _ = d.isocalendar()
        par_semaine["%d-S%02d" % (annee, semaine)] += 1
    return dict(sorted(par_semaine.items()))


# ------------------------------------------------------------------ ecriture

def ecris_fiche(motif, config):
    corps = []
    corps.append("# %s" % motif["titre"])
    corps.append("")
    corps.append("- Identifiant : `%s`" % motif["identifiant"])
    corps.append("- Règle concernée : `%s`" % motif["regle"])
    corps.append("- Instance : %s" % config.get("instance", "inconnue"))
    corps.append("- Constaté le : %s" % maintenant().strftime("%Y-%m-%d %H:%M"))
    corps.append("")
    corps.append("## Ce que disent les traces")
    corps.append("")
    corps.append(motif["preuve"])
    corps.append("")
    corps.append("## Cause probable")
    corps.append("")
    corps.append(motif["cause"])
    corps.append("")
    corps.append("## Correction proposée")
    corps.append("")
    corps.append(motif["action"])
    corps.append("")
    corps.append("## État")
    corps.append("")
    corps.append("Proposée. Elle n'entre dans `personnel/regles-personnelles.md` qu'après un verdict "
                 "favorable de la commande `gate` et l'accord du commercial, et ce verdict est consigné "
                 "dans `wiki/skill-impact.md`. Elle n'entre jamais dans une skill.")
    corps.append("")
    return ecris(os.path.join("wiki", "patterns", motif["identifiant"] + ".md"), "\n".join(corps))


def ecris_index(config):
    dossier = chemin("wiki", "patterns")
    fiches = sorted(f for f in os.listdir(dossier) if f.endswith(".md")) if os.path.isdir(dossier) else []
    lignes = ["# Catalogue des motifs constatés", "",
              "Ce catalogue est régénéré par `python3 src/wiki_loop.py analyse`. Chaque ligne renvoie "
              "vers une fiche qui porte la preuve chiffrée du motif et la correction proposée.", "",
              "Dernière mise à jour : %s" % maintenant().strftime("%Y-%m-%d %H:%M"), "",
              "| Fiche | Titre | Règle |", "|---|---|---|"]
    for nom in fiches:
        titre, regle = nom[:-3], ""
        with open(os.path.join(dossier, nom), encoding="utf-8") as f:
            for ligne in f:
                if ligne.startswith("# "):
                    titre = ligne[2:].strip()
                if ligne.startswith("- Règle concernée") or ligne.startswith("- Regle concernee"):
                    regle = ligne.split("`")[1] if "`" in ligne else ""
                    break
        lignes.append("| [%s](patterns/%s) | %s | %s |" % (nom[:-3], nom, titre, regle))
    if not fiches:
        lignes.append("| aucune | Aucun motif constaté pour l'instant | |")
    lignes.append("")
    return ecris(os.path.join("wiki", "index.md"), "\n".join(lignes))


def journalise(texte):
    entete = "\n## %s\n\n" % maintenant().strftime("%Y-%m-%d %H:%M")
    return ajoute(os.path.join("wiki", "log.md"), entete + texte + "\n")


def enregistre_impact(regle, verdict, preuve):
    ligne = "| %s | `%s` | %s | %s |\n" % (
        maintenant().strftime("%Y-%m-%d"), regle, verdict, preuve)
    plein = chemin("wiki", "skill-impact.md")
    if not os.path.exists(plein):
        ecris(os.path.join("wiki", "skill-impact.md"),
              "# Historique des consignes\n\n"
              "Chaque tentative reste écrite ici, y compris celles qui ont été rejetées. "
              "Une règle rejetée que l'on oublie revient toujours.\n\n"
              "| Date | Règle | Verdict | Preuve |\n|---|---|---|---|\n")
    return ajoute(os.path.join("wiki", "skill-impact.md"), ligne)


# ------------------------------------------------------------- sous-commandes

def commande_analyse(config):
    evenements = lis_traces(config.get("traces", {}).get("dossier", "raw/traces"))
    if not evenements:
        print("Aucune trace lisible dans %s." % config.get("traces", {}).get("dossier", "raw/traces"))
        print("Le coach doit d'abord tenir quelques sessions avant que la boucle ait de la matière.")
        journalise("Analyse lancée sans aucune trace disponible. Rien n'a été produit.")
        ecris_index(config)
        return
    motifs = detecte_motifs(evenements, config)
    for motif in motifs:
        ecris_fiche(motif, config)
    ecris_index(config)
    rythme = rythme_hebdomadaire(evenements)
    resume = ["%d événements lus, %d motifs constatés." % (len(evenements), len(motifs))]
    if motifs:
        resume.append("")
        for motif in motifs:
            resume.append("- %s (`%s`)" % (motif["titre"], motif["identifiant"]))
    if rythme:
        resume.append("")
        resume.append("Consignes faites par semaine : "
                      + ", ".join("%s : %d" % (k, v) for k, v in rythme.items()) + ".")
    journalise("\n".join(resume))
    print("\n".join(resume))


def commande_propose(config):
    evenements = lis_traces(config.get("traces", {}).get("dossier", "raw/traces"))
    motifs = detecte_motifs(evenements, config)
    if not motifs:
        print("Aucun motif ne justifie une nouvelle consigne. Les règles personnelles restent en l'état.")
        return
    print("Consignes candidates, à soumettre à la commande gate avant toute écriture dans personnel/regles-personnelles.md :")
    for motif in motifs:
        print("\n- Règle : %s" % motif["regle"])
        print("  Motif : %s" % motif["titre"])
        print("  Preuve : %s" % motif["preuve"])
        print("  Rédaction proposée : %s" % motif["action"])
        print("  Commande de test : python3 src/wiki_loop.py gate --regle %s" % motif["regle"])


def commande_gate(config, regle):
    evenements = lis_traces(config.get("traces", {}).get("dossier", "raw/traces"))
    seuils = config.get("seuils", {})
    mesures = mesure_regles(evenements, seuils.get("jours_avant_cloture_consigne", 10))
    minimum = seuils.get("occurrences_minimum_pour_motif", 5)
    bloc = mesures.get(regle)
    if not bloc:
        verdict = "SANS OBJET"
        preuve = "Aucune trace ne cite cette règle."
    elif bloc["total"] < minimum:
        verdict = "EN ATTENTE"
        preuve = ("%d consignes closes seulement, il en faut %d pour trancher (%d encore en cours)."
                  % (bloc["total"], minimum, bloc["en_cours"]))
    else:
        taux = bloc["positives"] / bloc["total"]
        seuil = seuils.get("taux_acceptation_minimum", 0.6)
        verdict = "RETENUE" if taux >= seuil else "REJETEE"
        preuve = ("%d consignes closes, %.0f pour cent faites, seuil à %.0f pour cent (%d encore en cours)."
                  % (bloc["total"], taux * 100, seuil * 100, bloc["en_cours"]))
    enregistre_impact(regle, verdict, preuve)
    journalise("Test de la règle `%s`. Verdict : %s. %s" % (regle, verdict, preuve))
    print("Règle %s. Verdict : %s. %s" % (regle, verdict, preuve))
    print("Ce verdict dit si le commercial suit la règle, pas si elle produit l'effet voulu.")
    if verdict == "RETENUE":
        print("Propose la règle au commercial. S'il est d'accord, écris-la dans personnel/regles-personnelles.md, datée, avec cette preuve.")
    elif verdict == "REJETEE":
        print("Ne change pas la règle. Demande une fois au commercial ce qui l'en empêche, propose une règle personnelle s'il en veut une, et note-le pour le rapport pour LABK.")


def commande_rapport(config):
    evenements = lis_traces(config.get("traces", {}).get("dossier", "raw/traces"))
    mesures = mesure_regles(evenements)
    print("Instance : %s" % config.get("instance", "inconnue"))
    print("Événements lus : %d" % len(evenements))
    if not mesures:
        print("Aucune consigne tracée pour l'instant.")
        return
    print("")
    print("%-34s %7s %9s %8s %10s" % ("Règle", "Total", "Faites", "Refusées", "Sans suite"))
    for regle, bloc in sorted(mesures.items(), key=lambda kv: -kv[1]["total"]):
        print("%-34s %7d %9d %8d %10d"
              % (regle[:34], bloc["total"], bloc["positives"], bloc["negatives"], bloc["neutres"]))
    rythme = rythme_hebdomadaire(evenements)
    if rythme:
        print("")
        print("Consignes faites par semaine :")
        for semaine, nombre in rythme.items():
            print("  %s : %d" % (semaine, nombre))


def main():
    parseur = argparse.ArgumentParser(description="Boucle d'apprentissage du Coach CRM.")
    parseur.add_argument("commande", choices=["analyse", "propose", "gate", "rapport"])
    parseur.add_argument("--config", default=os.path.join(RACINE_HARNAIS, "..", "os", "crm", "config.json"))
    parseur.add_argument("--regle", default=None)
    arguments = parseur.parse_args()
    config = charge_config(arguments.config)
    if arguments.commande == "analyse":
        commande_analyse(config)
    elif arguments.commande == "propose":
        commande_propose(config)
    elif arguments.commande == "gate":
        if not arguments.regle:
            sys.exit("La commande gate demande --regle <identifiant>.")
        commande_gate(config, arguments.regle)
    else:
        commande_rapport(config)


if __name__ == "__main__":
    main()
