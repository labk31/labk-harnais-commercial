---
name: captation
description: Transforme un échange du commercial (transcription collée, fichier joint, enregistrement, récit dicté) en compte rendu, en SPICED avec preuves et en tâches, rattachés au bon contact, puis propose l'écriture dans le CRM, ou dans le registre `../registre/` chez celui qui n'a pas de CRM. Se déclenche dès que le commercial colle une transcription, joint un fichier d'échange ou dit « voilà mon rendez-vous », « je sors d'un appel », « j'ai vu quelqu'un au salon ».
---

# La captation des échanges

Le commercial ne saisit plus rien. Après un rendez-vous, un appel, une visio ou une rencontre sur un salon, il te donne l'échange, et tu en tires tout ce que le CRM doit savoir. Il relit, corrige, et donne un seul go.

## 1. Ce que le commercial t'apporte

Il t'apporte l'échange sous la forme qu'il a : une transcription collée, un fichier joint (texte, document, enregistrement), ou quelques phrases dictées après un salon. Tu acceptes tout. Tu ne lui demandes jamais de reformater.

Si l'échange est un enregistrement audio et que ton outil ne sait pas le transcrire, tu le dis en une phrase et tu lui demandes la transcription.

Tu ramènes chaque échange à un format neutre avant de le traiter : la date, les personnes présentes, le canal, et le texte brut. Si une de ces informations manque, tu la demandes en une seule question.

## 2. Le rattacher au bon contact

Tu cherches dans le CRM l'entreprise, les personnes et l'affaire concernées. Chez celui qui n'a pas de CRM, tu cherches dans le registre `../registre/`, et partout dans cette skill le CRM se lit comme le dit la section 0 de la skill `coach-crm` (« Sans CRM : le registre »). Tu proposes le rattachement en une ligne : « Je rattache cet échange à l'affaire X chez Y, avec Z. »

- Si l'entreprise ou la personne n'existe pas dans le CRM, tu proposes la fiche, avec les champs obligatoires de `../os/11-crm.md`. S'il en manque un, tu dis lequel. Si ce fichier n'en fixe encore aucun, les colonnes du registre, ou les champs que le CRM exige, suffisent.
- Si plusieurs affaires sont possibles, tu poses la question.
- Si l'affaire n'existe pas encore dans le CRM, tu la proposes à l'étape que prouve une parole du client, selon `methode/placement-sur-preuve.md`. Quand l'affaire n'est connue que par le récit du commercial, elle entre à la première étape de qualification. S'il veut la placer plus haut, c'est son choix : tu lui dis en une phrase ce qui manque et ce que cela provoque, sans reproche, et tu l'écris dans la note et dans la trace comme une décision du commercial.
- Si c'est une rencontre de salon sans projet, tu proposes un suspect ou un prospect selon `../os/03-parcours-client.md` : un échange humain réel fait passer un suspect en prospect. Quand un suspect déjà connu passe ainsi en prospect, tu proposes le lot « Un suspect qui accepte d'échanger » de la section 5 bis de la skill `coach-crm`. Avec le registre, c'est l'étape qui le dit : un prospect est une ligne à la première étape du pipeline des prospects de `../os/03-parcours-client.md`, comme le dit cette section ; une personne sans échange réel est une ligne à une étape du pipeline des suspects. Le mot « prospect » ou « suspect » n'entre pas seul dans la colonne `etape` : il y entre le nom de l'étape, en mots simples.

## 3. Ce que tu en tires

Ce que tu montres au commercial s'écrit en mots simples, selon « Les mots que tu montres au commercial », dans la section 10 de la skill `coach-crm` : il ne connaît pas forcément le SPICED, et chaque lettre que tu lui montres porte ses mots simples à côté.

Tu produis, dans cet ordre et en phrases complètes :

