# Prospecter

Cette méthode dit comment le commercial va chercher des conversations avec des entreprises qui ne le connaissent pas encore, quel que soit le canal. Elle sert à la skill `liste`, qui construit les listes, et à la skill `campagne`, qui conduit une campagne de bout en bout. Les réglages de l'entreprise (canaux, plafonds, créneaux, cadence) vivent dans `../os/13-prospection.md`, jamais ici.

## Les mots

Une campagne contacte des **suspects** : des entreprises dans la cible qui n'ont encore donné aucun signe d'intérêt. Un suspect devient un **prospect** au premier échange humain réel (une réponse sur le fond, un appel, une rencontre, un rendez-vous accepté), et c'est alors le coach CRM qui le suit, avec son affaire. Un prospect devient un **client** quand il signe. Un clic ou une ouverture ne fait jamais d'un suspect un prospect. Ces trois mots sont ceux du parcours client de l'OS (`../os/03-parcours-client.md`), ils sont immuables, et le harnais ne les mélange jamais.

Une campagne ne s'adresse donc qu'à des suspects. Un prospect est suivi dans son affaire par le coach CRM, et un client ne reçoit jamais un message de prospection : on lui parle dans le cadre de la relation qu'il a déjà avec l'entreprise.

## Le principe

La prospection ne sert pas à envoyer des messages. Elle sert à faire de suspects des prospects, c'est-à-dire à ouvrir des conversations avec la bonne personne, au bon moment, pour les bonnes raisons. Un message qui part vers la mauvaise personne ne coûte pas seulement un envoi : il use l'adresse, il use la réputation du commercial, et il remplit le portefeuille d'affaires qui ne signeront pas.

On mesure donc une campagne aux réponses qualifiées et aux rendez-vous qu'elle ouvre, jamais au nombre de messages partis, ni aux ouvertures, ni aux clics. Une réponse est qualifiée quand elle porte un cas nommé, une question sur l'offre ou une demande de rendez-vous. Un clic n'est qu'un signal : il peut dire qu'un humain s'intéresse, il ne dit jamais qu'une affaire existe.

## Le calcul à rebours

Avant de construire une liste, le harnais dit au commercial combien de suspects il faut toucher, en partant de ce qu'il veut obtenir. Le calcul se fait à rebours, en quatre lignes :

1. L'objectif : le nombre de rendez-vous ou d'affaires voulus sur la période, lu dans `../os/09-objectifs.md`, ou donné par le commercial.
2. Le taux de réponse qualifiée et le taux de rendez-vous par réponse, lus dans le bilan des campagnes précédentes. Sans historique, le harnais prend les valeurs de départ de `../os/13-prospection.md` et les marque comme des hypothèses à corriger au premier bilan.
3. Le nombre de suspects à toucher, qui en découle.
4. Le nombre de suspects par jour ouvré, qui en découle aussi, et qu'on compare tout de suite au plafond par adresse et au temps que le commercial peut donner aux réponses.

Le harnais dit le résultat en une phrase, par exemple : « Pour 6 rendez-vous d'ici le 31/01, au taux observé sur vos deux dernières campagnes, il faut toucher environ 300 entreprises, soit 15 par jour ouvré. » Si le chiffre dépasse ce que le commercial peut traiter, il le dit avant de construire quoi que ce soit, parce que c'est souvent là qu'un objectif se révèle irréaliste. Sans objectif, il ne compare à aucune cible : il mesure le rythme observé et le dit.

## Le verrou : ce qui est posé avant d'écrire

Aucun message n'est écrit avant que le message noyau et l'offre soient posés. Sans preuve, la campagne peut démarrer, mais le message ne promet rien. C'est la règle qui a le plus servi : elle empêche d'écrire des messages brillants sur une offre qui n'existe pas encore.

Le harnais pose avec le commercial les sept cases qui suivent. Le message noyau, l'offre et la liste sont obligatoires ; une autre case vide se dit, et la campagne part en le sachant. Le harnais propose un premier jet de chacune à partir de l'OS (l'ICP, l'offre, le parcours client, le SPICED de référence), et le commercial corrige. Une case vide se dit, elle ne se remplit pas d'office.

1. **La personne qui reçoit le message**, et celle qui peut bloquer derrière elle. La seconde n'est jamais destinataire.
2. **Le message noyau** : une phrase qui dit le problème du client avec ses mots, et ce qui change pour lui. Pas une intention.
3. **Le signal daté** qui autorise le contact aujourd'hui : une loi, une échéance, une publication, une nomination, un recrutement. Jamais une impression. Sans signal, la raison de contacter est le problème du client, dit avec une scène qu'il reconnaît.
4. **La preuve** : au moins un résultat mesuré avant et après chez un client, avec son accord pour le citer. Un chiffre de marché ouvre une accroche, il ne remplace jamais une preuve client. Sans preuve, la campagne peut démarrer, mais elle le sait et le message ne promet rien.
5. **L'offre**, écrite comme un prospectus : ce que le client reçoit, le prix ou sa fourchette, le délai, et la porte de sortie.
6. **La liste** : le périmètre, le volume, les critères de tri, et la date où elle sera prête (skill `liste`).
7. **Le seuil de réussite** : combien de réponses qualifiées sur combien de suspects, et la date du bilan. Cette date est une décision du commercial, jamais un calcul tiré du stock.

S'y ajoute une huitième pièce, sans laquelle la campagne ne démarre pas : **la règle des réponses**, c'est-à-dire ce que le commercial fait de chaque type de réponse (`methode/lire-un-signal.md` donne la règle de départ, que la campagne peut préciser).

