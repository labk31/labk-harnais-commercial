---
name: installation
description: Installe le harnais chez un commercial (installation neuve), aide à remplir l'OS quand il est encore vide, copie et remplit le registre qui remplace le CRM quand il n'y en a pas, ou reprend un outil existant comme un ancien coach CRM sans rien perdre de ce qu'il a appris (reprise). Se déclenche sur « installe-toi », « reprends mon ancien coach », « on reprend l'installation », ou quand le dossier personnel du harnais n'existe pas encore.
---

# L'installation et la reprise

Tu installes toi-même le harnais, en menant la session avec le commercial. Deux questions au maximum par échange. Tu t'arrêtes à chaque temps pour le laisser parler.

Tous les chemins de cette skill se lisent depuis le dossier du harnais : `../os/`, `../os-gabarit/` et `../registre/` sont donc à côté de lui, jamais dedans.

## Celui qui vend seul, et l'entreprise qui a une équipe

Cette skill sert deux situations. Tu sais laquelle s'applique dès la séance 1 : elle est écrite dans `../os/00-sommaire.md`, ligne « Édition » (le kit gratuit est toujours en édition solo), et tu la confirmes avec le commercial par sa réponse à « Vendez-vous seul, ou avec d'autres commerciaux ? ».

**Chez celui qui vend seul**, il est à la fois l'entreprise, sa personne autorisée, son dirigeant et son commercial. Tu sautes alors, sans les lui présenter, tout ce qui suppose quelqu'un d'autre : le nom de propriétaire dans le CRM, les autres harnais sur le même CRM, le message au dirigeant, la personne autorisée à qui transmettre un constat, le dossier partagé de l'équipe. Quand une règle de cette skill dit « la personne autorisée décide », c'est lui qui décide, tout de suite, sur ton go demandé à lui. Tu sautes aussi ce qui suppose un outil qu'il n'a pas : sans CRM, il n'y a ni automatisation à lister, ni connecteur à tester, ni existant à relire ; sans pipeline Maturation dans la configuration, il n'y a pas d'animation de la Maturation ; sans fichier `../os/12-routines.md` ni objet des routines dans le CRM, il n'y a pas de routine à activer, et le point du matin se lance quand il écrit « point du matin ».

**Dans une entreprise qui a une équipe**, l'OS est en général rempli avant l'installation, et chaque commercial installe son propre harnais.

## Des séances d'environ une heure, pas une après-midi

L'installation se fait en séances d'environ une heure, à des jours différents si le commercial le veut. Une installation d'une traite dure plus de trois heures, et personne ne reste attentif aussi longtemps. Chez celui qui vend seul, compte quatre à six heures au total, selon le nombre de prospects à reprendre et la facilité à dire ce qu'il vend `[hyp : estimation à vérifier à la première vraie installation]`. Tu le lui dis honnêtement au début, sans promettre moins.

| Séance | Pour qui | Ce qui s'y fait | Sections |
|---|---|---|---|
| 1. Le cadre | Tout le monde | Les vérifications, la copie du gabarit de l'OS et, sans CRM, celle du registre s'il le faut, la partie personnelle, l'accueil du commercial | 0, 1, 2 |
| 2. L'OS minimum | Celui qui vend seul, quand son OS est encore vide | L'offre, l'ICP, le parcours client et un premier SPICED de référence, puis un premier point du matin sur ses trois affaires les plus chaudes | 2 bis |
| 3. L'existant | Tout le monde | La reprise d'un ancien outil s'il y en a un, l'existant du CRM ou, sans CRM, le remplissage du registre, puis le tour du portefeuille | 3, 3 bis ou 3 ter, 4 |
| 4. Le départ | Tout le monde | La première mission, puis le point du matin sur tout le portefeuille | 4 bis, 5 |

Celui qui vend seul fait donc au moins quatre séances. Une entreprise dont l'OS est déjà rempli n'a pas de séance 2 et en fait trois.

Une séance qui ne tient pas dans l'heure continue à la séance suivante, sous le même nom suivi de « suite » (par exemple « séance 2, suite »), plutôt que de déborder. Si la séance 2 ne tient pas dans l'heure, tu t'arrêtes à la fin du bloc de demandes en cours, et les blocs qui restent, puis le premier point du matin sur les trois affaires, ouvrent la séance 2, suite. Si le tour du portefeuille ne tient pas dans la séance 3, par exemple avec une quinzaine de prospects ou plus, il continue à la séance 3, suite, avant le départ.

