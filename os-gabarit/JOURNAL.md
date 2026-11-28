# Journal des versions

Chaque version du gabarit de l'OS porte un numéro et une ligne qui dit ce qui change. Un changement de gabarit ne touche jamais un OS déjà rempli chez un client : s'il le faut, la ligne dit ce que le client peut reporter dans le sien, à la main.

## v0.7 (en cours, 27/11/2026)

Ajout du 28/11/2026 : deux seuils dans `crm/config.json`, `ecart_objectif_alerte` (0.8) et `suspects_minimum_pour_taux_reel` (50), pour l'alerte du lundi sur l'écart à l'objectif. Un OS déjà rempli sans eux prend ces valeurs par défaut.

Précision du 28/11/2026 (décision de Laurent après la simulation 7) : dans `13-prospection.md`, la montée en charge compte tous les messages du jour, relances comprises. Pour un OS déjà rempli : ajouter « relances comprises » à la règle de montée en charge.

Nouveau fichier du socle, `13-prospection.md` : les canaux et leurs relais, l'envoi planifié, les adresses d'envoi, les créneaux et les absences, le rythme, la forme du go, les sources de listes, le suivi des clics, les valeurs de départ du calcul à rebours, la phrase pour ne plus être contacté, et l'endroit où vivent les campagnes. Il n'est pas requis pour démarrer, il l'est pour lancer une campagne. `crm/config.json` gagne un bloc `prospection` (noms techniques de la prospection dans le CRM, objets écrits par une machine, réglages du verdict des clics). `11-crm.md` gagne la section « La prospection dans le CRM ». `00-sommaire.md` gagne la ligne du nouveau fichier. Un OS déjà rempli peut ajouter ce fichier et ce bloc à la main, ou les remplir à la séance de la prospection de l'installation.

## v0.6 (en cours, 25/11/2026)

`08-autorisations.md` gagne trois lignes dans « Ce que le harnais ne fait jamais » : il ne fusionne aucune fiche, il ne recopie ni l'OS ni le CRM dans la partie personnelle du harnais, il n'exporte aucune liste de contacts. Un OS déjà rempli peut reporter ces trois lignes à la main.

## v0.5 (23/11/2026)

Correction des problèmes relevés par le test de déploiement d'un agent neuf, le 23/11/2026, pour la part qui touche l'OS.

`crm/config.json` gagne deux clés pour les rendez-vous (23/11/2026) : `seuils.jours_rdv_a_controler` (sept jours), la fenêtre que le point du matin croise entre l'agenda, les mails et le CRM, et `crm.champ_prochain_rdv`, le champ où le harnais écrit la date du prochain rendez-vous quand le CRM en a un. L'architecte CRM le renseigne après la pose ; laissé vide, la date vit dans la note et la tâche. Elle gagne aussi `seuils.jours_sans_echange_avant_revue_donnees` (trois ans), et une note qui dit que les clés « prospect » désignent les suspects du parcours client. Le bloc `objectif_trois_mois` n'est plus lu : l'objectif vit dans `09-objectifs.md`, et seulement là. La configuration demande le nom technique d'un champ, jamais son libellé.

La liste des trente-quatre demandes de la collecte entre dans l'OS (`collecte/liste-minimale.md`), avec, pour chaque demande, le fichier qu'elle alimente. La demande 25 recueille aussi les mots refusés et ce qu'on dit à la place.

