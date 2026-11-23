# Le profil du commercial

Ce fichier appartient au commercial. Le harnais le remplit avec lui pendant l'installation, puis le lit au début de chaque session. Les mises à jour du harnais n'y touchent jamais.

## Qui il est

- Nom : <nom>
- Rôle : <rôle>
- Types de clients et segments qu'il suit : <types de clients>
- Vend seul, ou avec d'autres commerciaux : <seul, ou en équipe>
- Tutoiement demandé : <oui ou non>
- Son nom de propriétaire dans le CRM, utile seulement dans une équipe : <nom, tel que le CRM l'écrit, ou « sans objet »>
- Les retours d'expérience, c'est-à-dire les cas clients racontés : <dossier ou lien, ou « aucun »>

## Ses outils

| Outil | Nom | Le harnais peut le lire | Le harnais peut y écrire, après son go |
|---|---|---|---|
| CRM | <nom, ou « aucun, registre ../registre/ »> | <oui ou non> | <oui ou non> |
| Messagerie | <nom> | <oui ou non> | non, le harnais prépare et le commercial envoie |
| Agenda | <nom> | <oui ou non> | <oui ou non> |
| Visio et transcription | <nom> | <oui ou non> | non |
| IA utilisée | <nom et modèle> | sans objet | sans objet |

Ces choix restent dans les limites de `../os/08-autorisations.md`, s'il existe ; sinon, le commercial décide seul. C'est toujours le cas chez celui qui vend seul. Ce qu'il a refusé est noté ici, et le harnais fait sans.

## Comment il apporte ses échanges

<il colle la transcription, il joint un fichier, ou il a un dossier où elles arrivent (lequel)>

## Son point du matin

- Heure : <heure>
- L'ordre de tri : celui de l'entreprise (`../os/07-ordre-du-point-du-matin.md`, quand il existe), sinon l'ordre LABK. Un ordre propre au commercial est une règle personnelle, écrite dans `regles-personnelles.md`, jamais ici.

## Python

La commande qui lance Python sur son ordinateur, relevée à l'installation : <python3, python ou py>

## Le modèle d'IA

<ce que son outil permet : choisir un petit modèle pour les tâches simples et un grand pour rédiger, négocier et coacher, ou une recommandation faite une fois>

## La version du harnais installée

<numéro de version, lu dans JOURNAL.md, et date d'installation>

Cette ligne garde la version de l'installation. Après une mise à jour, la version en cours se lit en tête de `JOURNAL.md`, et la mise à jour l'écrit dans `journal.md`.
