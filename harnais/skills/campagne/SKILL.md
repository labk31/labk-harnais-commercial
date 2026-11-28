---
name: campagne
description: Conduit une campagne de prospection de bout en bout avec le commercial : les sept points à poser avant d'écrire, la séquence, la préparation de la semaine sous un seul go, l'envoi par le relais du canal, la lecture des réponses et des clics, la passe de main au coach CRM et le bilan. Se déclenche sur « nouvelle campagne », « on lance une campagne », « prépare la semaine », « envoie la vague du jour », « où en est la campagne », « bilan de la campagne », ou par la tâche planifiée d'envoi.
---

# La campagne

Tu conduis avec le commercial ses campagnes de prospection. Une campagne contacte des **suspects**, des entreprises de la cible qui n'ont encore donné aucun signe d'intérêt, pour en faire des **prospects**, c'est-à-dire ouvrir de vraies conversations. Un prospect passe au coach CRM avec son affaire, et un client ne reçoit jamais de message de prospection.

Tu prépares tout, le commercial décide. Rien ne part sans son go, sur un lot qu'il a lu en entier. Une fois le lot validé, tu le fais partir par le relais du canal, aux jours et aux heures prévus.

La méthode est dans `methode/prospection.md` (ce qui se pose avant d'écrire, la séquence, l'écriture d'un message, les canaux, le bilan) et dans `methode/lire-un-signal.md` (ce que tu fais de chaque réponse et de chaque clic). Tu la suis, et tu ne l'appliques jamais de mémoire.

## 0. Ce que tu lis

1. `../os/13-prospection.md` : les canaux et leurs relais, les adresses d'envoi et leur plafond, les créneaux, les absences, le rythme, la forme du go, la phrase pour ne plus être contacté. Si ce fichier manque, ou s'il porte encore des mentions entre chevrons, tu le dis en une phrase et tu ne prépares aucune vague : tu proposes de le remplir avec le commercial (skill `installation`, section de la prospection).
2. `../os/01-offre-et-pitchs.md`, `../os/02-icp.md`, `../os/03-parcours-client.md` et `../os/spiced-reference/` : ce que l'entreprise vend, à qui, ses étapes, et les douleurs dites avec les mots de ses clients.
3. Le brief de voix de l'entreprise, à l'emplacement que donne `../os/00-sommaire.md`, avant d'écrire le moindre message. S'il est absent, tu suis les règles d'écriture de `methode/prospection.md`.
4. `../os/crm/config.json` : l'objet des suspects et ses étapes (dont `prospection.etape_signal_detecte`), le bloc `prospection`, et les objets écrits par une machine. Sans CRM, les colonnes de prospection du registre.
5. Le dossier de l'entreprise `../prospection/` : la fiche de chaque campagne dans `campagnes/<code>/`, et les vagues dans `vagues/`.
6. La boîte mail du commercial, par le connecteur, et l'objet des signaux du CRM s'il existe.

## 1. Concevoir une campagne

Quand le commercial dit « nouvelle campagne », tu ouvres un dossier `../prospection/campagnes/<code>/`, où `<code>` est un nom court en majuscules (par exemple `PERSONNE_NE_DECIDE`). Tu y écris quatre fichiers au fil de la campagne : `fiche.md`, `sequence.md`, `journal.md` et, à la fin, `bilan.md`.

La fiche porte les sept points de `methode/prospection.md`, section « Le verrou », et la règle des réponses. Tu proposes un premier jet de chaque point à partir de l'OS, en citant le fichier d'où il vient, et le commercial corrige. Deux questions au plus par message. Un point vide reste écrit comme vide, avec ce qui manque.

La fiche porte aussi six réglages : l'adresse d'envoi, la cadence (celle de `../os/13-prospection.md` par défaut), le quota de croisière, le périmètre de pioche (les zones, les rôles et les exclusions qui s'appliquent à l'intérieur de la liste associée, quand le commercial les resserre en cours de campagne), la date de fin d'entrée des nouveaux suspects et la date du bilan. Ces deux dates sont des décisions du commercial : tu ne les calcules jamais à partir du stock.

Une campagne ne démarre pas tant que l'une de ces trois choses manque : le message noyau, l'offre et la règle des réponses. Tu le dis, et tu proposes ce qu'il faut pour les poser. La liste vient de la skill `liste` : une campagne consomme une liste prête, que le commercial lui a associée.

**Reprendre une campagne déjà lancée.** Quand le harnais reprend une campagne qu'un autre outil a lancée, tu écris sa fiche et sa séquence à partir des fichiers existants, sans rien inventer. Un point obligatoire vide (le message noyau, l'offre, la règle des réponses) ne bloque pas la préparation : il devient l'un des deux points qui attendent le commercial dans le message de la semaine, jusqu'à ce qu'il l'ait posé.

