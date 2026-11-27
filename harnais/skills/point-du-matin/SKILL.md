---
name: point-du-matin
description: Rend chaque matin ouvré au commercial une page courte qui dit à qui parler aujourd'hui, pourquoi maintenant, avec quel prétexte et quelle preuve, la plus utile en premier. Se déclenche sur « point du matin », « on commence », ou quand la routine du point du matin est active.
---

# Le point du matin

Le point du matin dit au commercial ce qui mérite son attention aujourd'hui, ce qui peut attendre, et ce qui manque pour décider. Il est court : quelques actions, la plus utile en premier. Le reste attend.

## 1. Ce que tu lis

1. `personnel/profil.md` : l'heure et les réglages du commercial. Le profil ne fixe jamais l'ordre de tri.
2. `../os/07-ordre-du-point-du-matin.md` : l'ordre de tri de l'entreprise. S'il est vide, ou s'il n'existe pas, ce qui est le cas chez celui qui vend seul, l'ordre LABK de la section 2 s'applique.
3. `personnel/regles-personnelles.md` : si le commercial a ajusté l'ordre pour lui, par une règle écrite et datée.
4. Le CRM, puis l'agenda et la boîte mail, en lecture seule, comme le dit la section 0 de la skill `coach-crm`. Sans CRM (`crm.serveur_mcp` à `null`), tu lis le registre `../registre/`, comme le dit `CLAUDE.md` (« Sans CRM, le registre ») : `contacts.csv`, et `echanges.csv`, dont la colonne `engagements` porte les promesses qui ne tiennent pas dans la prochaine action. Un engagement daté se traite comme une prochaine action datée. Si l'agenda ou la boîte mail n'est pas relié, tu fais le point avec ce qui l'est, et tu dis en une ligne, au bas de la page, ce que tu n'as pas pu lire.
5. `personnel/suivi.md` : les populations à couvrir et les surveillances en cours.
6. `personnel/constats-a-remonter.md` : les constats que l'OS n'a pas pu recevoir. Tant qu'une ligne n'a pas de date dans la colonne « Reporté le », tu la rappelles en une ligne au bas de la page, avec le nom de la personne autorisée à qui la transmettre. Chez celui qui vend seul, la personne autorisée, c'est lui : tu lui proposes de trancher : changer le fichier de son OS concerné, sur son go, ou écarter le constat. Dans « Reporté le », tu écris la date seule quand son OS a changé, et « écarté le AAAA-MM-JJ » quand il l'a écarté ; une case vide veut dire que le constat attend. Un constat qui touche la méthode LABK, et non son OS, ne se reporte pas dans l'OS : le rapport pour LABK le reprend (skill `rapport-labk`), et tu ne le rappelles pas le matin.

L'ordre qui s'applique se lit dans cet ordre : une règle personnelle écrite, sinon l'ordre de l'entreprise, sinon l'ordre LABK. Une préférence dite en passant et jamais inscrite comme règle ne change pas l'ordre. Même avec une règle personnelle, une date qui tombe dans les deux jours ouvrés (un vote, une option, une échéance) reste dans le bloc du jour : tu la signales en une ligne, à la place que lui donne sa règle.

## 2. L'ordre LABK, par défaut

1. **Ce qui a une date** : un événement critique qui approche, une échéance de contrat, un rendez-vous à préparer.
2. **Ce qui vient de bouger** : une réponse, un signal, une objection. Une réponse d'un interlocuteur sorti du silence passe en tête de page, avec un brouillon de réponse prêt.
3. **Ce qui est proche de la signature.**
4. **Ce qui se dégrade en silence**, selon les délais du parcours client.
5. **L'hygiène du CRM**, sauf si un manque bloque une action plus haute.

## 3. La page

Tu suis la section 2 de la skill `coach-crm` pour la forme : les réponses sorties du silence en tête, puis « à regarder aujourd'hui », puis « ce que vous n'avez pas à faire aujourd'hui », puis « ce qui manque pour décider », puis le pied de page sur le rythme.

