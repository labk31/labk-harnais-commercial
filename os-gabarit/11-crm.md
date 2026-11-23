# Le CRM de l'entreprise

Ce fichier dit comment l'entreprise se sert de son CRM : quel outil, quels objets comptent, quelles fiches doivent porter quels champs, et les règles d'usage. Le CRM appartient à l'entreprise : n'importe quel commercial qui arrive avec un nouveau harnais doit pouvoir reprendre sa donnée.

Le contenu de ce fichier est révisable. Dans une entreprise accompagnée par LABK, la structure du CRM est produite par l'architecte CRM de LABK à partir de cet OS, puis paramétrée dans l'outil. Chez celui qui vend seul, il n'y a pas d'architecte CRM : vous remplissez ce fichier et `crm/config.json` avec le harnais, à l'installation. Ce fichier se remplit avec les demandes 23 et 24 de la liste minimale (`collecte/liste-minimale.md`). Le harnais lit la structure du CRM et ne la modifie jamais : il ne crée ni objet, ni champ, ni étape dans votre outil.

Celui qui n'a pas de CRM n'a presque rien à remplir ici : il lit la section « Sans CRM : le registre », qui tient lieu de CRM.

Règle immuable (décision du 23/11/2026) : aucun workflow ne tourne dans le CRM. L'architecte CRM intervient une fois cet OS défini : il se connecte au CRM, y pose les objets, les propriétés, les étapes et les listes de valeurs, puis remplit ce fichier et `crm/config.json` avec les vrais noms du CRM. Ce que des automatisations auraient fait (dater un changement d'étape, passer un suspect gagné en affaire, sortir un suspect dont le délai est passé), c'est le harnais du commercial qui le propose et l'écrit sur son go, dans le CRM comme dans le registre. Ainsi, le même harnais marche sur n'importe quel CRM. Si votre CRM fait déjà tourner des automatisations, l'installation les liste et vous signale celles qui doublent le harnais.

## L'outil

- CRM : <nom de l'outil, ou « aucun, registre `../registre/` »>
- Adresse : <adresse>
- Connecteur utilisé par le harnais : le nom indiqué dans `crm/config.json`, sous `crm.serveur_mcp`. Sans CRM, cette clé prend la valeur `null`.

## La configuration technique

Les noms exacts des objets, des étapes, des champs de qualification, des seuils et des délais vivent dans `crm/config.json`. Le harnais n'écrit jamais un nom d'étape ou de champ en dur : il le prend dans ce fichier. C'est ce qui permet de reprendre le même harnais chez un autre client.

Dans la configuration, on écrit toujours le nom technique d'un champ ou d'une étape, celui que le connecteur du CRM renvoie, et jamais son libellé affiché à l'écran. Le libellé change quand quelqu'un le renomme ; le nom technique, non. Chez certains CRM, ce nom technique est une suite de chiffres et de lettres : c'est celle-là qu'on recopie.

## Sans CRM : le registre

Celui qui n'a pas de CRM suit ses contacts dans le registre, deux fichiers de tableur que le harnais tient pour lui. Ils sont fournis vides avec le harnais (`../harnais/gabarits/registre/`) et copiés à l'installation dans un dossier `registre/`, à côté des dossiers `os/` et `harnais/`, jamais dans l'OS : l'OS dit comment vous vendez, le registre dit où en est chaque contact. `contacts.csv` porte une ligne par personne suivie : l'entreprise, la personne, l'étape en mots simples, le statut, le dernier échange, la prochaine action et sa date, le SPICED en cinq colonnes, le motif de perte et la date de réactivation. `echanges.csv` porte une ligne par échange, avec son compte rendu, les mots du client qui font preuve et les engagements pris. Les colonnes sont définies dans le `LISEZ-MOI.md` du registre, et nulle part ailleurs.

Le registre tient la place du CRM : partout où le harnais parle d'une fiche, d'une note ou d'une tâche, il parle du registre, avec les mêmes règles, et il n'y écrit rien sans votre go. Vous pouvez l'ouvrir et le corriger vous-même à tout moment.

Chez celui qui vend seul, le harnais le copie à l'installation et écrit lui-même dans ce fichier et dans `crm/config.json` les deux lignes qui disent qu'il n'y a pas de CRM. Dans une équipe sans CRM, le registre sert aussi, mais le harnais n'écrit pas dans l'OS : il prépare ces lignes dans un constat, la personne autorisée les écrit, et le harnais copie ensuite le registre sur le go du commercial. Il ne sert jamais à côté du CRM d'une équipe.

Avec le registre, le harnais ne lit pas les noms d'étapes ni de champs de `crm/config.json` : il lit les colonnes du registre et les étapes en mots simples de `03-parcours-client.md`. Ce qui suppose un CRM ne s'applique pas, et rien ne bloque : il n'y a ni objet des interlocuteurs (le statut et le rôle se lisent sur la ligne de la personne), ni objet Routine (aucune routine n'est lue), ni champ propriétaire (tout le registre est à vous), ni automatisation. Si vous passez un jour à un CRM, le registre s'y reprend tel quel : chaque colonne correspond à un champ du CRM.

## Le socle CRM

Le socle CRM est la structure minimale que LABK pose chez tous ses clients accompagnés, puis adapte à leur OS : les fiches des entreprises, des contacts, des suspects et des affaires ; les interlocuteurs de chaque affaire, avec leur statut et leur rôle dans la décision ; les tâches, les notes et les routines ; les deux pipelines (suspects et affaires) ; et la grille SPICED décrite plus bas. L'architecte CRM le décrit dans un classeur, le fait valider par la personne autorisée, puis le pose dans le CRM ou le compare au CRM existant. Ce classeur fait partie du service de l'architecte CRM et n'est pas dans ce dépôt. Celui qui vend seul n'en a pas besoin : son registre ou un CRM simple suffit.