## La séquence

Une séquence est une suite de pas, chacun sur un canal, avec son délai. La méthode de départ, qui a servi deux fois, compte quatre mails espacés de plusieurs jours ouvrés. La cadence exacte est un réglage de la campagne, écrit dans sa fiche, avec la valeur par défaut de `../os/13-prospection.md`. Un pas LinkedIn, un appel ou une invitation à un événement peut prendre la place d'un mail.

Chaque pas obéit à quatre règles.

- **Un angle neuf.** Un pas n'est jamais une relance vide. Les angles qui ont marché : la scène vécue par le client, le signal daté, la continuité (« ce qui ne dépend plus d'une seule personne »), l'offre écrite avec son prix et sa sortie.
- **Une seule demande.** Chaque pas vise une réponse, ou la lecture d'un contenu qui mène à une réponse, et une seule chose à la fois.
- **Une sortie simple.** Chaque mail porte une phrase qui permet de ne plus être contacté, sans se justifier. Une demande d'arrêt vaut pour toutes les campagnes de l'entreprise.
- **Un texte unique ou presque.** La segmentation sert à choisir qui reçoit quel sujet, et le message ne change que là où la situation du client change vraiment (sa taille, sa façon d'acheter).

La séquence s'arrête pour un suspect dès qu'il répond, quoi qu'il réponde, dès qu'un humain de son entreprise s'engage ou refuse, et dès qu'un vrai clic demande au commercial de lui écrire personnellement (`methode/lire-un-signal.md`).

## Écrire un message

Un message de prospection se lit en dix secondes sur un téléphone. Il suit la voix de l'entreprise quand l'OS en donne une, et sinon ces règles.

- La première phrase parle du client, jamais de l'entreprise qui écrit.
- Le problème se dit avec une scène que le client reconnaît dans sa semaine, pas avec un concept.
- On n'écrit jamais par la peur : ni menace réglementaire, ni « vos chiffres sont faux ». Un calendrier légal n'est jamais figé, et la peur braque.
- On ne fait pas la leçon à quelqu'un qui connaît déjà son sujet.
- On ne vend jamais un outil de plus à gérer.
- On réduit la taille de la décision plutôt que de combattre la prudence : face à « il est urgent d'attendre », on propose un premier pas assez petit pour ne pas mériter d'attendre.
- Tout fait daté cité dans un message est revérifié le jour de l'envoi.
- Le nom de l'entreprise qui écrit arrive quand le lecteur a déjà compris de quoi on parle.

## Les canaux

Le harnais prépare de la même façon sur tous les canaux. Ce qui change, c'est qui fait partir le message.

| Canal | Ce que prépare le harnais | Qui fait partir |
|---|---|---|
| Mail | La séquence, les vagues de la semaine, chaque message en entier | Le relais réglé dans `../os/13-prospection.md` (la messagerie du commercial ou son outil d'envoi), sur le go du commercial. Sans relais, le commercial envoie lui-même |
| LinkedIn | La liste des profils à ouvrir, l'invitation et le message, prêts à coller | Toujours le commercial, parce que les conditions de LinkedIn interdisent qu'un outil agisse à sa place. Le harnais ne lit jamais LinkedIn |
| Téléphone | La liste d'appels du jour, la raison d'appeler chacun, une ouverture courte, les objections probables (`methode/objections-acrac.md`) | Le commercial, puis il raconte l'appel, que la captation traite |
| Événements | Les événements où la cible sera, les personnes à voir, puis la relance de chaque personne rencontrée | Le commercial |
| Réseau et prescripteurs | Qui peut recommander, le message de demande, le suivi de chaque recommandation | Le commercial |

Vers des particuliers, le téléphone et le mail demandent un consentement préalable : le harnais n'en prépare pas sans ce consentement. Entre entreprises, la prospection vers une adresse nominative est permise sans consentement préalable, à condition d'informer la personne et de lui laisser un moyen simple de s'opposer [hyp : repères de la CNIL, à faire vérifier pour chaque cas].

## Le temps long

Les suspects de la cible qui n'ont pas répondu, et ceux qui ont dit « pas maintenant », entrent dans le temps long. Ceux qui sont hors cible n'y entrent jamais. Une réactivation part sur un signal daté, porté par la date de réactivation de la fiche, jamais sur un compte à rebours arbitraire, et elle apporte toujours quelque chose de neuf. Le coach CRM tient ce temps long avec la veille des entreprises (skill `coach-crm`, sections 12 et 13).

## Le bilan et l'apprentissage

Chaque campagne se ferme par un bilan, à la date décidée au lancement. Le bilan compte les suspects touchés, les réponses par type, les réponses qualifiées, les rendez-vous et les affaires ouvertes, et il compare au seuil de réussite. Il dit aussi ce qui a marché et ce qui n'a pas marché : un angle qui fait répondre, une cible qui ne répond jamais, une cadence qui fait demander l'arrêt.

Ce que le bilan apprend s'écrit dans la fiche de la campagne et dans la trace du harnais. Une leçon qui ne sert qu'à une cible reste dans sa campagne. Une leçon qui a servi deux fois devient un constat qui remonte à LABK par le rapport, pour entrer dans cette méthode. On n'écrit jamais ici une règle spéculative : on extrait le générique après l'avoir prouvé.

*Version 0.1 du 27/11/2026, reprise de la méthode campagne de LABK (v1 du 28/07/2026, prouvée sur deux cibles) et du règlement de prospection de LABK (septembre à novembre 2026), sur la décision de Laurent du 27/11/2026.*
