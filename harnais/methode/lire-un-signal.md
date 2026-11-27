# Lire ce qui revient d'une campagne

Cette méthode dit ce que le harnais fait de chaque signal qui revient d'une campagne : une réponse, un clic, un rebond. Elle sert à la skill `campagne`, au coach CRM quand il lit la boîte mail, et au point du matin. Une campagne peut préciser cette règle dans sa fiche ; sans précision, c'est celle-ci qui s'applique.

## Les mots

Le harnais emploie les mots du parcours client de l'OS (`../os/03-parcours-client.md`). Un **suspect** est une entreprise dans la cible qui n'a encore donné aucun signe d'intérêt : c'est elle qu'on contacte en campagne. Un **prospect** est une entreprise qui a donné un signe d'intérêt, c'est-à-dire un échange humain réel : une réponse sur le fond, un appel, une rencontre ou un rendez-vous accepté. Un **client** est une entreprise qui a signé : un prospect devient client à la signature. Un clic ou une ouverture ne suffit jamais à faire d'un suspect un prospect.

## Le principe

Une réponse est un fait : une personne a écrit. Un clic est un indice : quelqu'un, ou quelque chose, a suivi un lien. Le harnais ne confond jamais les deux. Une réponse change toujours quelque chose pour le suspect. Un clic ne change rien tant qu'il n'est pas jugé humain, et même alors il ne prouve pas qu'une affaire existe.

Le harnais ne mesure pas les ouvertures. Elles ne disent plus rien de fiable, parce que certaines messageries ouvrent les mails à la place des gens.

## Les réponses

Chaque réponse reçue est classée dans un seul type. Le classement s'écrit dans le CRM (ou le registre) à la passe qui la lit, et le harnais le montre au commercial au point du matin suivant.

| Type | À quoi on le reconnaît | Ce que fait le harnais |
|---|---|---|
| Sur le fond | La personne parle de son problème, pose une question sur l'offre, accepte un échange ou prend rendez-vous | Il arrête la séquence, il le met en tête du point du matin, et il prépare la réponse. C'est le premier signal humain d'intérêt : le suspect devient un prospect, et le coach CRM propose d'ouvrir l'affaire (section 5 bis) |
| Pas le moment | La personne dit que ce n'est pas le bon moment, sans fermer la porte | Il arrête la séquence. Le suspect reste un suspect, sorti avec le motif « pas le bon moment » et une date de réactivation tirée de ce qu'il a dit, et il entre dans le temps long |
| Absence | Un message automatique d'absence | Il met la séquence en pause jusqu'au lendemain du retour annoncé. Il propose de noter le téléphone de la signature. Si le message nomme une autre personne, il propose de l'ajouter, rattachée à l'entreprise, après une recherche de doublon |
| Arrêt | La personne demande à ne plus être contactée, quels que soient ses mots | Il la sort de toutes les campagnes, tout de suite, et pour toujours. Il ne lui répond pas pour argumenter |
| Rebond | L'adresse n'existe pas ou le serveur refuse le message | Il sort l'adresse de la séquence, son statut passe à `manquant`, et l'entreprise redevient à trouver. Un rebond dur nouveau arrête la montée en charge de l'adresse d'envoi, et le journal de la campagne le note |
| Filtre | Une réponse automatique d'un filtre ou d'un accusé de réception | Il la note et ne change rien |
| Filtre à valider | Un filtre anti-spam retient le message et demande à l'expéditeur de se faire connaître, par un lien à cliquer | Il met la séquence en pause pour ce suspect, montre le lien au commercial et lui demande s'il l'a traité. Quand il l'a traité, la séquence reprend, sans renvoyer le pas retenu |

Une réponse sur le fond ou un refus d'une personne fait sortir toute son entreprise des campagnes (`methode/sources-et-listes.md`, « Une entreprise qui a parlé »).

Une réponse que le harnais ne sait pas classer reste non classée, et il la montre au commercial avec sa question. Il ne devine pas.

## Les clics

Un clic n'a de sens que si le lien est suivi : cela suppose que l'entreprise ait un outil de suivi des liens, réglé dans `../os/13-prospection.md`. Sans outil de suivi, cette partie ne s'applique pas, et le harnais travaille sur les réponses seules.

Chaque clic reçoit un verdict, parmi quatre : **machine**, **à confirmer**, **humain probable**, **humain très probable**. Le verdict se calcule sur sept indices, dont les valeurs sont des réglages de l'entreprise :

1. **Le lien piège.** Chaque message peut porter un lien invisible pour un humain. Un clic sur ce lien est une machine, ainsi que tous les clics de la même adresse dans la minute.
2. **Le délai.** Un clic arrivé quelques minutes après l'envoi (deux par défaut) est une machine : c'est un filtre qui inspecte le message.
3. **La rafale.** Plusieurs liens du même message cliqués dans la même seconde sont une machine.
4. **L'adresse partagée.** La même adresse qui clique chez plusieurs entreprises dans l'heure est une machine.
5. **Le propriétaire de l'adresse.** Un hébergeur, un nuage ou un filtre de messagerie signe une machine. Un fournisseur d'accès (fixe, mobile, entreprise) laisse un humain possible.
6. **La signature du navigateur.** Un clic sans signature de navigateur, ou avec une signature nue, est une machine.
7. **La localisation.** Un clic humain possible, localisé dans la ville ou la région de l'entreprise, est humain très probable. Ailleurs, il est humain probable.

Le script `src/verdict_clic.py` applique ces sept indices, avec les listes de l'entreprise (fournisseurs d'accès, départements et régions, code du lien piège) lues dans sa configuration. Le harnais écrit le verdict et son motif sur le signal, sans go : ce n'est pas la fiche d'un suspect, c'est une donnée de mesure.

## Ce qu'un vrai clic déclenche

Un clic humain probable ou humain très probable fait, au point du matin qui le juge :

1. le suspect passe à l'étape « signal détecté ». Cette étape reste dans le pipeline des suspects : il ne devient pas un prospect pour autant ;
2. sa séquence se met en pause : aucun message de série ne part tant que le commercial n'a pas décidé ;
3. le harnais prépare une tâche de relance rattachée au suspect ;
4. il rédige un message personnel court, sur le sujet du contenu cliqué. Ce message ne mentionne jamais le clic : il pose une question qui ouvre la discussion ;
5. il propose au commercial d'aller voir lui-même le profil LinkedIn de la personne, s'il est connu, sans message ni invitation.

Ce message personnel n'est jamais couvert par le go d'une semaine : le commercial ne l'a pas lu. Il le valide à part, ou il entre dans la préparation de la semaine suivante.

Sans réponse dans le délai de la cadence de sa campagne après le message personnel, la séquence reprend au pas où elle s'était arrêtée, et la préparation de la semaine le montre.

Un clic n'est jamais une réponse. Un suspect qui clique sans écrire reste un suspect : un clic ne fait jamais d'un suspect un prospect, et il n'ouvre jamais d'affaire.

*Version 0.1 du 27/11/2026, reprise du règlement de prospection de LABK (traitement des réponses du 06/09/2026, verdict des clics validé par Laurent le 16/11/2026, étape « signal détecté » du 14/10/2026), sur la décision de Laurent du 27/11/2026.*
