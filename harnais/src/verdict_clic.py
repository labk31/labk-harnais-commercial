# -*- coding: utf-8 -*-
"""Verdict d'un clic de campagne : machine, a confirmer, humain probable, humain tres probable.

Script de la base du harnais LABK. La regle est decrite dans methode/lire-un-signal.md ; elle reprend
la regle du verdict des clics validee par Laurent Bouloc le 16/11/2026 pour la prospection de LABK.

Entrees : un signal tel que l'objet des signaux du CRM le porte (lien, dateSignal, ip, ipProprietaire,
ipVille, ipRegion, signatureNavigateur, identifiantRegistre), l'heure de l'envoi auquel il repond, la ville
et le departement de l'entreprise, et les autres signaux de la meme vague (pour la rafale et l'adresse
partagee).

Reglages : les valeurs ci-dessous sont celles de depart. charger_reglages(chemin) les remplace par le bloc
prospection.verdict_clic de ../os/crm/config.json ; une liste laissee a null garde la liste par defaut.
Les listes par defaut sont francaises : un client d'un autre pays remplit ses listes dans la configuration.
"""
import datetime as dt
import unicodedata

DELAI_MACHINE_S = 120          # moins de 2 minutes apres l'envoi : machine
FENETRE_RAFALE_S = 1           # plusieurs liens dans la meme seconde : machine
FENETRE_IP_PARTAGEE_S = 3600   # meme adresse chez une autre entreprise dans l'heure : machine
FENETRE_PIEGE_S = 60           # clics de la meme adresse dans la minute d'un clic piege : machine

# Proprietaires d'adresses qui signent une machine : hebergeurs, nuages, filtres de messagerie.
HEBERGEURS = ["ovh", "amazon", "aws", "microsoft", "azure", "google", "hetzner", "digitalocean",
              "linode", "akamai", "cloudflare", "fastly", "oracle", "ionos", "scaleway", "online s.a.s",
              "proofpoint", "mimecast", "barracuda", "cisco", "zscaler", "forcepoint", "trend micro",
              "sophos", "fortinet", "vade", "mailinblack", "hostinger", "leaseweb", "contabo", "datacamp",
              "m247", "choopa", "vultr", "alibaba", "tencent", "yandex", "facebook", "meta platforms"]
# Operateurs d'acces (fixe, mobile, entreprise) : humain possible.
OPERATEURS = ["orange", "sfr", "free", "proxad", "bouygues", "completel", "numericable", "coriolis",
              "nordnet", "kosc", "adista", "jaguar network", "colt", "lumen", "telefonica", "vodafone",
              "swisscom", "proximus", "telenet", "bretagne telecom", "sewan", "celeste", "nerim", "k-net",
              "alsatis", "ozone", "videofutur", "zayo", "iliad"]

DEP_REGION = {
    "ain": "auvergne-rhone-alpes",
    "allier": "auvergne-rhone-alpes",
    "ardeche": "auvergne-rhone-alpes",
    "cantal": "auvergne-rhone-alpes",
    "drome": "auvergne-rhone-alpes",
    "isere": "auvergne-rhone-alpes",
    "loire": "auvergne-rhone-alpes",
    "haute-loire": "auvergne-rhone-alpes",
    "puy-de-dome": "auvergne-rhone-alpes",
    "rhone": "auvergne-rhone-alpes",
    "savoie": "auvergne-rhone-alpes",
    "haute-savoie": "auvergne-rhone-alpes",
    "cote-d'or": "bourgogne-franche-comte",
    "doubs": "bourgogne-franche-comte",
    "jura": "bourgogne-franche-comte",
    "nievre": "bourgogne-franche-comte",
    "haute-saone": "bourgogne-franche-comte",
    "saone-et-loire": "bourgogne-franche-comte",
    "yonne": "bourgogne-franche-comte",
    "territoire-de-belfort": "bourgogne-franche-comte",
    "cotes-d'armor": "bretagne",
    "finistere": "bretagne",
    "ille-et-vilaine": "bretagne",
    "morbihan": "bretagne",
    "cher": "centre-val-de-loire",
    "eure-et-loir": "centre-val-de-loire",
    "indre": "centre-val-de-loire",
    "indre-et-loire": "centre-val-de-loire",
    "loir-et-cher": "centre-val-de-loire",
    "loiret": "centre-val-de-loire",
    "corse-du-sud": "corse",
    "haute-corse": "corse",
    "ardennes": "grand-est",
    "aube": "grand-est",
    "marne": "grand-est",
    "haute-marne": "grand-est",
    "meurthe-et-moselle": "grand-est",
    "meuse": "grand-est",
    "moselle": "grand-est",
    "bas-rhin": "grand-est",
    "haut-rhin": "grand-est",
    "vosges": "grand-est",
    "aisne": "hauts-de-france",
    "nord": "hauts-de-france",
    "oise": "hauts-de-france",
    "pas-de-calais": "hauts-de-france",
    "somme": "hauts-de-france",
    "paris": "ile-de-france",
    "seine-et-marne": "ile-de-france",
    "yvelines": "ile-de-france",
    "essonne": "ile-de-france",
    "hauts-de-seine": "ile-de-france",
    "seine-saint-denis": "ile-de-france",
    "val-de-marne": "ile-de-france",
    "val-d'oise": "ile-de-france",
    "calvados": "normandie",
    "eure": "normandie",
    "manche": "normandie",
    "orne": "normandie",
    "seine-maritime": "normandie",
    "charente": "nouvelle-aquitaine",
    "charente-maritime": "nouvelle-aquitaine",
    "correze": "nouvelle-aquitaine",
    "creuse": "nouvelle-aquitaine",
    "dordogne": "nouvelle-aquitaine",
    "gironde": "nouvelle-aquitaine",
    "landes": "nouvelle-aquitaine",
    "lot-et-garonne": "nouvelle-aquitaine",
    "pyrenees-atlantiques": "nouvelle-aquitaine",
    "deux-sevres": "nouvelle-aquitaine",
    "vienne": "nouvelle-aquitaine",
    "haute-vienne": "nouvelle-aquitaine",
    "ariege": "occitanie",
    "aude": "occitanie",
    "aveyron": "occitanie",
    "gard": "occitanie",
    "haute-garonne": "occitanie",
    "gers": "occitanie",
    "herault": "occitanie",
    "lot": "occitanie",
    "lozere": "occitanie",
    "hautes-pyrenees": "occitanie",
    "pyrenees-orientales": "occitanie",
    "tarn": "occitanie",
    "tarn-et-garonne": "occitanie",
    "loire-atlantique": "pays-de-la-loire",
    "maine-et-loire": "pays-de-la-loire",
    "mayenne": "pays-de-la-loire",
    "sarthe": "pays-de-la-loire",
    "vendee": "pays-de-la-loire",
    "alpes-de-haute-provence": "provence-alpes-cote-d'azur",
    "hautes-alpes": "provence-alpes-cote-d'azur",
    "alpes-maritimes": "provence-alpes-cote-d'azur",
    "bouches-du-rhone": "provence-alpes-cote-d'azur",
    "var": "provence-alpes-cote-d'azur",
    "vaucluse": "provence-alpes-cote-d'azur",
}