Chaque ligne dit en une phrase : qui, pourquoi aujourd'hui, la preuve (la fiche et le champ du CRM, la ligne du registre et sa colonne, ou le mail avec son expéditeur et sa date), et le geste proposé. Une ligne sans preuve ne sort pas. La page s'écrit en mots simples, selon « Les mots que tu montres au commercial », dans la section 10 de la skill `coach-crm` : celui qui vient d'installer ne connaît pas forcément le SPICED.

**Le contrôle des rendez-vous.** Avant de remplir la page, tu croises les rendez-vous des `seuils.jours_rdv_a_controler` prochains jours (sept par défaut) entre l'agenda, la boîte mail et le CRM. Tu cherches cinq écarts : un rendez-vous promis dans un mail ou un compte rendu qui n'est pas dans l'agenda ; un rendez-vous de l'agenda avec un contact connu du CRM qui n'a ni note, ni tâche, ni affaire ; une confirmation jamais envoyée au contact ; une date du CRM qui ne correspond pas à celle de l'agenda ; une tâche de préparation absente ou en retard. Chaque écart devient une ligne du bloc, avec sa preuve (l'événement de l'agenda, le mail avec son expéditeur et sa date, la fiche du CRM) et le lot qui le répare, celui du « rendez-vous fixé » de la section 5 bis de la skill `coach-crm`. Un rendez-vous à préparer aujourd'hui ou demain est une date qui tombe dans les deux jours ouvrés : il entre toujours dans le bloc. Quand tout est en ordre, tu le dis en une ligne : « Les N rendez-vous de la semaine sont confirmés, dans l'agenda et dans le CRM. » La trace porte la règle `rendez_vous`.

Le bloc « à regarder aujourd'hui » se remplit en trois temps, toujours dans cet ordre :

1. **Ce qui ne peut pas attendre.** Une date qui tombe dans les deux jours ouvrés (un vote, une option, une échéance, un rendez-vous à préparer) entre toujours dans le bloc, quelle que soit la règle de tri. Elle prend la place que lui donne cette règle.
2. **Le reste, dans l'ordre de tri**, jusqu'au plafond : `seuils.dossiers_par_matin` dossiers du portefeuille (cinq par défaut), et jamais plus de dix lignes en tout. Un dossier peut prendre deux lignes, par exemple une réponse et la relance qui en découle.
3. **Ce qui ne tient pas.** Si les dates du premier temps dépassent à elles seules le plafond, elles restent toutes, et tu le dis en une ligne en tête du bloc. Les autres dossiers qui ne tiennent pas ne disparaissent pas : tu les nommes sur une seule ligne, sous le bloc, « reportés à demain », avec la raison en trois mots pour chacun. Le lendemain, ils passent devant les dossiers de même rang.

Ce plafond est le seul : la skill `coach-crm` y renvoie.

**Le bloc de la prospection.** Quand une campagne est en cours (skill `campagne`), la page porte, après le bloc « à regarder aujourd'hui », un bloc court sur la prospection, en quatre lignes au plus :

1. ce qui part aujourd'hui : la vague du jour (le nombre de messages, la campagne, l'objet), ou « rien ne part aujourd'hui » et pourquoi ;
2. ce qui est revenu depuis la veille : les réponses avec la personne, l'entreprise et ce qu'elles disent, les vrais clics, les rebonds, les arrêts, ou « rien » ;
3. les gestes manuels du jour : les profils LinkedIn à ouvrir, les appels à passer, avec chaque message prêt à coller ou chaque raison d'appeler ;
4. le stock, quand il passe sous le seuil d'alerte (skill `liste`, section 9).

Une réponse sur le fond d'un suspect ne reste pas dans ce bloc : elle passe en tête de la page, avec le lot du coach CRM qui ouvre l'affaire. Le bloc de la prospection ne compte pas dans le plafond des dossiers, et il ne répète jamais ce qu'il a déjà dit la veille.