**La reprise.** À la fin de chaque séance, et aussi quand le commercial s'arrête au milieu d'une séance, tu écris une ligne dans `personnel/journal.md` : dans la colonne « Ce qui s'est passé », la séance et ce qui est fait ; dans la colonne « Ce qui reste ouvert », la phrase « Installation : reprendre à la séance N, section X », où N peut être une suite (« séance 2, suite »), suivie de ce qui reste à faire dans cette section. Quand le commercial revient et dit « on reprend l'installation », tu relis la dernière ligne de ce journal dont la colonne « Ce qui reste ouvert » commence par « Installation », tu lui dis en une phrase où vous en êtes, et tu repars de là, sans refaire ce qui est fait. Quand l'installation est finie, cette colonne le dit : « Installation terminée ».

## 0. Vérifier ce qui est là

Avant tout, tu vérifies cinq choses, dans cet ordre, et tu dis en une ligne ce qui manque.

**Les prérequis de `PREREQUIS.md`.** Tu ouvres un fichier de ce dossier, puis tu lances `python3 --version`. Si cette commande échoue, tu essaies `python --version`, puis `py --version` (Windows) ; tu notes celle qui répond dans `personnel/profil.md`, section « Python », dès que ce fichier existe. Si tu ne peux ni ouvrir les fichiers ni lancer Python, tu le dis tout de suite au commercial, avec la phrase de `PREREQUIS.md` qui explique pourquoi, et tu ne vas pas plus loin.

**L'OS, dans `../os/`.** Trois cas se présentent.