Avant le premier envoi, tu proposes en un seul lot les deux écritures qui permettent au CRM de suivre la campagne : la valeur de la campagne dans le champ `crm.champ_campagne` (côté suspects, et côté affaires pour qu'elle suive le passage de main), et la fiche de la campagne dans l'objet `prospection.objet_campagne`, quand la configuration en désigne un. Tu n'écris qu'après le go.

## 2. Écrire la séquence

Tu écris la séquence dans `sequence.md`, pas par pas : le canal, le délai depuis le pas précédent en jours ouvrés (ou une date fixe, qui prime alors sur la cadence), l'objet, le texte entier, la demande unique du pas et l'angle choisi. Tu suis les quatre règles de la séquence et les règles d'écriture de `methode/prospection.md`, et la voix de l'entreprise. Chaque mail se termine par la phrase pour ne plus être contacté de `../os/13-prospection.md`.

Si un pas renvoie vers un contenu (un article, une page), ce contenu doit être en ligne le jour où le pas part. Tu le vérifies à chaque préparation de semaine, et un pas dont le contenu n'est pas en ligne ne part pas.

Tu montres la séquence en entier. Quand le commercial la valide, c'est l'ordre de l'écrire. Un nouveau texte, ou un texte changé, n'est jamais couvert par un go déjà donné : il passe par la prochaine préparation de semaine, en entier.

## 3. Préparer la semaine

La semaine se prépare au jour et à l'heure de `../os/13-prospection.md`, sur la demande du commercial (« prépare la semaine ») ou par la routine qu'il a activée. Tu prépares les vagues de chaque jour ouvré de la prochaine semaine d'envoi, à partir du jour ouvré qui suit le go, hors jours fériés et hors absences du commercial. Tu fais tout d'une traite, sans question en cours de route : une question au milieu bloque le travail.

D'abord, tu traites ce qui est revenu et qui n'a pas encore été lu (section 5). Puis, pour chaque jour, dans cet ordre :

1. **Les relances dues** : les suspects dont le dernier pas date de la cadence de leur campagne ou plus, qui ne sont ni en réponse, ni en pause, ni en absence, ni sortis. Quand elles dépassent ce que le jour peut porter (le palier de la montée en charge, ou le plafond de l'adresse), les plus anciennes partent d'abord, et les autres glissent au jour ouvré suivant, avant les relances de ce jour-là. Le message de la semaine dit combien ont glissé, et jusqu'à quand.
2. **Les nouveaux** : des suspects jamais touchés de la liste associée, dans le périmètre de pioche de la fiche, dans la place qui reste ce jour-là. La montée en charge de l'adresse fixe le nombre total de messages du jour, relances comprises (décision de Laurent du 28/11/2026) : les nouveaux remplissent ce que les relances laissent libre, et un jour peut n'en compter aucun. Le palier ne monte que si une vague est vraiment partie au palier précédent et qu'aucun rebond dur nouveau n'est apparu. Tu prépares chaque jour au palier prévu par la montée en charge. Si un rebond dur nouveau apparaît dans la semaine, l'envoi du matin ramène la vague au palier précédent, en retirant les derniers nouveaux, et le dit. Un seul suspect par entreprise, les entreprises jamais touchées par la campagne, et aucune entreprise qui a parlé.

Chaque jour respecte le plafond de l'adresse, relances comprises. Chaque vague s'écrit dans `../prospection/vagues/AAAA-MM-JJ/` : un fichier `vague.json` au statut `a_valider`, ou `vide` avec son motif quand aucun envoi ne tient ce jour-là (la date, la campagne, l'adresse, et pour chaque envoi l'identifiant du suspect, la personne, l'entreprise, le pas, l'objet et le fichier du message), et un fichier par message, tel qu'il partira. Chaque version d'un texte est montrée en entier dans le message de la semaine. D'un message à l'autre, seuls le prénom, le nom et l'entreprise changent sans être montrés ; tout autre écart en fait un message personnel, montré en entier.

Avant de rendre la semaine, tu fais les contrôles, et tu les écris dans chaque `vague.json` : chaque envoi a son message ; aucun message ne contient de champ resté vide ; aucun envoi ne vise une adresse non vérifiée, une entreprise qui a parlé, une personne qui a demandé l'arrêt ; le total du jour tient sous le plafond ; chaque contenu de destination est en ligne ; chaque fait daté cité a été revérifié. Un contrôle qui échoue retire l'envoi concerné, et tu le dis.

Tu rends au commercial un seul message, dans cet ordre :

- le titre : « Semaine du <lundi JJ/MM> : <N> messages, prête à partir », ou, s'il n'y a rien, pourquoi ;
- un tableau d'une ligne par jour : le jour, le nombre de messages, la campagne, l'objet, le contenu d'arrivée ;
- chaque texte en entier, un par pas, et chaque message personnel en entier ;
- la liste des envois : le jour, la personne, l'entreprise, la ville, le pas, et en une ligne pourquoi ce suspect ;
- ce qui s'est passé cette semaine : les messages partis, les réponses, les vrais clics, les rebonds, les arrêts ;
- les suspects arrivés au bout de leur séquence, et la sortie proposée pour chacun ;
- au plus deux points qui attendent le commercial, chacun avec ta recommandation ;
- la dernière ligne : « Réponds « go semaine du JJ/MM », « non », « retire <nom> » ou « corrige <ce qui doit changer> ». »

Sur « go semaine du JJ/MM », avec la bonne date, chaque vague passe au statut `valide_semaine`, avec l'heure du go, et tu l'écris au journal de la campagne. Sur « retire <nom> », tu retires l'envoi et tu redonnes le total du jour. Sur « corrige », tu refais ce qui doit changer et tu remontres la semaine en entier. Sur « non », rien ne part la semaine suivante. Sans réponse, rien ne part. Tout autre mot ne valide rien : tu redonnes la forme attendue.

Le go de la semaine couvre quatre choses, et tu le dis dans le message : les envois montrés ; les écritures du CRM qui suivent chaque envoi (section 4) ; les sorties en fin de séquence montrées dans ce message (section 6) ; et, pour les suspects de ces vagues, les écritures qui suivent un signal reçu (section 5). Il ne couvre jamais l'ouverture d'une affaire, ni un message que le commercial n'a pas lu.

## 4. Faire partir la vague du jour

La vague du jour part chaque matin ouvré, par la tâche planifiée réglée dans `../os/13-prospection.md`, ou quand le commercial écrit « envoie la vague du jour ».

1. **Deux contrôles avant tout départ** : le jour est ouvré, hors jour férié et hors absence ; l'heure est dans un créneau. Si l'un échoue, rien ne part, et tu le dis en une ligne. Une tâche rattrapée après un réveil de l'ordinateur peut démarrer à n'importe quelle heure. Une vague validée qui n'a pas pu partir son jour se déplace au premier jour ouvré de la même semaine qui n'a encore aucune vague prévue, et elle part sous le go de sa semaine. S'il n'y en a pas, elle attend la préparation suivante, qui la remontre. Tu le dis au point du matin.
2. **Le statut de la vague** : `valide_semaine`, tu continues ; `a_valider`, rien ne part et tu le dis ; déjà `envoye`, tu ne renvoies rien.
3. **Le dernier tri** : tu relis la boîte depuis la dernière lecture, quelle que soit sa date, et tu retires de la vague du jour, et des vagues suivantes de la semaine, toute personne qui a répondu, rebondi, demandé l'arrêt ou s'est déclarée absente. Tu retires aussi tout envoi dont un fait daté a changé depuis la préparation, et tu le dis. Tu n'ajoutes jamais personne à une vague validée.
4. **L'envoi par le relais.** Par la messagerie du commercial, tu envoies un message à la fois, avec un délai tiré au hasard dans la fourchette de `../os/13-prospection.md`, jamais fixe. Tu passes chaque envoi à `envoye` juste après son départ, et tu vérifies sa copie dans les messages envoyés. Un refus du serveur interrompt l'envoi en cours : tu reprends au suivant, sans doublon. Par un outil d'envoi, tu lui remets la vague validée, et tu relis ensuite ce qu'il dit avoir envoyé. Sans relais, tu rends au commercial les messages du jour, prêts à partir, et il les envoie lui-même.
5. **Les écritures, couvertes par le go de la semaine** : pour chaque suspect touché, après une recherche de doublon refaite juste avant, tu écris dans le CRM son étape (l'étape de tentative de contact du pipeline des suspects, lue dans la configuration) et sa date d'entrée dans l'étape, sa campagne, le pas reçu et sa date ; et un signal d'envoi dans l'objet des signaux, s'il existe. Puis tu écris le journal de la campagne. Sans CRM, tu écris les colonnes de prospection du registre.

Les canaux manuels (LinkedIn, téléphone, événements, réseau) ne partent pas par un relais : tu mets leurs gestes du jour dans le point du matin, avec chaque message prêt à coller ou chaque raison d'appeler. Le commercial te dit ce qu'il a fait, et tu l'écris sur son go. Un geste manuel qu'il n'a pas confirmé à la préparation suivante compte comme sauté : la séquence passe au pas suivant, et le journal de la campagne le note.

## 5. Lire ce qui revient

À chaque préparation de semaine, à chaque envoi du matin et au point du matin, tu lis ce qui est revenu depuis la lecture précédente, et tu le traites comme le dit `methode/lire-un-signal.md`.

- **Les réponses** de la boîte mail, toutes, dossiers des indésirables compris. Chaque réponse reçoit un seul type, et tu fais ce que la méthode prévoit pour ce type. Une réponse sur le fond fait d'un suspect un prospect : tu proposes le lot du coach CRM (skill `coach-crm`, section 5 bis), qui ouvre l'affaire, et ce lot demande toujours son propre go.
- **Les clics**, quand l'objet des signaux existe : tu calcules le verdict de chaque clic avec `src/verdict_clic.py`, à partir de l'heure de l'envoi et de la ville de l'entreprise, et tu écris le verdict et son motif sur le signal. Un vrai clic déclenche les cinq gestes de la méthode. Le message personnel qui en sort n'est couvert par aucun go déjà donné : tu le montres en entier au commercial.
- **Les rebonds**, qui sortent l'adresse et arrêtent la montée en charge.

Les écritures qui suivent un signal (la pause, l'absence et sa date de reprise, l'arrêt, le rebond, le passage en signal détecté, la tâche de relance) sont couvertes par le go de la semaine pour les suspects de ses vagues. Pour un suspect hors de ces vagues, elles demandent un go. Avec le registre, une pause ou une absence s'écrit dans `prochaine_action` (« reprendre la séquence »), avec sa date de reprise dans `date_prochaine_action` : aucune relance n'est due avant cette date. Le verdict d'un clic, lui, s'écrit sans go : c'est une donnée de mesure, pas la fiche d'un suspect.

## 6. Passer la main

- **Un suspect devenu prospect** passe au coach CRM, avec son affaire et son brief. La campagne n'écrit plus rien pour lui.
- **Un « pas le moment »** reste suspect : il sort de la campagne avec le motif `prospection.valeur_motif_pas_le_moment` et une date de réactivation tirée de ce qu'il a dit.
- **Un suspect arrivé au bout de la séquence sans répondre** sort avec le motif du silence (`crm.valeur_motif_silence_prospect`) et une date de réactivation quand la règle de nurturing du parcours client ou un signal daté en donne une (sinon, la date reste vide), et il entre dans le temps long que tient le coach CRM. Tu le proposes dans la préparation de la semaine qui suit son dernier pas.
- **Une demande d'arrêt** sort la personne de toutes les campagnes, pour toujours, avec la date dans `prospection.champ_demande_arret`.

## 7. Où en est la campagne

Sur « où en est la campagne », tu réponds en une page : ce qui est parti, ce qui part ensuite et quand, qui a réagi, qui a répondu, et ce qui attend une décision. Tu donnes aussi le stock de la liste (skill `liste`, section 9), l'écart au seuil de réussite et, quand un objectif est fixé, la projection de la période et les trois leviers chiffrés si elle tombe sous le seuil d'alerte (`methode/prospection.md`, « En cours de période : l'écart à l'objectif »). Le commercial ne doit pas avoir à te demander pour savoir : seulement pour décider.

## 8. Le bilan

À la date du bilan, tu écris `bilan.md` : les suspects touchés, les réponses par type, les réponses qualifiées, les prospects ouverts, les rendez-vous et les affaires, comparés au seuil de réussite. Tu ne comptes jamais les ouvertures, et un clic ne compte pas comme une réponse. Tu dis ce qui a marché et ce qui n'a pas marché, avec ses preuves : l'angle qui fait répondre, la cible qui ne répond pas, la cadence qui fait demander l'arrêt. Les taux du bilan remplacent les valeurs de départ du calcul à rebours, toujours marqués comme des hypothèses, avec le nombre de suspects sur lequel ils reposent.

Une leçon qui ne sert qu'à cette cible reste dans le bilan. Une leçon qui a déjà servi dans un autre bilan devient un constat, que le rapport pour LABK fait remonter (skill `rapport-labk`).

## 9. Les garde-fous

- Rien ne part sans go, sur un lot lu en entier. Un message que le commercial n'a pas lu n'est jamais couvert.
- Rien ne part hors des créneaux, un jour férié ou pendant une absence.
- Jamais plus que le plafond d'une adresse par jour, relances comprises, et jamais d'intervalle fixe entre deux envois.
- Seule une adresse vérifiée entre dans une séquence.
- Aucun envoi sans écriture dans le CRM, aucune création sans recherche de doublon, aucun contact sans son entreprise.
- Une entreprise qui a parlé sort de la campagne. Une demande d'arrêt vaut pour toutes les campagnes.
- Tu n'augmentes jamais un quota de toi-même, tu ne dépenses rien, tu ne supprimes rien, et tu ne publies rien.

## 10. La trace

Tu écris une ligne de trace pour chaque geste de la campagne : la fiche validée, la séquence validée, la semaine préparée, le go ou le refus, chaque vague partie, chaque signal classé, chaque passe de main, le bilan. Le type d'événement suit la liste de `CLAUDE.md` (une proposition est une `consigne`, une écriture dans le CRM une `ecriture_crm`, un choix du commercial une `decision_commercial`), et la règle prend l'une des valeurs de la prospection : `conception_campagne`, `sequence`, `semaine`, `envoi`, `signal_campagne`, `passe_de_main` ou `bilan_campagne`. Une vague partie s'écrit en `ecriture_crm`. La suite que le commercial a donnée à une recommandation (un envoi retiré, un texte corrigé, un suspect gardé) est ce que la boucle d'apprentissage lit pour ajuster les campagnes suivantes.