Tu ne compares à aucun objectif tant que `../os/09-objectifs.md` n'en fixe pas, ou s'il n'existe pas, ce qui est le cas chez celui qui vend seul : tu mesures le rythme observé, sans inventer de cible.

## 3 bis. Quand le portefeuille est presque vide

Le premier matin, celui qui vient d'installer a souvent quelques lignes seulement dans son CRM ou son registre, sans historique, et parfois sans boîte mail reliée. La page doit quand même lui dire à qui parler aujourd'hui et pourquoi, et la règle « preuve ou silence » ne se relâche pas pour autant. Tu remplis le bloc avec ce qui existe, dans cet ordre :

1. **Chaque contact du portefeuille**, même sans date. La preuve est ce que porte sa fiche ou sa ligne : la date du dernier échange, une prochaine action vide ou passée, la première lettre du SPICED encore sous 2. Le pourquoi aujourd'hui en découle : sans prochaine action datée, un contact se perd sans que personne le décide. Par exemple : « Z, chez Y : aucune prochaine action après votre dernier échange du 20/11 (registre, colonne `prochaine_action` vide), et on ne sait pas encore ce qui lui fait mal. Proposez-lui un appel de quinze minutes cette semaine ? »
2. **Les échanges récents avec une personne absente du portefeuille**, quand la boîte mail ou l'agenda est relié : un mail ou un rendez-vous des `silence.jours_avant_statut` derniers jours. Tu proposes de l'ajouter, avec le mail ou l'événement comme preuve.
3. **Ce que tu ne sais pas**, en une ligne au bas de la page (section 1) : « Je ne lis pas votre boîte mail : je ne vois que les trois contacts de votre registre. »

Si le portefeuille est vide et que rien d'autre n'est relié, tu ne proposes aucun nom. Tu le dis en une phrase, et tu poses une seule question : « Avec qui avez-vous parlé de votre offre ces deux derniers mois ? » Chaque personne qu'il nomme entre, sur son go, dans son CRM ou son registre, à l'étape que sa parole prouve (`methode/placement-sur-preuve.md`), et le point du matin repart de là. Une entreprise n'entre jamais dans la page parce qu'elle ressemble à l'ICP : ressembler à la cible ne dit pas pourquoi lui parler aujourd'hui.

## 4. Ce que fait le commercial

Il répond ligne par ligne, d'un mot : fait, plus tard, non. Chaque réponse devient une suite dans la trace. « C'est fait » devient `faite`. « Je vais le faire », « je l'appelle cet après-midi » devient `acceptee` : c'est une intention, pas un geste, et la boucle d'apprentissage ne la compte pas comme une réussite. Le lendemain, tu reprends toutes les suites de la veille dans une liste à cocher, une ligne par geste, à laquelle il répond d'un mot par ligne (fait, plus tard, non). Cette liste ne compte pas dans tes deux questions de l'échange. Pour chaque ligne, tu écris une nouvelle ligne pour la même consigne, avec le même `consigne_id`, `consigne_du` à sa date d'origine et sa suite réelle (`faite`, `differee`, `refusee` ou `sans_objet`) ; c'est la dernière ligne d'une consigne qui compte. « Plus tard » devient `differee`, « non » devient `refusee`. Une consigne que les faits ont rendue inutile (le client a rappelé avant la relance, l'affaire s'est réglée autrement) devient `sans_objet` : ce n'est pas un refus. Une ligne que tu lui as montrée et à laquelle il n'a pas répondu devient `sans_reponse`. Une consigne dont le geste est prévu plus tard dans la journée ou un autre jour devient `differee`, pas `sans_reponse`. Une suite que tu n'as pas eu la place de lui demander ne reçoit pas de nouvelle ligne : tu la reprends le lendemain.

## 5. Quand une catégorie est toujours ignorée

Grâce à la trace, tu vois les actions faites et les actions ignorées. Si une catégorie est ignorée plusieurs matins de suite, tu le dis en une phrase et tu proposes de revoir l'ordre pour lui. Tu ne le changes jamais seul. S'il valide, l'ajustement va dans `personnel/regles-personnelles.md`.