def _norm(s):
    s = unicodedata.normalize("NFKD", (s or "").strip().lower())
    return "".join(c for c in s if not unicodedata.combining(c)).replace(" ", "-")

def _date(s):
    if not s: return None
    try: return dt.datetime.fromisoformat(str(s).strip().replace("Z", "+00:00"))
    except Exception: return None

def type_proprietaire(org):
    o = (org or "").lower()
    if not o: return "INCONNU"
    if any(k in o for k in HEBERGEURS): return "HEBERGEUR"
    if any(k in o for k in OPERATEURS): return "OPERATEUR"
    return "INCONNU"

SUFFIXE_PIEGE = "-piege"

def charger_reglages(chemin_config):
    """Lit le bloc prospection.verdict_clic de la configuration du CRM et remplace les valeurs de depart."""
    import json
    global DELAI_MACHINE_S, FENETRE_RAFALE_S, FENETRE_IP_PARTAGEE_S, FENETRE_PIEGE_S, SUFFIXE_PIEGE
    global HEBERGEURS, OPERATEURS, DEP_REGION
    with open(chemin_config, encoding="utf-8") as f:
        r = (json.load(f).get("prospection") or {}).get("verdict_clic") or {}
    DELAI_MACHINE_S = r.get("delai_machine_secondes", DELAI_MACHINE_S)
    FENETRE_RAFALE_S = r.get("fenetre_rafale_secondes", FENETRE_RAFALE_S)
    FENETRE_IP_PARTAGEE_S = r.get("fenetre_adresse_partagee_secondes", FENETRE_IP_PARTAGEE_S)
    FENETRE_PIEGE_S = r.get("fenetre_piege_secondes", FENETRE_PIEGE_S)
    SUFFIXE_PIEGE = r.get("suffixe_lien_piege") or SUFFIXE_PIEGE
    if r.get("hebergeurs"): HEBERGEURS = [x.lower() for x in r["hebergeurs"]]
    if r.get("fournisseurs_acces"): OPERATEURS = [x.lower() for x in r["fournisseurs_acces"]]
    if r.get("departements_regions"): DEP_REGION = {_norm(k): _norm(v) for k, v in r["departements_regions"].items()}

def est_piege(lien):
    return (lien or "").lower().endswith(SUFFIXE_PIEGE)