## Selon l'outil

Le harnais marche sur tout CRM qu'un connecteur relie à l'IA. Trois cas reviennent. L'architecte CRM les règle à la pose. Celui qui vend seul n'a pas de socle à poser : à l'installation, le harnais relève ce que son CRM a déjà, l'écrit dans `crm/config.json` et laisse à `null` ce qui manque (skill `installation`, section 3 bis) ; s'il veut un pipeline ou un champ de plus, il le crée lui-même dans son outil, et le harnais en relève ensuite le nom.

- **Le CRM permet de créer des objets** (Twenty, Salesforce, certaines offres de HubSpot) : on pose le socle tel qu'il est, avec l'objet des interlocuteurs de l'affaire et l'objet des routines.
- **Le CRM ne permet que des champs** (Pipedrive, par exemple) : le statut d'un interlocuteur (actif, en silence, à atteindre) et son rôle dans la décision deviennent deux champs de la personne, et le silence se lit sur la personne ; les routines vivent dans `12-routines.md` quand ce fichier existe (édition équipe), et sinon aucune routine n'est lue. Les suspects ne vivent pas dans la boîte des leads de Pipedrive, qui n'a pas d'étapes : on crée un pipeline « Suspects » à part, avec ses étapes. Dans la configuration, `crm.objet_suspect` et `crm.objet_opportunite` désignent alors tous deux les affaires, et `crm.pipeline_suspect` et `crm.pipeline_opportunite` disent quel pipeline est lequel. La clé technique des champs personnalisés de Pipedrive est une longue suite de caractères : c'est elle qu'on écrit dans la configuration.
- **Le CRM n'a pas de connecteur** : le harnais ne peut ni le lire ni y écrire. Celui qui vend seul garde le registre, ou change d'outil ; une équipe change d'outil ou ajoute le connecteur.

## Les montants

Règle révisable. Tous les montants du CRM, des notes et des devis s'écrivent hors taxe, sauf mention contraire écrite ici : <hors taxe, ou autre convention>. Quand un client donne un budget sans dire s'il est hors taxe ou toutes taxes comprises, le harnais pose la question au commercial avant d'écrire le montant.

## La grille SPICED à installer dans le CRM

Règle immuable : c'est la grille de la méthode LABK. L'architecte CRM crée sur l'affaire un champ par lettre, en liste à quatre valeurs, avec exactement ces libellés et ces définitions. La définition complète s'écrit dans la description du champ, pour que le commercial la lise dans son CRM. Une lettre est acquise à 2, avec une preuve dans une note. La grille ne dit pas une vérité sur l'affaire : elle dit où est le risque de parler à la mauvaise personne, au mauvais moment, pour de mauvaises raisons.

La grille complète, avec la définition de chaque niveau et les cas qui reviennent, est dans la base du harnais : `../harnais/methode/grille-spiced.md`. L'architecte CRM y recopie, dans la description de chaque champ, la définition de chaque niveau, mot pour mot. Les libellés courts à installer sont :

| Lettre | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| S | Inconnue | Partielle | Comprise | Confirmée |
| P | Inconnue | Supposée | Dite | Partagée |
| I | Inconnu | Ressenti | Chiffré | Repris |
| CE | Inconnu | Sans date | Daté | Imminent |
| D | Inconnue | Décideur nommé | Circuit connu | Confirmée |

Le CE à 2 demande deux champs de plus sur l'affaire, que l'architecte CRM crée aussi : le déclencheur (ce qui fera bouger le client, en texte) et la date du déclencheur. L'impact a deux faces, qui ne prennent pas de champ : l'impact rationnel (ce que le problème coûte ou rapporte à l'entreprise) et l'impact émotionnel (ce qu'il fait vivre à la personne). Chacune s'écrit en une phrase ou une explication dans le compte rendu de l'échange ; le score du I se fonde sur le rationnel. Le hors cible ne se note pas dans le S : il se note dans le type ICP de l'entreprise.

Si l'outil du client ne permet pas de créer ces champs, le score de chaque lettre s'écrit dans la note de qualification de l'affaire, une ligne par lettre, sous la forme « CE : 2, <phrase du client>, <date de l'échange> ». Le harnais relit ces lignes à la place des champs.

## Les champs obligatoires par fiche

| Fiche | Champs obligatoires |
|---|---|
| Entreprise | <champs> |
| Personne | <champs> |
| Affaire | <champs> |

Quand un champ obligatoire manque, le harnais ne crée pas la fiche : il dit ce qui manque. Sans CRM, le harnais écrit ici, à l'installation, que chaque ligne de `contacts.csv` porte au moins `entreprise`, `personne` et `etape`, l'étape disant si c'est un suspect ou une affaire.

## Les règles d'usage

- <règle> (statut, source)

Exemples : la note prouve, le score résume, l'étape suit, la tâche agit ; un clic ou une ouverture de mail ne fait jamais avancer une étape.

## La règle pour contacter un collègue d'un interlocuteur

<demander l'accord de l'interlocuteur, ou simplement le prévenir>

## Un seul CRM

Si un autre CRM ou un autre outil reçoit les mêmes informations (par exemple en copie de tous les mails), il faut trancher lequel fait foi. Deux CRM font deux vérités.
