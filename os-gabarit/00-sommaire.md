# OS de l'entreprise : sommaire

L'OS de l'entreprise est la mémoire commune de sa façon de vendre : ce qu'elle vend, à qui, par quelles étapes, et ce qu'on s'attend à entendre chez chaque type de client. Il appartient à l'entreprise et reste chez elle, dans le dossier `os`. Le harnais de chaque commercial le lit sans en garder de copie. Dans une équipe, il n'y écrit que dans le fichier des constats du terrain. Chez celui qui vend seul, il y écrit aussi, sur son go, parce que celui qui vend seul est sa propre personne autorisée (voir « Qui fait quoi »).

Le harnais lit d'abord ce sommaire, puis seulement les fichiers utiles à la tâche du moment.

## Qui fait quoi

| Rôle | Nom | Ce qu'il fait |
|---|---|---|
| Personne autorisée | <nom et fonction, en général le dirigeant ou le directeur commercial> | Elle valide l'OS, change une règle révisable, tranche les constats du terrain. Seule elle écrit dans l'OS, hors constats. |
| Commerciaux | <noms, un par ligne, avec leur nom de propriétaire dans le CRM> | Chacun a son harnais, qui lit cet OS et écrit dans le CRM sur les fiches dont il est propriétaire. |

Celui qui vend seul est à la fois la personne autorisée et le commercial : il écrit son nom sur les deux lignes. Il valide son OS et le change quand il le décide, et le harnais l'y aide sur son go, puis ajoute la ligne au journal des changements, plus bas. Il n'a pas besoin de nom de propriétaire, puisque tout son CRM, ou son registre s'il n'a pas de CRM, est à lui.

## L'édition

- Édition : solo

L'édition solo contient le socle. L'édition équipe y ajoute les fichiers marqués « équipe » dans le tableau ci-dessous. Le harnais vérifie la présence de ces fichiers au moment où il en a besoin : quand un fichier est absent, les règles qui s'y rapportent ne s'appliquent pas, et rien ne bloque. La section « Quand un fichier d'équipe manque » dit ce qui s'applique à leur place.

## Où vit cet OS

- <chemin du dossier partagé de l'entreprise, ou « sur l'ordinateur du commercial » pour celui qui vend seul>

Chez celui qui vend seul, l'OS est le dossier `os/`, posé à côté du dossier `harnais/`. Dans le kit gratuit, le harnais le crée à l'installation en copiant une seule fois le gabarit `os-gabarit/`, et une mise à jour ne l'écrase jamais. Dans une équipe, l'OS vit dans un seul dossier partagé, que chaque commercial voit à côté de son harnais sous le nom `os`. Personne n'en garde de copie.

## Les fichiers de l'OS

| Fichier | Ce qu'il porte | Requis pour démarrer | Édition |
|---|---|---|---|
| `01-offre-et-pitchs.md` | Ce que l'entreprise vend, à qui, et comment elle le dit | Oui | socle |
| `02-icp.md` | Les types de clients, rangés dans les quatre cercles | Oui | socle |
| `03-parcours-client.md` | Les étapes, les règles de cadrage, les motifs de refus et les règles de nurturing | Oui, au moins les étapes | socle |
| `spiced-reference/` | Un SPICED de référence par couple offre et type de client | Oui, un seul au départ | socle |
| `04-battle-cards.md` | Les concurrents et la façon de répondre quand le client les cite | Non | socle |
| `05-grille-des-contreparties.md` | Ce que le commercial peut céder en négociation, et jusqu'où seul | Non | équipe |
| `06-mots-interdits.md` | Les mots et les promesses que l'entreprise refuse | Non | équipe |
| `07-ordre-du-point-du-matin.md` | L'ordre dans lequel le harnais classe les actions du jour | Non (l'ordre LABK s'applique par défaut) | équipe |
| `08-autorisations.md` | Ce que l'entreprise permet au harnais de ses commerciaux | Non (le commercial décide seul à l'installation) | équipe |
| `09-objectifs.md` | Les objectifs fixés aux commerciaux | Non | équipe |
| `10-constats-du-terrain.md` | Ce que les harnais font remonter du terrain | Non (vide au départ) | équipe |
| `11-crm.md` et `crm/config.json` | L'outil CRM ou le registre qui le remplace, les champs obligatoires, les règles d'usage, et les noms techniques des objets, étapes et champs | Oui (sans CRM, le registre décrit dans `11-crm.md` suffit) | socle |
| `12-routines.md` | Les routines retenues, quand le CRM ne les porte pas | Non | équipe |
| `collecte/liste-minimale.md` | Les trente-quatre demandes qui remplissent l'OS | Oui (c'est une liste à suivre, rien à y écrire) | socle |

## Quand un fichier d'équipe manque

Dans l'édition solo, les fichiers marqués « équipe » ne sont pas là, et c'est normal. Le harnais ne les invente pas et ne vous rappelle pas leur absence à chaque fois. Voici ce qui s'applique à leur place :