def verdict_clic(ev, envoi_iso, ent_ville="", ent_departement="", autres=(), entreprise_de=lambda cid: ""):
    """Rend (verdict, motif). ev : dict avec lien, dateSignal, ip, ipProprietaire, ipVille, ipRegion,
    signatureNavigateur, identifiantRegistre."""
    lien = ev.get("lien", "")
    t = _date(ev.get("dateSignal"))
    ip = ev.get("ip", "") or ""
    if est_piege(lien):
        return "MACHINE", "clic sur le lien piege, invisible pour un humain"
    for o in autres:
        if o is ev or (o.get("ip") or "") != ip or not est_piege(o.get("lien")): continue
        to = _date(o.get("dateSignal"))
        if t and to and abs((to - t).total_seconds()) <= FENETRE_PIEGE_S:
            return "MACHINE", "meme adresse que le clic du lien piege, dans la minute"
    proprio = type_proprietaire(ev.get("ipProprietaire"))
    if proprio == "HEBERGEUR":
        return "MACHINE", "adresse d'hebergeur ou de nuage (%s)" % ev.get("ipProprietaire")
    ua = (ev.get("signatureNavigateur") or "").strip()
    if ua in ("", "Mozilla/5.0"):
        return "MACHINE", "signature de navigateur vide ou nue"
    te = _date(envoi_iso)
    if t and te and 0 <= (t - te).total_seconds() < DELAI_MACHINE_S:
        return "MACHINE", "moins de %d secondes apres l'envoi" % DELAI_MACHINE_S
    for o in autres:
        if o is ev or o.get("identifiantRegistre") != ev.get("identifiantRegistre"): continue
        if (o.get("lien") or "") == lien: continue
        to = _date(o.get("dateSignal"))
        if t and to and abs((to - t).total_seconds()) <= FENETRE_RAFALE_S:
            return "MACHINE", "plusieurs liens cliques dans la meme seconde"
    mon_ent = (entreprise_de(ev.get("identifiantRegistre")) or "").lower()
    for o in autres:
        if o is ev or (o.get("ip") or "") != ip or not ip: continue
        ent = (entreprise_de(o.get("identifiantRegistre")) or "").lower()
        if not ent or ent == mon_ent: continue
        to = _date(o.get("dateSignal"))
        if t and to and abs((to - t).total_seconds()) <= FENETRE_IP_PARTAGEE_S:
            return "MACHINE", "meme adresse chez une autre entreprise dans l'heure (scanner)"
    if proprio == "INCONNU":
        return "A_CONFIRMER", "proprietaire de l'adresse inconnu ou non classe (%s)" % (ev.get("ipProprietaire") or "vide")
    ville_ip, region_ip = _norm(ev.get("ipVille")), _norm(ev.get("ipRegion"))
    if ville_ip and ville_ip == _norm(ent_ville):
        return "HUMAIN_TRES_PROBABLE", "operateur, clic localise dans la ville de l'entreprise (%s)" % ev.get("ipVille")
    reg_ent = DEP_REGION.get(_norm(ent_departement), "")
    if region_ip and reg_ent and region_ip == reg_ent:
        return "HUMAIN_TRES_PROBABLE", "operateur, clic localise dans la region de l'entreprise (%s, entreprise a %s)" % (ev.get("ipVille"), ent_ville)
    return "HUMAIN_PROBABLE", "operateur, clic localise ailleurs (%s, entreprise a %s)" % (ev.get("ipVille") or "ville inconnue", ent_ville or "?")

if __name__ == "__main__":
    E = "2026-11-18T08:35:00+01:00"
    cas = [
        ({"lien": "ps-piege", "dateSignal": "2026-11-18T08:36:00+01:00", "ip": "1.2.3.4", "signatureNavigateur": "x"}, "MACHINE"),
        ({"lien": "ps-m1", "dateSignal": "2026-11-18T09:40:00+01:00", "ip": "51.89.1.1", "ipProprietaire": "AS16276 OVH SAS", "signatureNavigateur": "Mozilla/5.0 (Windows)"}, "MACHINE"),
        ({"lien": "ps-m1", "dateSignal": "2026-11-18T08:35:40+01:00", "ip": "90.1.1.1", "ipProprietaire": "AS3215 Orange S.A.", "signatureNavigateur": "Mozilla/5.0 (iPhone)"}, "MACHINE"),
        ({"lien": "ps-m1", "dateSignal": "2026-11-18T08:50:00+01:00", "ip": "90.1.1.1", "ipProprietaire": "AS3215 Orange S.A.", "ipVille": "Montauban", "ipRegion": "Occitanie", "signatureNavigateur": "Mozilla/5.0 (iPhone)"}, "HUMAIN_TRES_PROBABLE"),
        ({"lien": "ps-m1", "dateSignal": "2026-11-18T10:00:00+01:00", "ip": "90.1.1.2", "ipProprietaire": "AS15557 SFR SA", "ipVille": "Paris", "ipRegion": "Île-de-France", "signatureNavigateur": "Mozilla/5.0 (Mac)"}, "HUMAIN_PROBABLE"),
        ({"lien": "ps-m1", "dateSignal": "2026-11-18T10:00:00+01:00", "ip": "9.9.9.9", "ipProprietaire": "AS9999 Inconnu Ltd", "signatureNavigateur": "Mozilla/5.0 (Mac)"}, "A_CONFIRMER"),
    ]
    ok = 0
    for ev, attendu in cas:
        v, m = verdict_clic(ev, E, "Montauban", "Tarn-et-Garonne")
        ok += v == attendu
        print(("OK " if v == attendu else "KO ") + v + " | " + m)
    print("%d/%d" % (ok, len(cas)))