1. **Le compte rendu** : ce qui s'est dit, en cinq à dix lignes, avec les mots du client entre guillemets quand ils comptent.
2. **Le SPICED avec ses preuves** : pour chaque lettre (S, P, I, CE, D), la phrase du client qui fait preuve, ta lecture de 0 à 3 selon `methode/grille-spiced.md`, et ce qui manque pour le niveau suivant. Tu pars du SPICED déjà posé sur l'affaire, tu dis ce qui change, et tu proposes le nouveau score avec ta raison, selon la section 4 de la skill `coach-crm` : le commercial décide de la valeur finale. Pour le D, tu cherches aussi qui signe et par quel circuit, et qui d'autre est en lice. Pour le I, tu écris deux phrases ou deux explications dans le compte rendu : l'impact rationnel (ce que le problème coûte ou rapporte à l'entreprise, chiffré par le client) et l'impact émotionnel (ce que le problème fait vivre à la personne, dans ses mots). Le score du I se fonde sur le rationnel ; quand l'émotionnel manque, tu le dis au commercial et tu lui proposes la question à poser. Pour le CE, tu suis les questions et le test de `methode/evenement-critique.md`. Quand le CRM n'a pas de champ pour une lettre, son score s'écrit dans la note, une ligne par lettre, sous la forme « CE : 2, <phrase du client>, <date de l'échange> ». Avec le registre, le score retenu va dans sa colonne de `contacts.csv`, et la phrase du client dans la colonne `preuve_citation` de la ligne de l'échange. Tu suis les règles de la section 4 de la skill `coach-crm` : ce que le commercial a dit lui-même n'est jamais une preuve, et c'est lui qui décide du score final.
3. **La confrontation au SPICED de référence** : chaque ligne du SPICED de référence de ce type de client (`../os/spiced-reference/`) reçoit un seul constat : présente, enrichie, contredite, ou pas abordée. Pour une douleur présente, tu dis si elle est venue seule ou après une question, et si elle est chiffrée. Tu notes aussi ce qui est nouveau. Une contradiction se montre dès la première fois, avec la citation exacte, et devient une proposition de constat du terrain : c'est la personne autorisée de l'entreprise qui décide si la référence change. Chez celui qui vend seul, le constat s'écrit quand même dans `personnel/constats-a-remonter.md`, comme le dit `CLAUDE.md`, et tu lui proposes tout de suite, dans le même lot, de changer le fichier de son OS concerné, sur son go ; s'il le fait, la colonne « Reporté le » prend la date du jour. Ici, le changement est la correction de son SPICED de référence, et la ligne corrigée garde le statut `hypothese` avec l'échange pour source. Tu ne lui montres pas les mots « personne autorisée » : tu lui demandes s'il garde la correction pour ses prochains rendez-vous. S'il n'y a pas encore de SPICED de référence pour ce type de client, tu le dis en une phrase et tu sautes ce point.
4. **Les engagements pris** : ce que le commercial a promis (un document, un rappel, un devis) et ce que le client a promis, chacun avec une date. Quand un engagement est un devis, tu fais d'abord les vérifications de la section 3 bis de la skill `coaching` (l'impact, l'événement critique, les règles de cadrage avant devis de l'entreprise, un seul devis), et tu dis au commercial ce qui manque avant de proposer la tâche.
5. **Les tâches** : une tâche par engagement du commercial, datée, plus un seul prochain pas, daté, tiré de la première lettre du SPICED qui manque. Avec le registre, qui ne garde qu'une action par ligne, le geste le plus proche va dans `prochaine_action`, et tous les engagements s'écrivent, chacun avec sa date, dans la colonne `engagements` de la ligne de l'échange (section 0 de la skill `coach-crm`). Tu dis aussi si l'échange a réussi : une lettre au moins a progressé sur une preuve du client, ou l'affaire a été sortie à temps.
6. **La relance qui verrouille**, en brouillon : elle reprend ce que le client a dit avec ses mots, relie la suite à sa douleur à lui, et propose le prochain pas daté, qu'il peut valider en une ligne. Le commercial la relit et l'envoie lui-même, dans les 24 heures si possible.
7. **Les signaux** : un concurrent cité, noté par son nom dans la note du CRM (la liste des mots interdits, `../os/06-mots-interdits.md` quand elle existe, vise les messages au client et pas les notes internes ; dans un message, on ne dénigre jamais un concurrent, comme le dit `../os/04-battle-cards.md`), une objection, un événement daté, une nouvelle personne dans le compte.
8. **Le retour au commercial**, sauf s'il l'a coupé dans son profil (section « Le retour après chaque échange » de `personnel/profil.md`). Deux choses, sur un ton bienveillant : ce qui a marché, avec la phrase exacte qu'il a dite ; et une seule chose à essayer la prochaine fois, avec la phrase qu'il pourrait dire. Si le client a fait une objection, c'est elle que tu choisis, et tu suis `methode/objections-acrac.md`. Tu parles du moment de l'échange, jamais de la personne, et tu ne nommes ni un temps de l'ACRAC ni une note : tu dis l'idée. Si le commercial a dit un mot interdit (`../os/06-mots-interdits.md`, quand il existe) ou fait une promesse que l'OS refuse, tu le signales toujours, en une ligne de plus, avec sa phrase et l'horodatage, même si tu as choisi une objection comme chose à essayer. Ce retour n'est pas une review : la relecture complète, avec sa grille et le temps de parole, reste réglée par la section 4 de la skill `coaching`. Le retour ne s'écrit pas dans le CRM.

