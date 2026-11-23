# Placer une affaire sur la preuve

Cette méthode dit à quelle étape va une affaire, au moment où elle entre dans le CRM et chaque fois qu'elle doit changer d'étape.

## Le principe

Une affaire va à la plus haute étape dont la preuve existe. La preuve est une phrase du client, avec ses mots, dans une note ou un compte rendu daté. Ce que le commercial a dit lui-même ne compte pas, même s'il le répète avec conviction.

Les étapes se cumulent : une affaire qui n'a pas sa preuve d'impact reste à l'étape qui précède, même si elle a déjà un appui chez le client. La première lettre du SPICED qui manque dit l'action suivante.

Un placement doit pouvoir s'expliquer au commercial, affaire par affaire, avec la phrase du client qui le justifie. Il n'y a pas de placement sans cette phrase.

## Quand une affaire entre dans le CRM sur le récit du commercial

C'est le cas le plus fréquent : le commercial raconte une affaire qu'il connaît, et le CRM ne la porte pas encore.

1. Le harnais cherche la preuve du client : une transcription, un mail, une note. S'il la trouve, l'affaire va à l'étape qu'elle prouve.
2. S'il ne la trouve pas, l'affaire entre à la première étape de qualification du parcours de l'entreprise, avec la mention « placée sans preuve du client, à confirmer ».
3. Si le commercial veut la placer plus haut, c'est son choix. Le harnais lui dit en une phrase ce qui manque et ce que cela provoque (le portefeuille paraît plus avancé qu'il n'est, et le point du matin la classe mal), puis il écrit le choix du commercial dans la note de l'affaire et dans la trace, comme une décision du commercial. Il ne le lui reproche pas.

## Les étapes du placement

1. Lister les affaires à placer, avec leur étape actuelle, leurs scores et la date de leur dernière modification.
2. Lire toutes les notes de chaque affaire, celles de l'affaire et celles de l'entreprise, car les notes anciennes sont souvent sur l'entreprise seule. Lire aussi les comptes rendus que le commercial a hors du CRM.
3. Lire les fils de mail de l'affaire et de l'entreprise, au moins les dates et les expéditeurs : qui a écrit en dernier, et si une réponse du client attend. Un mail reçu la veille n'est presque jamais encore noté, et c'est souvent lui qui dit si l'affaire est vivante.
4. Relever, lettre par lettre, la phrase du client qui prouve chaque niveau, avec sa source et sa date. Marquer ce qui vient du commercial comme ne comptant pas.
5. Déduire l'étape : la plus haute dont toutes les lettres nécessaires sont acquises. Une affaire sans aucune note revient au plus haut à la première étape de qualification, avec le risque « Rien de noté ».
6. Déduire les scores à partir des mêmes phrases, puis le risque principal.
7. Présenter la liste au commercial avant de toucher au CRM : pour chaque affaire, l'étape, la phrase du client, sa source, la lettre qui manque. Une affaire dont le sort dépend d'une décision (la passer en perdu, par exemple) reste à l'étape que prouvent ses notes tant que la décision n'est pas prise.
8. Après le go, écrire les étapes, puis les scores, puis le risque, puis la date de qualification.
9. Relire le CRM et comparer à la liste validée.
10. Faire entrer dans le CRM, sous forme de notes, les preuves trouvées hors du CRM. Sans elles, le harnais ne pourra plus expliquer le placement.

## Les pièges

- **Un rendez-vous tenu n'est pas une preuve.** Une démonstration devant deux décideurs ressemble à un projet porté ; si personne n'a chiffré la douleur, l'affaire reste à l'étape du problème reconnu.
- **Une date ne remplace pas un chiffre.** Un appel à projets daté ne fait pas l'impact ; la date sert de levier pour faire chiffrer.
- **Un chiffre dit par le commercial ne compte pas.** « Ça vous fait perdre une heure ou deux, non ? » suivi d'un oui n'est pas un chiffre du client.
- **Une affaire sans note ne garde pas une étape haute.** Des scores anciens sans aucune note se revoient.
- **Les notes ne suffisent pas.** Sans la lecture des mails, une affaire qui vient de répondre peut être jugée endormie.
- **Une affaire peut reculer.** Une affaire en qualification dont personne n'a encore accepté de créneau revient à l'étape d'avant.
- **Un déplacement fait repartir le délai de l'étape.** Le commercial doit le savoir.

## Ce qui se règle chez chaque entreprise

Les noms des étapes et des champs viennent de `../os/crm/config.json`. Les preuves attendues à chaque étape viennent de `../os/03-parcours-client.md`.
