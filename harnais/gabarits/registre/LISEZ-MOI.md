# Le registre : le suivi sans CRM

Ce dossier remplace le CRM pour celui qui n'en a pas, et pour celui qui vend seul et dont le CRM n'est pas relié à son IA. Il ne sert jamais à côté du CRM d'une équipe. Le harnais le copie à l'installation vers `../registre/`, à côté de l'OS et du harnais, et il le tient à jour avec la personne, après son go, avec les mêmes règles que pour un CRM. Ce dossier est à elle : les mises à jour du harnais n'y touchent jamais.

Deux fichiers suffisent. Ils s'ouvrent dans n'importe quel tableur (Excel, Numbers, Google Sheets, LibreOffice), avec le point-virgule comme séparateur.

| Fichier | Une ligne par | Ce qu'il remplace dans un CRM |
|---|---|---|
| `contacts.csv` | personne suivie, qu'elle n'ait encore rien répondu, qu'elle soit en discussion ou déjà cliente | la fiche de la personne, de son entreprise et de son affaire, l'étape, le SPICED, la prochaine tâche |
| `echanges.csv` | échange (mail, appel, rendez-vous, rencontre) | les notes de l'affaire : le compte rendu et ses preuves |

## Les colonnes de `contacts.csv`

- `id` : un identifiant court, par exemple `mecanova-dupont`, repris dans `echanges.csv`.
- `entreprise`, `site`, `personne`, `fonction`, `email`, `telephone` : qui c'est.
- `type_de_client` : le type de client de l'ICP (`../os/02-icp.md`).
- `etape` : l'étape du parcours client (`../os/03-parcours-client.md`), écrite avec son nom en mots simples. C'est elle qui dit où en est la personne : une étape du pipeline des suspects veut dire qu'elle n'a encore donné aucun signe, une étape du pipeline des prospects veut dire qu'il y a eu un vrai échange.
- `statut_interlocuteur` : actif, en silence ou à atteindre.
- `role_dans_la_decision` : décideur, celui qui paie, utilisateur, celui qui peut bloquer, ou inconnu.
- `origine` : comment le contact est arrivé (recommandation, salon, site, prospection).
- `date_dernier_echange`, `prochaine_action`, `date_prochaine_action` : ce qui s'est passé, et ce qui vient. La prochaine action est un seul geste, le plus proche, par exemple « préparer le rendez-vous du 2026-11-27 », ce qui garde aussi la date du prochain rendez-vous. Les autres engagements de l'échange s'écrivent dans la colonne `engagements` de `echanges.csv`.
- `S`, `P`, `I`, `CE`, `D` : la méthode SPICED, qui dit ce que vous savez vraiment de l'affaire : la situation du client (S), son problème (P), ce que ce problème lui coûte (I), ce qui le pousse à décider avant une date (CE), et qui décide (D). Chaque lettre a un score de 0 (on ne sait rien) à 3 (c'est confirmé) ; la preuve est dans `echanges.csv`.
- `date_evenement_critique`, `montant_estime_ht`, `date_entree_etape` : ce qui donne le rythme de l'affaire.
- `motif_perdu`, `date_reactivation` : remplis quand l'affaire s'arrête, pour savoir quand et comment revenir vers la personne. Une perte ne supprime rien : la ligne reste dans le fichier, à l'étape perdue.
- `linkedin` : l'adresse du profil LinkedIn public de la personne. Elle vit ici, et non dans le dossier personnel du harnais, parce qu'une donnée sur un contact appartient à l'entreprise, et que le dossier personnel part avec le commercial (décision de Laurent du 25/11/2026).

Les dates s'écrivent `AAAA-MM-JJ`.

## Les colonnes de `echanges.csv`

- `date` : la date de l'échange, `AAAA-MM-JJ`.
- `contact_id` : l'identifiant de la personne dans `contacts.csv`.
- `type` : mail, appel, rendez-vous, visio ou rencontre.
- `resume` : le compte rendu, en quelques phrases. Si la transcription complète existe, le résumé dit où elle est rangée.
- `preuve_citation` : les mots exacts du client qui justifient un score ou une étape.
- `scores_proposes` : les scores proposés par le harnais et retenus par vous, par exemple `P:2 CE:3`.
- `engagements` : tout ce qui a été promis, par qui et pour quand, par exemple `moi : plan d'intervention avant le 27/11 ; client : rendez-vous avec le DG le 30/11`.
- `ecrit_le` : la date à laquelle le harnais a écrit la ligne.

## Ce que le registre ne porte pas

Les pages publiques à surveiller de chaque entreprise et les entreprises en veille ne sont pas dans ces deux fichiers. Elles s'écrivent dans `personnel/suivi.md`, dans le dossier du harnais, section « Surveillances en cours », une ligne par entreprise, avec l'`id` de l'un de ses contacts quand il en a un.

## Si vous passez à un CRM

Le registre se reprend tel quel dans un CRM : chaque colonne correspond à un champ du CRM.