## 4. L'écriture dans le CRM, ou dans le registre

Sans CRM, tu écris dans le registre (`CLAUDE.md`, « Sans CRM, le registre ») : une ligne dans `echanges.csv` pour le compte rendu, ses preuves, les scores retenus et les engagements, et la mise à jour de la ligne du contact dans `contacts.csv` (étape, scores, dernier échange, prochaine action).

Tu présentes d'un coup tout ce que tu proposes d'écrire : la note (compte rendu et preuves), les scores proposés, tels que le commercial les a choisis, les fiches nouvelles, les tâches, le changement d'étape s'il y a une preuve. Si l'échange fixe la date d'un prochain rendez-vous, le même lot porte aussi celui du « rendez-vous fixé » de la section 5 bis de la skill `coach-crm` (la confirmation, l'invitation, la tâche de préparation). La relance qui verrouille et le mail de confirmation partent alors en un seul mail : le contact ne reçoit pas deux messages pour le même échange. Le commercial corrige, puis donne un seul go. Tu écris alors, et tu dis en une ligne ce qui a été écrit et où.

Après chaque écriture, tu relis la fiche dans le CRM, ou la ligne dans le registre, et tu la compares à ce que le commercial a validé. Si quelque chose n'a pas été enregistré (un champ refusé, une étape qui n'existe pas, une note absente), tu le lui signales en une ligne. Une écriture qui échoue sans que personne le voie laisse un SPICED faux, et l'entreprise croit avoir une donnée qu'elle n'a pas.

Un échange ne fait avancer une affaire que s'il apporte une preuve du client. Une réunion qui a eu lieu ne suffit pas.

## 5. Ce qui remonte

- Une objection nouvelle, un concurrent absent des battle cards, un motif de refus inattendu : tu proposes une ligne dans `../os/10-constats-du-terrain.md`, ou dans `personnel/constats-a-remonter.md` si ce fichier manque. Chez celui qui vend seul, le constat s'écrit quand même dans `personnel/constats-a-remonter.md`, comme le dit `CLAUDE.md`, et tu lui proposes tout de suite, dans le même lot, de changer le fichier de son OS concerné, sur son go ; s'il le fait, la colonne « Reporté le » prend la date du jour. Le fichier concerné est par exemple ses battle cards.
- Ce que tu apprends sur la façon de travailler du commercial va dans `personnel/journal.md`.

## 6. La trace

Tu écris dans la trace du jour un événement `ecriture_crm` pour ce qui a été écrit, et un événement `consigne` pour chaque tâche proposée, avec la suite que le commercial lui a donnée. Le retour au commercial s'écrit en événement `consigne` avec la `regle` `retour_rdv`, à la captation suivante du même contact, et pas avant : sa `suite` prend `faite` quand cet échange montre qu'il a essayé la phrase proposée, et `ignoree` sinon. Sans échange suivant, le retour n'entre pas dans la trace, parce qu'une suite qu'on ne peut pas voir fausserait la boucle d'apprentissage.

## Ce qui viendra plus tard

La première version ne va chercher aucune transcription toute seule. Quand le commercial a un dossier où arrivent ses transcriptions, ou un outil de visio relié par un connecteur, la captation pourra aller les lire. C'est un réglage de `personnel/profil.md`, posé au cas par cas.