- `../os/` existe déjà : tu ne copies rien, même s'il te paraît vide ou ancien, et tu ne touches à aucun de ses fichiers. C'est l'OS de l'entreprise.
- `../os/` n'existe pas, mais `../os-gabarit/` existe : c'est le kit gratuit. Sa racine contient `harnais/` (ce dossier), `os-gabarit/` (le gabarit vide de l'OS) et un `CLAUDE.md` d'entrée. Tu dis au commercial en une phrase que tu crées son OS à partir du gabarit, puis tu copies `../os-gabarit/` vers `../os/`, une seule fois, avec tout son contenu. Tu ne touches plus jamais à `../os-gabarit/` ensuite : il ne sert qu'à cette copie. Le fichier `.gitignore` du kit exclut `os/`, `registre/` et `harnais/personnel/`, donc une mise à jour par `git pull` ne touche jamais ce que la personne a écrit, seulement le harnais et le gabarit.
- Ni l'un ni l'autre n'existe : tu demandes au commercial où est l'OS de l'entreprise, et tu ne crées rien avant sa réponse. Dans une équipe, l'OS vit dans un dossier partagé (voir « Un seul OS pour toute l'équipe » ci-dessous).

**Le contenu de l'OS.** L'OS porte au moins `00-sommaire.md`, l'offre (`01-offre-et-pitchs.md`), l'ICP (`02-icp.md`) et le parcours client (`03-parcours-client.md`). S'ils ne contiennent encore que les exemples du gabarit (les mentions entre chevrons, comme `<nom de l'activité>`), l'OS est vide. Chez celui qui vend seul, la séance 2 a alors lieu (section 2 bis), et c'est toujours le cas juste après la copie du gabarit. Dans une équipe, tu suis le premier paragraphe de la section 2 bis.

**Le CRM.** Tu demandes au commercial s'il a un CRM. S'il en a un, tu vérifies qu'il est joignable par le connecteur nommé dans `../os/crm/config.json` (clé `crm.serveur_mcp`) ; si le connecteur manque, tu le dis. Chez celui qui vend seul, le registre sert alors en attendant. Dans une équipe, tu le dis et tu proposes un constat pour la personne autorisée : tu ne crées pas de registre à côté du CRM de l'entreprise. Chez celui qui vend seul sans CRM, ou sans connecteur, tu copies `gabarits/registre/` vers `../registre/` : deux fichiers de tableur vides, `contacts.csv` et `echanges.csv`, et leur `LISEZ-MOI.md`. Tu le lui dis en une phrase : « Sans CRM, je tiendrai votre suivi dans le registre, deux fichiers de tableur à côté de ce dossier, que vous pourrez ouvrir avec votre tableur habituel. » Dans le même geste, tu écris `null` dans `crm.serveur_mcp` de `../os/crm/config.json` et « aucun, registre `../registre/` » sur la ligne « CRM » de `../os/11-crm.md` : sa réponse vaut l'ordre d'écrire, comme toute réponse validée à l'installation (section 2 bis), et tu lui dis en une ligne ce que tu as écrit et où. Dans une équipe qui n'a pas de CRM, le registre sert aussi, mais tu n'écris rien dans l'OS : tu prépares ces deux lignes, et celles de la section 3 ter, dans un constat pour la personne autorisée. Tu copies le registre dans `../registre/`, à côté de ce harnais, sur le go du commercial, dès qu'elle les a écrites.

**La partie personnelle.** Le dossier `personnel/` n'existe pas encore. S'il existe, le harnais est déjà installé : tu ne réinstalles rien. Si la dernière ligne « Installation » de `personnel/journal.md` ne dit pas « Installation terminée », tu proposes de reprendre l'installation là où elle s'est arrêtée ; sinon, tu proposes une mise à jour (skill `mise-a-jour`).

Si un fichier de l'OS est vide, tu le dis, et tu continues avec ce qui existe : une hypothèse fait foi tant que le terrain ne la contredit pas. Si un fichier de l'OS manque, tu suis la règle de `CLAUDE.md` (« Un fichier de l'OS peut manquer, et rien ne bloque ») : tu ne le réclames pas, et tu ne le crées pas de toi-même. La seule exception est le fichier des mots refusés, que la section 2 bis crée quand celui qui vend seul en nomme.

### Un seul OS pour toute l'équipe

Cette partie ne vaut que dans une équipe. Quand plusieurs commerciaux vendent pour la même entreprise, il n'y a qu'un seul OS. Il vit dans un dossier partagé de l'entreprise (Google Drive, SharePoint, ou tout dossier synchronisé), et chaque commercial le voit à côté de son harnais, sous le nom `os`. Chaque commercial a son propre harnais ; aucun ne garde de copie de l'OS. Ainsi, une règle changée par la personne autorisée vaut le lendemain pour tout le monde.

Si les commerciaux n'ont que la lecture sur le dossier partagé, le harnais ne peut pas écrire dans `../os/10-constats-du-terrain.md`. Il écrit alors le constat dans `personnel/constats-a-remonter.md`, et il le rappelle au commercial au point du matin, jusqu'à ce que la personne autorisée l'ait reporté.

## 1. Créer la partie personnelle

Tu copies `gabarits/personnel/` vers `personnel/`, avec tous ses fichiers et ses dossiers. Ce dossier appartient au commercial. Les mises à jour du harnais ne le touchent jamais. Tu lui dis en une ligne que c'est fait et où.

## 2. L'accueil du commercial

Tu remplis `personnel/profil.md` avec lui, dans cet ordre :

1. **Qui il est** : son nom, son rôle, ses types de clients et ses segments. Dans une équipe, tu lui demandes aussi son nom de propriétaire dans le CRM ; chez celui qui vend seul, tu écris « sans objet ».
2. **Ses outils** : son espace de travail (Google, Microsoft, autre), sa messagerie, son agenda, son outil de visio, et son IA. Tu vérifies ce que tu peux lire par un connecteur. S'il n'a pas de CRM, tu écris « aucun, registre `../registre/` » sur la ligne CRM du profil, pour que les séances suivantes le sachent. Quand un outil n'est pas relié à l'IA, tu ne bloques rien : tu notes « non » dans la colonne « Le harnais peut le lire », et tu lui dis qu'il te collera ce que tu dois savoir.
3. **Ce qu'il permet** : lire sa boîte mail, son agenda, écrire dans son agenda et dans le CRM ou le registre après son go. Ces choix restent dans les limites de `../os/08-autorisations.md`, s'il existe ; sinon, le commercial décide seul, ce qui est toujours le cas chez celui qui vend seul. S'il refuse une chose, tu la notes et tu fais sans.
4. **Comment il t'apporte ses échanges** : il colle la transcription, il joint un fichier, il te raconte l'échange en quelques phrases, ou il a un dossier où les transcriptions arrivent.
5. **Son point du matin** : l'heure à laquelle il veut le lire. Tu lui montres l'ordre de tri qui s'applique : celui de `../os/07-ordre-du-point-du-matin.md` s'il existe et qu'il est rempli, sinon l'ordre LABK (section 2 de la skill `point-du-matin`), que tu lui résumes en une phrase. S'il veut un autre ordre, c'est une règle personnelle : tu suis la procédure « Le commercial a le dernier mot » de `CLAUDE.md`, tu lui cites une fois les situations qu'elle ferait passer après (par exemple une option qui tombe dans deux jours), puis tu l'inscris dans `personnel/regles-personnelles.md`. Tu ne la ranges jamais dans le profil.

Tu lui demandes aussi si un autre CRM tourne en parallèle, par exemple en copie de ses mails. Deux CRM font deux vérités : tu le notes dans `personnel/journal.md`, et c'est à l'entreprise de trancher. Chez celui qui vend seul, c'est lui qui tranche, et tu notes sa décision.

**Plusieurs harnais sur le même CRM.** Ce paragraphe ne vaut que dans une équipe ; chez celui qui vend seul, tout le CRM est à lui, et tu le sautes. Dans une équipe, chaque commercial a son harnais, et tous lisent le même CRM. Ils ne se gênent pas, parce que chacun n'écrit que dans son périmètre : les fiches dont son commercial est propriétaire, lues dans le champ désigné par `crm.champ_proprietaire`. Sur la fiche d'un collègue, le harnais lit, mais il n'écrit pas : il propose au commercial de prévenir le collègue, avec le fait et sa preuve. Une fiche sans propriétaire se signale ; le harnais propose au commercial de la prendre, et il ne l'écrit qu'après son go. Si l'entreprise a plusieurs commerciaux et que le CRM n'a pas de champ propriétaire, tu le dis : tant que l'architecte CRM ne l'a pas posé, deux harnais risquent d'écrire sur la même fiche, et tu ne proposes d'écriture que sur les affaires que le commercial te désigne comme les siennes.

Quand il a un CRM, tu lui demandes aussi si un autre assistant d'IA, qui n'est pas un harnais LABK, agit déjà dessus, par exemple une automatisation ou un autre agent. Si c'est le cas, tu le notes dans `personnel/journal.md`, tu le signales, et tu n'écris pas sur les fiches que cet assistant modifie tant que l'entreprise n'a pas dit lequel fait foi. Sans CRM, la question n'a pas d'objet.

Tu lui demandes enfin où sont les retours d'expérience de l'entreprise, c'est-à-dire les cas clients racontés, chiffrés si possible : un dossier, un lien, ou « aucun ». Chez celui qui vend seul, ce sont ses propres cas clients, même s'ils ne sont écrits nulle part ; « aucun » est une réponse normale. Tu notes leur emplacement dans `personnel/profil.md`.

**Le SPICED de référence.** Quand l'OS est rempli, tu vérifies qu'il porte un SPICED de référence pour son type de client principal, dans l'ordre de pose écrit dans `../os/spiced-reference/LISEZ-MOI.md`. Quand l'OS est vide, ce premier SPICED se pose à la séance 2 (section 2 bis), et tu ne le réclames pas ici. Pour ses autres types de clients, tu ne réclames rien tant qu'aucune affaire de ce type n'est ouverte : quand la première arrive sans SPICED de référence, tu le dis, sans l'inventer, et tu proposes un constat du terrain pour que la personne autorisée le fasse poser (chez celui qui vend seul, tu proposes de le poser avec lui). En attendant, tu prépares les rendez-vous de ce type de client avec les questions générales de `methode/douleur-et-impact.md`, et tu le dis.

## 2 bis. Remplir l'OS minimum, quand il est vide

Cette partie sert à celui qui vend seul : personne n'a encore écrit comment il vend, et il est la seule personne qui puisse le faire. Dans une entreprise accompagnée par LABK, l'OS est rempli avant l'installation, et cette partie ne s'applique pas. Dans une équipe dont l'OS est encore vide, tu ne l'écris pas toi-même : tu le dis au commercial, tu continues avec ce qui existe, et c'est la personne autorisée qui le remplit, seule ou avec LABK, comme le décrit `../os/collecte/liste-minimale.md`.

**Ce que tu remplis.** Le minimum qui fait tourner le harnais : l'offre (`../os/01-offre-et-pitchs.md`), l'ICP (`../os/02-icp.md`), le parcours client (`../os/03-parcours-client.md`) et un premier SPICED de référence pour son type de client principal (`../os/spiced-reference/`, sur le modèle de `_modele.md`). Le reste de l'OS se remplit plus tard, au fil des affaires, quand une situation en a besoin.

**Comment tu demandes.** Tu suis les demandes de `../os/collecte/liste-minimale.md`, bloc par bloc, dans l'ordre, jamais toutes d'un coup. La règle des deux questions par échange s'applique toujours : un bloc se répartit sur autant d'échanges qu'il faut. Tu les poses avec tes mots, en t'adressant à lui. Tu ne lui demandes pas de connaître la méthode : il n'a jamais entendu parler du SPICED, des quatre cercles de l'ICP ni du parcours client, et il n'en a pas besoin pour répondre. La première fois qu'un de ces mots sert, tu l'expliques en une phrase : par exemple, « le SPICED, ce sont les cinq choses à savoir d'un client avant de lui faire une proposition : sa situation, ce qui le gêne, ce que ça lui coûte, ce qui l'oblige à décider avant une date, et qui décide ».

Pour celui qui vend seul, tu poses dix-huit demandes, en quatre blocs, et seulement pour son type de client principal :

| Bloc | Demandes de la liste | Ce que tu écris |
|---|---|---|
| A. Ce qu'il vend | 1, 29, puis 25 (ses pitchs et les mots qu'il refuse) | `../os/01-offre-et-pitchs.md` |
| B. Ses clients | 2 et 5, puis il désigne le type de client qui pèse le plus dans son chiffre d'affaires, puis 6, 7 et 9 pour ce type | `../os/02-icp.md`, la première ligne de l'ordre de pose dans `../os/spiced-reference/LISEZ-MOI.md`, et la valeur délivrée à ce type dans `../os/01-offre-et-pitchs.md` |
| C. Comment ses clients achètent | 10, 21, 15, 16 et 18 | `../os/03-parcours-client.md` |
| D. Qui décide chez ce client | 11, 12, 13, 14 et 17 | Le premier SPICED de référence, `../os/spiced-reference/spiced-reference-<offre>-<type de client>.md`, avec ce que les blocs B et C ont déjà dit |

Les autres demandes attendent, et tu le lui dis : les questions 3, 4 et 8 viennent avec le temps ; les concurrents (19 et 20) remplissent `../os/04-battle-cards.md` quand un client en cite un, et la réponse à la demande 18 y va aussi si elle nomme un concurrent ; les outils (23 et 24) ont été vus à la séance 1 ; les pièces (26 à 28 et 30 à 34) se lisent quand il les apporte. La demande 22 ne se pose pas : il vend seul, il est la personne autorisée. La demande 34 parle de ce que « l'équipe » a produit avec l'IA ; chez lui, ce sont ses propres conversations et notes, s'il en a.

Au bloc D, avant d'écrire son premier SPICED de référence, tu lui montres l'exemple fictif de `../os/spiced-reference/exemple-fictif-consultant-organisation.md`, pour qu'il voie à quoi ressemble un SPICED de référence rempli, puis vous écrivez le sien. Tu ne recopies jamais l'exemple : ses lignes sont inventées.

**Quand la réponse ne vient pas.** Il ne sait pas toujours répondre, et c'est normal. Quand il dit « je ne sais pas », tu ne repasses pas la question : tu proposes un premier jet, tiré de ce que tu peux lire (son site, un devis, un mail qu'il te colle, ses meilleurs clients cités), et tu lui demandes ce qui est faux. Chaque ligne que tu écris porte le statut `hypothese` et sa source ; elle fait foi tant que le terrain ne la contredit pas.

**Les quatre cercles de l'ICP.** Tu ranges toi-même, en `hypothese`, les types de clients qu'il a cités : son type principal et ceux qui signent et restent dans le cercle cœur, ceux de la demande 5 dans l'anti-cercle. Le cercle futur et le faux cercle restent vides tant qu'il n'a pas répondu aux demandes 3 et 4, qui viennent avec le temps. Tu lui montres le rangement en quatre lignes et il corrige. Chez lui, il n'y a pas de diagnostic ni d'atelier : ce rangement en tient lieu jusqu'à ce que ses affaires réelles le contredisent.

**Le parcours client.** Il n'a pas d'étapes en tête, et tu ne lui en demandes pas. Tu pars des étapes déjà écrites dans `../os/crm/config.json` (`crm.etapes_suspect` et `crm.etapes_opportunite`), tu les décris en mots simples dans `03-parcours-client.md` avec ce que ses réponses du bloc C t'ont appris (ce qui se passe avant qu'un client l'appelle, comment il arrive, pourquoi il signe ou ne signe pas), et tu lui demandes ce qui ne colle pas à sa façon de vendre. S'il renomme une étape, tu changes le nom dans la configuration et le sens dans le parcours client, aux deux endroits à la fois. Sans CRM, les noms en mots simples retenus dans le parcours client sont ceux qui s'écrivent dans la colonne `etape` du registre, comme le dit `CLAUDE.md`, et la configuration n'a pas à suivre. Il s'en tient à une seule suite d'étapes : la configuration ne désigne pas de pipeline Maturation, et le harnais saute ce qui s'y rapporte.

**Les mots qu'il refuse.** Si, à la demande 25, il nomme des mots ou des promesses qu'il refuse d'employer, tu crées `../os/06-mots-interdits.md`, qui n'est pas dans le kit, avec une phrase d'introduction et un tableau à deux colonnes : « Le mot ou la promesse refusés » et « Ce qu'il dit à la place ». Tu le relis ensuite avant chaque message, comme le dit `CLAUDE.md`. S'il n'en nomme aucun, tu ne crées pas ce fichier.

**Le sommaire et la configuration.** Tu écris dans `../os/00-sommaire.md` « solo » sur la ligne « Édition », son nom et sa fonction sur la ligne « Personne autorisée », son nom sur la ligne « Commerciaux », « sur l'ordinateur du commercial » sous « Où vit cet OS », et « absent » pour le brief de voix s'il n'en a pas. Tu ajoutes une ligne au journal des changements du sommaire : la date, son nom, « OS minimum écrit à l'installation », et « séance 2 de l'installation ». Dans `../os/crm/config.json`, tu remplaces `instance` par le nom de son entreprise.

**Pourquoi tu écris dans l'OS.** Pendant l'installation, tu écris dans l'OS, ici comme aux sections 0 et 3 ter, parce qu'il est la personne autorisée de sa propre entreprise : chaque réponse validée est l'ordre d'écrire, et tu lui dis en une ligne ce que tu as écrit et où. Après l'installation, chez celui qui vend seul, tu continues de l'aider à changer son OS sur son go, comme le dit `CLAUDE.md` (« Tu ne changes jamais une règle de l'OS »).

**Un premier résultat dès cette séance.** À la fin de la séance 2, tu lui demandes ses trois affaires les plus chaudes, en une ligne chacune : l'entreprise, la personne, la date du dernier échange, et ce qui a été promis, par qui. S'il a un CRM, tu les y retrouves par le connecteur, sans rien y écrire avant la séance 3, qui relève sa configuration ; le point du matin de ce jour s'appuie sur ce qu'il t'a dit et sur ce que ses fiches montrent. Sans CRM, tu prépares pour chacune une ligne de `../registre/contacts.csv`, à l'étape que sa parole prouve (`methode/placement-sur-preuve.md`) et sans aucun score SPICED, et une ligne de `../registre/echanges.csv` pour ce dernier échange, avec les promesses dans la colonne `engagements` ; tu ne remplis jamais une date ou une promesse qu'il ne t'a pas donnée. Sur son go, tu les écris, puis tu lui rends un premier point du matin sur ces trois affaires seulement, avec la skill `point-du-matin` (section 3 bis, « Quand le portefeuille est presque vide »). Tu lui dis comment y répondre : d'un mot par ligne, « fait », « plus tard » ou « non ». Il repart avec quelque chose d'utile avant même la reprise de tout son portefeuille.

## 3. La reprise d'un outil existant

Cette partie ne s'applique que si le commercial avait déjà un outil, par exemple un coach CRM installé par LABK. Sinon, tu la sautes sans en parler. Tu ne supprimes jamais l'ancien outil : il reste en place, intact, tant que le commercial n'a pas vérifié que tout est passé.

Tu lis l'ancien outil, en lecture seule, et tu ranges chaque élément au bon endroit :

| Ce que tu trouves dans l'ancien outil | Où ça va |
|---|---|
| Les règles d'usage du CRM, les étapes, les délais, les règles de l'entreprise | À reporter dans `../os/`, par la personne autorisée de l'entreprise : tu les prépares dans le compte rendu de reprise, fichier par fichier |
| La configuration du CRM (noms d'objets, d'étapes, de champs) | À reporter dans `../os/crm/config.json` par la personne autorisée : tu la prépares dans le compte rendu de reprise, après l'avoir comparée au schéma réel du CRM |
| Les SPICED de référence | À reporter dans `../os/spiced-reference/` par la personne autorisée : tu les prépares dans le compte rendu de reprise |
| Les populations à couvrir, les surveillances en cours | `personnel/suivi.md` |
| Le journal des décisions et les questions ouvertes | `personnel/journal.md` |
| Les règles décidées par le commercial, ou validées par l'ancienne boucle | `personnel/regles-personnelles.md`, avec leur date et leur origine |
| Les traces (`raw/traces/`) | `personnel/raw/traces/`, copiées telles quelles |
| Le wiki (`wiki/`) | `personnel/wiki/`, copié tel quel |

Quand un élément ne trouve pas sa place, tu ne le jettes pas : tu le listes.

Dans une équipe, tu n'écris jamais toi-même dans l'OS pendant la reprise : ce qui lui revient attend, dans le compte rendu, que la personne autorisée de l'entreprise le reporte. Chez celui qui vend seul, il est cette personne : tu lui montres ce qui revient à l'OS, fichier par fichier, et tu le reportes sur son go.

Tu rends ensuite **le compte rendu de reprise**, que tu écris dans `personnel/reprise-AAAA-MM-JJ.md` : ce qui est allé dans l'OS, ce qui est allé dans la partie personnelle, ce qui n'a pas trouvé de place, et les écarts entre l'ancienne configuration et le CRM réel. Le commercial peut l'envoyer à son consultant : il ne contient que des noms de fichiers et de règles, aucune donnée client.

## 3 bis. L'existant du CRM

Cette partie ne s'applique que s'il y a un CRM. Sans CRM, tu passes à la section 3 ter.

Le CRM n'est presque jamais vide le jour de l'installation. Tu ne réécris rien de ce qui existe : tu le lis, et tu le fais entrer dans la méthode au fil des échanges.

- **Les affaires en cours restent à leur étape.** Tu ne les déplaces pas en masse. Le tour du portefeuille (section 4) propose, affaire par affaire, l'étape que la preuve porte, et le commercial décide.
- **Les automatisations du CRM.** Tu listes celles qui tournent (règles, workflows, séquences) et tu signales celles qui font ce que le harnais fait désormais sur go, par exemple passer une étape ou créer une tâche. Tu ne les arrêtes jamais toi-même : tu proposes un constat pour que la personne autorisée décide, avec l'architecte CRM s'il y en a un. Chez celui qui vend seul, c'est lui qui décide de les garder ou de les arrêter, et il le fait lui-même dans son CRM. Deux mécanismes qui écrivent la même chose font deux vérités.
- **Les champs et les valeurs que la configuration ne connaît pas** se signalent dans le compte rendu de séance, sans être supprimés.
- **La configuration, chez celui qui vend seul.** Il n'a pas d'architecte CRM pour remplir `../os/crm/config.json`. Tu relèves toi-même, par le connecteur, les noms techniques des objets, des étapes et des champs de son CRM, tu lui montres la configuration remplie, et tu l'écris sur son go. Ce que son CRM n'a pas reste à `null`, et les skills sautent ce qui s'y rapporte ; les scores SPICED vont alors dans la note de l'affaire, sous la forme que prévoit `../os/11-crm.md`. Tu ne crées aucun champ dans son CRM pendant l'installation.

**Le dirigeant est prévenu avant que le pipeline baisse.** Placer les affaires sur preuve fait souvent descendre le montant du pipeline le premier jour : une affaire que personne n'a qualifiée retourne à l'étape que sa preuve porte. Ce n'est pas une perte, c'est la vérité du pipeline. Avant la première écriture qui fait reculer une affaire, tu prépares pour le commercial un message court au dirigeant : combien d'affaires reculent, de combien le pipeline baisse, pourquoi, et ce qui les fera remonter. Le commercial l'envoie lui-même. Celui qui vend seul est son propre dirigeant : tu ne prépares pas de message, tu le lui dis simplement, en une phrase.

## 3 ter. Le registre, quand il n'y a pas de CRM

Cette partie s'applique chez celui qui vend seul, quand il n'a pas de CRM ou que son CRM n'a pas de connecteur, et dans une équipe sans CRM, comme le dit la section 0. Elle ne s'applique jamais à côté du CRM d'une équipe, et dans une équipe tu n'écris jamais toi-même dans l'OS. Le registre tient la place du CRM, comme le dit `CLAUDE.md` (« Sans CRM, le registre ») : partout où une skill parle du CRM, d'une fiche, d'une note ou d'une tâche, elle parle du registre, avec les mêmes règles. En particulier, rien ne s'y écrit sans le go du commercial.

**Ce qui est déjà là.** La séance 1 a copié `gabarits/registre/` vers `../registre/`, à côté du harnais et de l'OS, jamais dans l'OS. Les colonnes de ses deux fichiers sont définies dans `../registre/LISEZ-MOI.md`, et nulle part ailleurs : tu ne les changes pas et tu n'en ajoutes pas. Si la séance 2 a eu lieu, les trois affaires les plus chaudes y sont déjà : tu pars de ces lignes, sans les recréer.

**Ce que l'OS dit du registre.** Chez celui qui vend seul, la séance 1 a écrit `null` dans `crm.serveur_mcp` et « aucun, registre `../registre/` » sur la ligne « CRM » de `../os/11-crm.md`. Tu ajoutes dans ce même fichier la convention des montants (hors taxe, sauf s'il en dit une autre) et, sous « Les champs obligatoires par fiche », que chaque ligne de `contacts.csv` porte au moins `entreprise`, `personne` et `etape`. Les autres clés de `../os/crm/config.json` ne changent pas : avec le registre, tu lis ses colonnes et les étapes en mots simples de `../os/03-parcours-client.md`, pas les noms de la configuration. Dans une équipe, ces lignes vont dans le constat de la section 0.

**Le remplir avec ce qu'il a déjà.** Un registre vide ne donne pas de point du matin. Tu lui demandes où sont ses contacts aujourd'hui : dans sa tête, dans sa boîte mail, dans un fichier, dans ses devis. Pour aller vite, tu lui proposes de coller une ligne par prospect, dans ce format : l'entreprise, la personne, la date du dernier échange, ce qui a été promis et par qui. S'il préfère, il te transfère ou te colle les derniers mails de chaque prospect, et tu en tires la ligne toi-même. Tu acceptes aussi une liste, un export ou ses affaires dictées en quelques phrases, sans lui demander de reformater. Si sa boîte mail est reliée à l'IA, tu proposes de relever les échanges des deux derniers mois avec ses clients et ses prospects. Tu commences par ses affaires en cours, puis par les personnes qui attendent une réponse de lui, puis par ses meilleurs clients cités à la demande 7 ; une entreprise de ces clients où aucune affaire n'est ouverte passe en veille, sur une ligne de la section « Surveillances en cours » de `personnel/suivi.md`, avec la date du jour.

Pour chaque personne, tu prépares une ligne de `contacts.csv`, à l'étape que sa parole prouve (`methode/placement-sur-preuve.md`), et, quand il t'en donne un, une ligne de `echanges.csv` pour le dernier échange, avec ce qui a été promis dans la colonne `engagements`. Tu remplis ce que tu sais et tu laisses vide ce que tu ne sais pas : tu ne remplis jamais une date ou une promesse qu'il ne t'a pas donnée, et tu signales la case vide. Tu ne poses aucun score SPICED sans une phrase du client : le tour du portefeuille s'en charge. Tu lui montres alors le lot entier, récapitulé : les lignes du registre et, chez celui qui vend seul, les lignes de `../os/11-crm.md`. Sur son go, tu écris le tout, tu relis les fichiers, puis tu lui dis en une ligne ce que tu as écrit et où.

S'il passe un jour à un CRM, le registre se reprend tel quel : chaque colonne correspond à un champ du CRM.

## 4. Le tour du portefeuille

Tu passes ses affaires ouvertes une à une, avec la section 4 de la skill `coach-crm` : l'étape, la preuve qui la justifie, la première lettre du SPICED qui manque, le geste proposé. À chaque affaire, tu lui demandes ce qu'il sait et que le CRM ou le registre ne dit pas. Ce qu'il te dit d'un client devient une proposition de note, et un score ne se propose qu'à partir des mots du client. Quand il conteste une règle de l'entreprise, tu notes la question dans `personnel/journal.md` pour la personne autorisée, et tu ne tranches pas. Chez celui qui vend seul, c'est sa propre règle : tu lui proposes de la changer dans son OS, sur son go.

Avec une dizaine d'affaires, le tour tient dans la séance. Au-delà, tu commences par celles qui ont une date dans les deux semaines, puis par les plus avancées, et tu dis lesquelles attendront le point du matin.

## 4 bis. La première mission, sur son go

Avant le point du matin de la section 5, tu prépares ce que le harnais lira ensuite, en un seul lot montré au commercial :

- pour chaque entreprise de ses affaires ouvertes et de celles qu'il garde en veille : son site, et les pages de son site qu'il veut que tu surveilles (actualités, recrutements) ; pour chaque interlocuteur, l'adresse de son profil LinkedIn, que le commercial ouvrira lui-même (voir section 14 de la skill `coach-crm`) ; avec le registre, cette adresse, comme les pages à surveiller, s'écrit dans la section « Surveillances en cours » de `personnel/suivi.md`, une ligne par interlocuteur, avec son `id` ;
- les fiches des interlocuteurs présents dans les notes mais absents du CRM ou du registre ;
- le statut de chaque interlocuteur, tiré de la date de son dernier échange connu (mail, note ou tâche faite) : « Actif » s'il a échangé depuis moins que le premier palier du silence, « En silence » au-delà, « À atteindre » s'il n'a jamais répondu. Sans cela, le statut « En silence » reste vide le premier jour, et le point du matin ne voit aucun silence ;
- les doublons, que tu signales sans rien supprimer ;
- les tâches de relance qui tombent avant le premier palier du silence, à redater, et celles dont la date est passée depuis longtemps, à clore ou à redater.

Puis, s'il y en a, tu lui montres les routines de l'entreprise, dans le CRM ou à défaut dans `../os/12-routines.md` (section 14 de la skill `coach-crm`), et tu lui proposes de passer à Active celles qu'il veut, au rythme qu'il veut. Quand ni le CRM ni ce fichier n'en portent, ce qui est le cas dans le kit gratuit, tu lui dis en une phrase que son point du matin se lance quand il écrit « point du matin », à l'heure notée dans son profil. Tu ne proposes l'animation de la Maturation que si l'entreprise a retenu ce pipeline, c'est-à-dire si `crm.etapes_maturation` est rempli dans la configuration.

## 5. Le point du matin sur tout le portefeuille

Tu rends le point du matin sur tout son portefeuille devant lui, avec la skill `point-du-matin`, et vous le lisez ensemble. C'est là qu'il apprend à te répondre, et que tu apprends ce qu'il sait. Si c'est son premier, tu lui dis comment répondre : d'un mot par ligne, « fait », « plus tard » ou « non ». Celui qui vend seul a déjà lu, à la séance 2, celui de ses trois affaires les plus chaudes : tu ne le lui réexpliques pas.

Ce point ne reprend pas ce que le lot de la première mission vient de couvrir : une fiche complétée, un statut posé ou une tâche redatée sur son go n'y reviennent pas. Il ne garde que ce qui reste à faire aujourd'hui, pour que le commercial ne valide pas deux fois la même chose.

Le rythme du portefeuille, au pied de la page, ne se compare qu'avec huit semaines d'historique dans le CRM ou le registre (deux périodes de quatre semaines, section 2 de la skill `coach-crm`). Avant, tu dis en une ligne depuis quand tu observes et à partir de quand le rythme sera comparable, sans inventer de tendance. Le premier jour d'un registre neuf, c'est toujours le cas.

## 6. Fin de chaque séance

Tu écris une ligne dans `personnel/journal.md`, au format de la section « La reprise » : la date, la séance, ce qui a été installé ou repris, et où reprendre. À la fin de la dernière séance, tu écris « Installation terminée », et tu écris la version du harnais installée, lue dans `JOURNAL.md`, dans `personnel/profil.md`, section « La version du harnais installée ».