- sans grille des contreparties (`05`), aucune grille n'encadre la négociation : ce que vous cédez reste votre décision ;
- sans liste des mots interdits (`06`), le harnais n'a pas de liste à relire avant de vous proposer un message. Chez celui qui vend seul, le harnais crée ce fichier à l'installation si vous nommez des mots ou des promesses que vous refusez (demande 25), et il le relit ensuite avant chaque message ;
- sans ordre du point du matin (`07`), l'ordre LABK du point du matin s'applique ;
- sans autorisations (`08`), vous décidez seul, à l'installation, de ce que le harnais peut lire et écrire ;
- sans objectifs (`09`), aucune cible n'est comparée ;
- sans fichier des constats du terrain (`10`), un constat s'écrit dans `personnel/constats-a-remonter.md`, dans le dossier du harnais. Chez celui qui vend seul, le harnais l'y écrit quand même, et il vous propose tout de suite de changer la règle concernée dans votre OS, sur votre go ; si vous le faites, la colonne « Reporté le » prend la date du jour ;
- sans fichier des routines (`12`), le harnais lit les routines dans le CRM s'il porte l'objet Routine (`11-crm.md`), et sinon aucune routine ne tourne d'elle-même : le point du matin se fait quand vous écrivez « point du matin ».

## Le brief de voix de l'entreprise

Le brief de voix dit comment l'entreprise écrit à ses clients. Le harnais le relit avant de rédiger un message pour un commercial. S'il n'existe pas, écrivez « absent » : le harnais écrit alors sans lui.

- Emplacement : <chemin du fichier, ou « absent »>

## Le statut de chaque ligne

Chaque ligne de l'OS porte un statut. C'est le même statut que dans la synthèse de la collecte faite avec LABK, et le harnais l'emploie aussi quand vous remplissez l'OS seul avec lui :

- `validee` : un fait montré par une pièce de l'entreprise, ou une règle décidée par une personne autorisée ;
- `hypothese` : une parole du dirigeant ou un travail fait avec une IA, à confirmer par le terrain ;
- `absente` : une information qui manque encore.

Une hypothèse fait foi tant que le terrain ne la contredit pas. Le harnais s'en sert, et il signale quand une affaire réelle la contredit.

## Qui peut changer quoi

Chaque règle de l'OS est soit immuable, soit révisable.

- **Immuable** : personne ne la change par le circuit des constats du terrain. C'est le cas de ce qui vient du référentiel LABK : le SPICED, l'ACRAC, les deux pipelines et les quatre cercles de l'ICP. La méthode LABK elle-même (placement sur preuve, douleur et impact, événement critique, ACRAC, reviews) vit dans la base du harnais, dossier `../harnais/methode/`, qui se met à jour avec chaque version.
- **Révisable** : une personne autorisée la change quand tout le monde est d'accord qu'elle n'est plus valable. C'est le cas des règles de cadrage, des règles de nurturing, de la grille des contreparties ou de l'ordre du point du matin.

Ces fichiers sont faciles à ouvrir et à modifier : la distinction entre immuable et révisable relève d'une charte de bon usage, pas d'un verrou. Elle tient par trois choses.

1. **Le harnais ne change jamais une règle de l'OS de lui-même.** Quand un commercial d'une équipe lui demande de modifier une règle de l'entreprise, il refuse et propose d'en faire un constat du terrain. Chez celui qui vend seul, le commercial est aussi la personne autorisée : le harnais l'aide alors à changer la règle, sur son go.
2. **Tout changement laisse une trace.** Celui qui change une règle ajoute une ligne au journal ci-dessous : la date, son nom, la règle et la raison. Quand le harnais aide celui qui vend seul à changer son OS, c'est lui qui écrit cette ligne. Un changement sans ligne de journal se voit à la relecture.
3. **Un vrai verrou reste possible dans une équipe.** Si l'entreprise le veut, elle range le dossier `os` dans un espace partagé (Google Drive, SharePoint) où les commerciaux n'ont que le droit de lecture.

## Le journal des changements de l'OS

| Date | Qui | Règle ou fichier changé | Raison |
|---|---|---|---|
| <date> | <nom> | <fichier, règle> | <constat ou décision à l'origine> |

## D'où vient le contenu

L'OS se remplit à partir des trente-quatre demandes de `collecte/liste-minimale.md`, de deux façons. Celui qui vend seul les remplit avec son harnais, à l'installation, et seulement pour le minimum qui fait tourner le harnais : l'offre, l'ICP, le parcours client et un premier SPICED de référence. Une entreprise accompagnée par LABK les remplit par la collecte, le diagnostic et les ateliers. Chaque fichier dit en tête quelles demandes l'alimentent et ce qu'il faut remplir pour démarrer.

## Version

Gabarit de l'OS, version 0.5 du 23/11/2026.
