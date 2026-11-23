# Les reviews de rendez-vous

Une review relit un rendez-vous, à partir de sa transcription, pour coacher le commercial sur sa façon de le mener. Les reviews se découpent par moment de la vente : la brief-review relit la découverte, la devis-review relit la présentation du devis, la négo-review relira la négociation (sa grille n'existe pas encore). Les trois rendent la même carte de coaching.

Statut : grilles de la méthode LABK validées. Qui peut demander une review au harnais se règle dans `../os/08-autorisations.md`, ou, sans ce fichier et hors mission LABK, par le commercial lui-même, quand il la demande (skill `coaching`, section 4).

## Les règles communes à toutes les reviews

1. **Mesurer le temps de parole.** Chaque review donne la part de parole du commercial et celle du client, en pourcentage et en minutes, avec le nombre d'interventions du client. Quand la transcription ne sépare pas les voix, les répliques sont attribuées au sens et le chiffre porte la mention « estimé ». Cible pour un entretien de découverte : le commercial ne parle pas plus de la moitié du temps.
2. **Cadrer la review quand le format sort du cadre.** Quand l'entretien ne correspond pas au format standard (un entretien très court, plusieurs interlocuteurs, une visio sans caméra), le harnais ne choisit pas seul les points à regarder. Il demande au commercial, ou à la personne qui a demandé la review, lesquels s'appliquent et ce qu'elle en attend. La réponse devient la consigne de cette review.
3. **Relire un entretien relais avec la grille complète.** Quand l'interlocuteur n'est pas décideur et que l'entretien sert à obtenir une mise en relation, la review applique quand même toute la grille.

## La brief-review : l'entretien de découverte

Elle dit si le commercial a cherché à comprendre le vrai problème du client et ce qu'il lui coûte, plutôt qu'à vendre. Dix points, dans cet ordre :

1. **Le temps de parole**, selon la règle commune.
2. **Les mots interdits.** Quand `../os/06-mots-interdits.md` existe, chaque mot de ce fichier prononcé par le commercial, avec son horodatage. Sans ce fichier, la review saute ce point.
3. **Le pitch : maîtrisé ou improvisé.** Ce que dit le commercial, comparé au pitch validé de `../os/01-offre-et-pitchs.md` : même promesse, même ordre, mêmes mots, ou bien un pitch qui change d'un entretien à l'autre.
4. **Ce qu'il affirme : vrai, inventé, ou à vérifier.** Chaque affirmation sur l'offre, les clients, les chiffres et les délais, confrontée à l'OS. Ce que le harnais ne peut pas vérifier est listé pour le commercial ou son responsable, qui tranche.
5. **Le cadrage du début.** Le commercial annonce-t-il ce qui va se passer après l'entretien, pour qu'aucune étape ne surprenne le client ? La preuve : chaque étape à venir qu'il nomme, avec l'horodatage.
6. **La découverte : la douleur et l'impact.** Le client a-t-il dit, dans ses mots, une vraie douleur et ce qu'elle lui coûte, sur ses deux faces ? On cite sa phrase. Une douleur dite par le commercial et approuvée d'un « oui » ne compte pas.
7. **Faire parler avant de proposer.** Le commercial pose-t-il des questions avant d'avancer une solution, ou imagine-t-il à la place du client (« j'imagine que… ») ? On relève chaque supposition non vérifiée.
8. **Savoir à qui il parle.** Le commercial connaît-il le rôle de la personne, qui d'autre décide, et sur quoi ? On cherche la question qui l'a établi, et sa réponse.
9. **Faire dire, reformuler, valider, puis argumenter.** On cherche ces trois temps avant chaque argument. Un argument sans reformulation validée est marqué comme prématuré, et la review donne la reformulation qu'il aurait pu dire. Le rebond en fait partie (`objections-acrac.md`).
10. **Le cadrage de la fin.** L'étape d'après est-elle posée (qui fait quoi, quand), le client a-t-il donné sa date, et le commercial lui a-t-il demandé de se munir des autres devis reçus pour en parler à la présentation ?

**Pour un entretien très court** (un rendez-vous de quinze minutes sur un salon) : le cadrage du début et le pitch tiennent en deux phrases, suivies d'une question qui fait parler le client ; la question de la décision se pose au rendez-vous suivant. Quand le commercial a qualifié les contacts et proposé les rendez-vous avant l'événement, la review ne juge ni la qualification ni la température du client : elle porte sur la façon de mener l'entretien.

## La devis-review : la présentation du devis

Elle dit si le commercial a fait sortir les points bloquants que la découverte n'avait pas montrés, et s'il a pris la température sur le prix. Quatre questions :

1. **A-t-il cherché ce qui pourrait bloquer ?** Une question ouverte, par exemple : « Qu'est-ce qui pourrait empêcher que ce projet se fasse avec nous ? » On relève ce que le client a répondu sur le décideur, le calendrier, le budget, un autre prestataire ou une contrainte.
2. **A-t-il pris la température sur le prix avant l'envoi ?** Le moment où il annonce le montant ou une fourchette, et la réaction du client, en mots ou en silence. Un prix envoyé sans avoir été dit à voix haute compte comme non sondé.
3. **Comment a-t-il traité ce qui est sorti ?** Chaque point bloquant et chaque réaction au prix se lisent avec `objections-acrac.md`.
4. **Le client a-t-il donné sa date de réponse ?** Il accuse réception du devis et dit quand il répondra.

La qualité du document de devis n'entre pas dans cette grille : elle porte sur la conversation.

## Ce que la review rend : la carte de coaching

Elle s'adresse au commercial, sur un ton bienveillant et simple :
1. le temps de parole ;
2. ce qui a marché d'abord, avec la phrase exacte et l'horodatage ;
3. au plus trois choses à essayer, chacune avec une phrase à dire la prochaine fois ;
4. un seul réflexe à travailler.

Elle ne nomme jamais un temps de l'ACRAC ni une note : elle dit l'idée. Elle parle du moment de l'échange, jamais de la personne. Pour une série d'entretiens le même jour, elle rend une carte par entretien, puis une ligne sur le réflexe qui revient.

## Ce qui se règle chez chaque entreprise

L'étape du parcours qui correspond à la découverte et celle qui correspond à la présentation du devis, avec le critère qui fait passer à l'étape suivante, se lisent dans `../os/03-parcours-client.md`.
