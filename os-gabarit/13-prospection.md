# La prospection de l'entreprise

Ce fichier porte les réglages de la prospection de l'entreprise : par quels canaux elle va chercher des suspects, qui fait partir les messages, à quel rythme, et sous quelles limites. Le comment vit dans le harnais (la méthode `prospection.md`, `sources-et-listes.md` et `lire-un-signal.md`, et les skills `liste` et `campagne`) ; le quoi et le combien vivent ici.

Règle révisable, décidée par la personne autorisée. Chez celui qui vend seul, c'est vous, avec le harnais, à l'installation. Les valeurs écrites entre parenthèses sont les valeurs de départ : elles ont servi chez LABK, et vous les changez dès que votre terrain dit autre chose.

Ce fichier n'est pas requis pour faire tourner le harnais. Il l'est pour lancer une campagne : tant qu'il manque ou porte encore des mentions entre chevrons, le harnais suit les suspects et les prospects qui existent déjà, mais il ne prépare aucune vague.

## Les canaux et leurs relais

Le relais est l'outil ou la personne qui fait partir un message. Un canal sans relais reste en manuel : le harnais prépare tout, et le commercial fait partir lui-même.

| Canal | Utilisé | Relais | Ce qu'il faut savoir |
|---|---|---|---|
| Mail | <oui ou non> | <la messagerie du commercial par son connecteur, le nom de l'outil d'envoi, ou « manuel »> | Un outil d'envoi mesure souvent les ouvertures par défaut. Le harnais ne s'en sert pas : vous pouvez couper ce réglage |
| LinkedIn | <oui ou non> | Manuel, toujours | Les conditions de LinkedIn interdisent qu'un outil agisse à la place d'une personne |
| Téléphone | <oui ou non> | Manuel | Vers des particuliers, le consentement préalable est obligatoire |
| Événements | <oui ou non> | Manuel | <les sources d'événements suivies, par exemple les clubs d'affaires et la chambre de commerce> |
| Réseau et prescripteurs | <oui ou non> | Manuel | <les prescripteurs connus, ou « à construire »> |

**L'envoi planifié.** Pour que les vagues de mails partent chaque matin sans que le commercial ouvre son IA, il faut une tâche planifiée qui lit la vague validée du jour et la fait partir.

- Tâche planifiée : <oui, avec son nom et son heure ; ou non : le commercial écrit « envoie la vague du jour » chaque matin ouvré>

## Les adresses d'envoi

| Adresse | Compte de messagerie | Mise en service | Plafond par jour |
|---|---|---|---|
| <adresse@entreprise.fr> | <nom du compte dans le connecteur> | <date> | <nombre> (50) |

Chaque campagne écrit dans sa fiche l'adresse qui l'envoie. Le plafond compte tous les messages de la journée sur cette adresse, nouveaux et relances, toutes campagnes confondues.

## Les créneaux et les absences

- Jours d'envoi : <jours ouvrés> (du lundi au vendredi, hors jours fériés français)
- Créneaux : <heures> (de 8 h 30 à 12 h et de 14 h à 17 h 30, heure de Paris)
- Absences du commercial : <emplacement du fichier ou de l'agenda qui les porte, ou « aucun »>. Pendant une absence, rien ne part, et les relances dues glissent au retour.

## Le rythme

- Délai entre deux envois sur la même adresse : <secondes> (tiré au hasard entre 120 et 240 secondes, jamais fixe)
- Montée en charge d'une adresse neuve (jamais servie à la prospection), ou à l'arrêt depuis deux semaines ou plus : <règle> (10 messages par jour au départ, puis un de plus par palier de deux jours ouvrés, tant qu'aucun rebond dur nouveau n'apparaît sur la vague précédente)
- Quota de croisière : <nombre par jour> (fixé par le commercial ; le calcul à rebours le propose)
- Cadence par défaut d'une séquence : <nombre de pas et délai> (quatre pas, six jours ouvrés entre deux pas). Chaque campagne peut fixer la sienne dans sa fiche.

## Le go

- Forme du go : <par lot ou par semaine> (par semaine : le harnais prépare les cinq vagues de la semaine suivante, les montre en entier, et un seul go les couvre)
- Jour et heure de la préparation de la semaine : <jour et heure> (le vendredi à 14 h)

Un message que le commercial n'a pas lu en entier n'est jamais couvert par un go, même hebdomadaire : un message personnel écrit après un vrai clic, ou le premier texte d'un sujet nouveau.

## Les sources de listes

| Source | Verdict | Coût | Qui lance la recherche |
|---|---|---|---|
| <nom du fournisseur de données sous licence, ou « aucun »> | Vert | <coût par contact exporté et par adresse trouvée> | Le commercial, sur le coût annoncé par le harnais |
| Fichiers fournis par le commercial | À vérifier, fichier par fichier | Aucun | Le commercial |
| Pages publiques désignées par le commercial | À vérifier, site par site | Aucun | Le commercial |
| Sites d'offres d'emploi | Rouge | | Personne |

- Seuil du score d'adéquation : <nombre sur 10> (6)
- Personne contactée par défaut dans une entreprise : <rôle> (le dirigeant ou le fondateur)
- Seuil d'alerte du stock : <règle> (dix jours ouvrés d'envois au rythme du moment)

## Le suivi des clics

Le suivi des clics est facultatif. Sans lui, le harnais travaille sur les réponses seules.

- Outil de suivi des liens : <nom et adresse, ou « aucun »>
- Code du lien piège : <code, par exemple un suffixe « -piege »>
- Les listes du verdict (fournisseurs d'accès, hébergeurs, départements et régions) : dans `crm/config.json`, bloc `prospection.verdict_clic`. Sans réglage, le script du harnais prend ses listes françaises par défaut.

## Les valeurs de départ du calcul à rebours

Le harnais s'en sert tant qu'aucun bilan de campagne n'existe, et les marque comme des hypothèses. Le premier bilan les remplace.

- Réponses qualifiées pour cent suspects touchés : <nombre, ou « à estimer avec le commercial »>
- Rendez-vous pour dix réponses qualifiées : <nombre, ou « à estimer avec le commercial »>

## La phrase pour ne plus être contacté

Chaque mail de prospection la porte, à la fin.

- Texte : <phrase> (« Si ce sujet ne vous concerne pas, dites-le-moi simplement et je ne vous écrirai plus. »)

## Où vivent les campagnes

Les fiches des campagnes et les vagues de chaque jour vivent dans le dossier `prospection/` de l'entreprise, à côté des dossiers `os/` et `harnais/` : une fiche par campagne dans `prospection/campagnes/`, et une vague par jour dans `prospection/vagues/`. Les suspects eux-mêmes vivent dans le CRM, ou à défaut dans le registre.