Le sommaire dit qui fait quoi (la personne autorisée, qui valide l'OS, et les commerciaux avec leur nom de propriétaire dans le CRM), l'édition de l'OS (solo ou équipe, chaque fichier marqué « socle » ou « équipe ») et l'endroit où il vit. Dans une équipe, il n'y a qu'un seul OS, dans un dossier partagé.

Le `README.md` décrit les deux façons de remplir l'OS : seul avec son harnais, ou avec LABK par la collecte, le diagnostic, les ateliers dans leur ordre, l'architecte CRM et la validation. L'architecte reçoit le cadrage de l'atelier du parcours, il ne l'écrit pas.

Le parcours client décrit les étapes en mots simples (le nom technique ne vit que dans la configuration), définit les trois temps du pipeline des prospects (Maturation, Signature, gagné ou perdu), et dit de remplir le cadrage d'abord pour les deux premières étapes. `11-crm.md` décrit le tableur pour qui n'a pas de CRM, et ce qui change selon l'outil, Pipedrive compris. Les SPICED de référence se posent dans un ordre écrit, un seul au départ, et la vente additionnelle a le sien. La veille des routines ne lit plus LinkedIn, et l'animation de la Maturation ne vaut que si l'entreprise a ce pipeline. Un projet de licence est écrit (`LICENCE.md`), à faire relire par un juriste.

Après une relecture isolée du même jour : la configuration renomme `objet_prospect` en `objet_suspect` et `etapes_prospect` en `etapes_suspect`, et ajoute `pipeline_suspect` et `pipeline_opportunite`, pour les CRM où suspects et affaires sont le même objet. `11-crm.md` définit le socle CRM et range le tableur hors de l'OS, dans `registre/`. Le `README.md` dit comment brancher concrètement l'OS partagé, et détaille chaque atelier (ce qu'il faut avant, ce qui en sort, qui y participe, sa durée indicative). La liste des demandes aide le dirigeant qui ne sait pas, demande qui décide des règles de vente et si l'outil d'IA sait ouvrir un dossier ; elle ne renvoie plus à aucun chemin interne de LABK. Un SPICED de référence fait foi dès son premier jet.

Après le test du kit par ChatGPT du même jour : les renvois de l'OS vers la méthode pointent vers `../harnais/methode/`, `11-crm.md` renvoie au registre fourni avec le harnais, et `spiced-reference/` gagne un exemple entièrement fictif (`exemple-fictif-consultant-organisation.md`), qui montre la forme d'un SPICED de référence rempli.

Polissage du kit gratuit avant sa publication (23/11/2026), pour la part qui touche le gabarit de l'OS. Une ligne par changement :

- 00-sommaire.md dit que celui qui vend seul écrit son nom sur les deux lignes de « Qui fait quoi », qu'il change son OS lui-même avec l'aide du harnais sur son go, et que le harnais écrit alors la ligne du journal des changements ; l'introduction et la charte « Qui peut changer quoi » portent la même exception, sans toucher à la règle d'équipe.
- 00-sommaire.md gagne la section « Quand un fichier d'équipe manque », alignée sur harnais/CLAUDE.md : pour chacun des fichiers 05 à 10 et 12, elle dit ce qui s'applique à sa place dans l'édition solo, sans toucher à la ligne « - Édition : <solo ou équipe> ».
- 00-sommaire.md précise l'endroit de l'OS chez celui qui vend seul (le dossier os/ à côté de harnais/, copié une fois depuis os-gabarit/ dans le kit), ce qu'il faut pour démarrer avec le parcours client, le SPICED de référence, 11-crm.md sans CRM et la liste minimale, le brief de voix absent, et le statut des lignes quand on remplit l'OS sans LABK.
- 01-offre-et-pitchs.md, 02-icp.md, 03-parcours-client.md et 04-battle-cards.md disent en tête qui les remplit (chez celui qui vend seul, lui-même avec le harnais), ce qu'il faut pour démarrer, et quelles demandes de la liste minimale nourrissent chaque section ; les consignes de remplissage sont en phrases complètes.
- 02-icp.md ne dit plus que le rangement se fait seulement au diagnostic et en atelier : seul, il se fait avec le harnais à partir des meilleurs clients réels, chaque ligne restant une hypothèse.
- 03-parcours-client.md gagne la section « Ce qu'il faut pour démarrer » : les étapes du pipeline des prospects et la preuve du gagné, dont le harnais propose un premier jet puisque aucune demande de la liste minimale ne les fait écrire ; il dit aussi que le délai de silence de chaque étape se reporte dans crm/config.json.
- 01-offre-et-pitchs.md envoie un constat du terrain dans 10-constats-du-terrain.md s'il existe, sinon dans personnel/constats-a-remonter.md du harnais, et dit que celui qui vend seul peut ajouter l'offre lui-même.
- 11-crm.md conditionne au fichier 12-routines.md, présent dans l'édition équipe seulement, la phrase sur les routines des CRM sans objets, et renvoie à la grille SPICED « décrite plus bas » au lieu de « ci-dessus ».
- crm/config.json, sans aucune clé renommée, dit dans sa note de tête comment celui qui vend seul le remplit et ce qui sert sans CRM (serveur_mcp à null, seuils appliqués au registre), et ses notes sur 09-objectifs.md et 06-mots-interdits.md disent ce qui se passe dans l'édition solo.
- collecte/liste-minimale.md commence par les deux façons de répondre et sépare ce qui vaut dans les deux cas de ce qui vaut seulement avec LABK ; les demandes 2, 7, 8, 15 à 18, 22, 24, 25 à 29 et 34 disent ce que répond celui qui démarre, vend seul ou n'a pas de CRM ; le tableau ajoute la demande 18 au SPICED de référence et dit que 06 et 08 n'existent que dans l'édition équipe.
- spiced-reference/LISEZ-MOI.md explique le SPICED lettre par lettre à un débutant, la différence entre le SPICED d'une affaire et le SPICED de référence, les trois moments où le harnais s'en sert, qui le remplit et comment le harnais aide à poser le premier ; la règle d'un seul au départ a son titre, et celui qui vend seul décide lui-même d'une contradiction.
- spiced-reference/_modele.md dit ce qu'il faut remplir pour démarrer et ce qui reste vide jusqu'au premier échange, relie chaque section aux demandes de la liste minimale, et gagne une section « Les objections attendues » pour la demande 17, que la skill coaching lit déjà dans le SPICED de référence.
- 11-crm.md, section « Sans CRM : le registre », renvoie au LISEZ-MOI.md du registre pour ses colonnes (ligne réécrite à la fusion avec la version de 16:33), le résume sans le recopier, et dit ce que deviennent sans CRM l'objet des interlocuteurs, l'objet Routine, le champ propriétaire et les automatisations ; celui qui vend seul remplit ce fichier avec le harnais faute d'architecte CRM.
- 00-sommaire.md et collecte/liste-minimale.md disent que, chez celui qui vend seul, le harnais crée 06-mots-interdits.md à l'installation s'il nomme des mots refusés, et la liste dit qu'avec le harnais on ne répond qu'aux demandes qu'il pose, pour le seul type de client principal.
- 03-parcours-client.md dit que le premier jet des étapes part des étapes écrites dans crm/config.json, et qu'une étape renommée change aux deux endroits à la fois, comme la section 2 bis de l'installation.
- 00-sommaire.md et 01-offre-et-pitchs.md disent, comme harnais/CLAUDE.md, que chez celui qui vend seul le constat s'écrit quand même dans personnel/constats-a-remonter.md, que le harnais lui propose tout de suite de changer son OS sur son go, et que la colonne « Reporté le » prend alors la date du jour.
- crm/config.json, note des mots interdits : dans l'édition solo, 06-mots-interdits.md n'existe que si le commercial a nommé des mots refusés à l'installation ; aucune clé ne change.
- 11-crm.md, section « Selon l'outil », dit que celui qui vend seul n'a pas de socle à poser : le harnais relève ce que son CRM a déjà, et il crée lui-même dans son outil un pipeline ou un champ de plus ; la grille SPICED ne cite plus le CRM interne de LABK, et la promesse de proposer un vrai CRM devient le constat neutre que le registre s'y reprend tel quel.
- spiced-reference/LISEZ-MOI.md définit le S par l'organisation et les outils du client et non par la cible, compte la règle de pivot dans le minimum pour démarrer, et s'adresse au lecteur par « vous » d'un bout à l'autre ; _modele.md corrige l'accord « qui les nourrissent ».
- collecte/liste-minimale.md dit que les réponses de celui qui répond seul s'écrivent dans ses dossiers et ne passent que par son outil d'IA (CONFIDENTIALITE.md du harnais), au lieu de « tout reste dans vos dossiers ».
- 03-parcours-client.md dit que les motifs de refus reçoivent dès l'installation les réponses aux demandes 16 et 18 ; 02-icp.md rend à l'édition entreprise le diagnostic et l'analyse des affaires gagnées parmi ses sources ; 04-battle-cards.md dit qu'une fiche peut commencer dès l'installation si la réponse à la demande 18 nomme un concurrent.
- 00-sommaire.md, section « Quand un fichier d'équipe manque », s'adresse au lecteur par « vous » dans la puce des constats du terrain, comme les autres puces.
- 11-crm.md dit, comme la section 0 de la skill installation, que dans une équipe sans CRM le registre sert une fois que la personne autorisée a écrit dans 11-crm.md et crm/config.json les lignes que le harnais lui a préparées dans un constat, le harnais copiant ensuite le registre sur le go du commercial. La dernière phrase de la section « Sans CRM : le registre » donne la même raison que le LISEZ-MOI.md du registre : il se reprend tel quel dans un CRM, parce que chaque colonne correspond à un champ du CRM (ligne réécrite à la fusion avec la version de 16:33).
- Fusion du polissage avec la version de 16:33 (décision de Laurent du 23/11/2026) : le gabarit de l'OS part de la version de 16:33 et adopte son registre, défini dans harnais/gabarits/registre/LISEZ-MOI.md. 11-crm.md, section « Sans CRM : le registre », le présente une fois comme deux fichiers de tableur, dit qu'il ne sert jamais à côté du CRM d'une équipe, et ne promet plus de proposer un CRM dès que les contacts se comptent par dizaines (à confirmer par Laurent) ; la ligne « CRM » s'écrit « aucun, registre ../registre/ ». crm/config.json, sans aucune clé renommée ni retirée, dit dans sa note de tête que sans CRM l'installation écrit null dans serveur_mcp et que les autres clés ne changent pas, le harnais lisant les colonnes du registre et les étapes en mots simples de 03-parcours-client.md, qui le dit aussi. 00-sommaire.md et collecte/liste-minimale.md disent « le registre » ; spiced-reference/LISEZ-MOI.md renvoie à l'exemple fictif de 16:33.
- 11-crm.md, section « Les champs obligatoires par fiche », à la fusion : sans CRM, chaque ligne de `contacts.csv` porte au moins `entreprise`, `personne` et `etape`, l'étape disant si c'est un suspect ou une affaire ; la colonne type de l'ancien tableur n'y est plus. 03-parcours-client.md dit que le délai de silence par étape se reporte dans `crm/config.json`, et place la phrase « Sans CRM » après lui.

Ce qui change pour l'existant : un OS déjà rempli en v0.4 garde tout son contenu. La personne autorisée complète le sommaire (qui fait quoi, l'édition, l'endroit où vit l'OS), ajoute le fichier `collecte/liste-minimale.md`, et renomme dans `crm/config.json` les deux clés `objet_prospect` et `etapes_prospect` (aucune skill ne les lit encore, rien ne casse si elle tarde).

## v0.4 (22 et 23/11/2026)

Nouveau fichier `12-routines.md` (23/11/2026) : les quatre routines de la méthode (point du matin, point des réactivations, animation de la Maturation, veille des signaux), au statut Proposée, et la place des routines propres à l'entreprise. Le CRM fait foi quand il porte l'objet Routine du socle CRM ; sinon, le harnais lit ce fichier.

Aucun workflow ne tourne dans le CRM (décision du consultant du 23/11/2026) : `11-crm.md` le pose comme règle immuable et dit que l'architecte CRM remplit ce fichier et `crm/config.json` à la fin de la pose. `crm/config.json` gagne les clés qui disent au harnais où écrire quand il fait ce travail (étapes gagné et perdu du suspect, motifs de silence et de jamais contacté, origine, propriétaire, date d'entrée dans l'étape).

La méthode LABK (placement sur preuve, douleur et impact, événement critique, ACRAC, reviews) entre dans la base du harnais v0.6, dossier `methode/`, et non dans l'OS : le gabarit de l'OS n'est copié qu'une fois chez le client, alors que la méthode doit suivre les versions de LABK. Le sommaire le dit.

`11-crm.md` porte la grille SPICED à installer par l'architecte CRM (une liste de quatre valeurs par lettre, avec leurs définitions), les deux faces de l'impact, le repli quand le CRM n'a pas de champ, et la convention des montants hors taxe. Le modèle du SPICED de référence reprend la méthode complète : le verdict, la chaîne des trois questions par douleur, la répartition par interlocuteur, les deux faces de l'impact, le compte des entreprises et la règle de pivot. `06-mots-interdits.md` précise qu'il vise les messages au client et non les notes internes, et devient la seule liste des mots interdits (la clé `vocabulaire.interdits` sort de `crm/config.json`). `crm/config.json` accepte un délai de silence par étape. Il gagne aussi le seuil `jours_avant_cloture_consigne` (dix jours), lu par la boucle d'apprentissage du harnais. Les délais y sont présentés comme des hypothèses de départ, réglables par segment ICP (`qualification_perimee_jours_par_segment`, `jours_avant_statut_par_segment`).

Le parcours client reçoit, repris des gabarits des parcours cadrés de la méthode LABK, le cadrage et la conversation de chaque étape (ce que le commercial annonce, ce qu'il désamorce, la phrase de cadrage, ce qu'il cherche à savoir, ce qu'il apporte) et les familles de nurturing (les motifs, le type de contenu, le rythme, ce qui fait revenir l'affaire, la sortie).

Dans `crm/config.json`, les clés `champs_bloquants_avant_avancement` et `champs_bloquants_avant_sortie_maturation` deviennent `lettres_a_verifier_avant_avancement` et `lettres_a_verifier_avant_sortie_maturation` : le harnais signale ces lettres, il ne bloque rien.

Le parcours client reçoit une section « L'échéance de décision » : la date de référence de l'entreprise (ou son absence), les délais de préparation pour le calcul à rebours, et les options si elle en pose. `11-crm.md` ne garde plus que les libellés courts de la grille SPICED et renvoie à `methode/grille-spiced.md` de la base du harnais pour les définitions, pour n'avoir qu'une source.

La grille des contreparties définit le « oui sur le fond ».

Le parcours client demande une ligne pour chaque étape, négociation et signature comprises, et la preuve qui fait passer une affaire en gagné.

Ce qui change pour l'existant : rien, aucun client n'a encore reçu de version.

## v0.3 (22/11/2026)

Le CE de `crm/config.json` désigne désormais l'événement critique du SPICED, et non plus la conséquence économique : les champs de qualification sont `situation`, `douleur`, `impact`, `evenement_critique` et `decision`, et l'événement critique remplace la conséquence économique parmi les champs bloquants. Le mode d'emploi de `crm/config.json` est réécrit, et les mots « lead » et « opportunité » du vocabulaire deviennent « prospect » et « affaire ». Le parcours client définit en tête les trois mots suspect, prospect et client, et précise qu'un clic ou une ouverture de mail n'est pas un signe d'intérêt. `08-autorisations.md` dit à qui reviennent les reviews de coaching, et le sommaire dit où se trouve le brief de voix de l'entreprise.

Ce qui change pour l'existant : rien, aucun client n'a encore reçu de version.

## v0.2 (21/11/2026)

Ajout de `11-crm.md` (l'outil, les champs obligatoires, les règles d'usage, la règle de contact d'un collègue) et de `crm/config.json` (les noms techniques que lit le harnais), repris de la configuration du coach CRM de LABK.

Ce qui change pour l'existant : rien, aucun client n'a encore reçu de version.

## v0.1 (21/11/2026)

Création du dépôt, à partir du gabarit d'abord rangé dans le dépôt du harnais. Il contient le sommaire avec la charte et le journal des changements, un fichier par brique (offre et pitchs, ICP, parcours client, battle cards, grille des contreparties, mots interdits, ordre du point du matin, autorisations, objectifs), le modèle de SPICED de référence et le fichier des constats du terrain.
