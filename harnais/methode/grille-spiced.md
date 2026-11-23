# La grille SPICED

Cette grille dit ce que vaut chaque note de 0 à 3, lettre par lettre. Le harnais s'en sert pour proposer les scores à partir des comptes rendus, le commercial pour décider de la valeur finale, et l'architecte CRM l'installe dans le CRM de l'entreprise (`../os/11-crm.md`). C'est la même chez tous les clients de LABK.

Statut : grille de la méthode LABK.

## Ce qu'elle mesure

La grille ne dit pas une vérité sur l'affaire : elle dit où est le risque de parler à la mauvaise personne, au mauvais moment, pour de mauvaises raisons. Une lettre est acquise à 2, avec une preuve dans une note : la phrase du client, avec ses mots, et la date de l'échange. Ce que le commercial a dit lui-même, ou ce que le client a approuvé d'un simple oui, ne compte pas comme preuve.

## Les quatre niveaux, lettre par lettre

| Lettre | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| S, la situation | Inconnue | Partielle : on connaît l'entreprise, pas encore son organisation ni ses outils | Comprise : dans la cible, son organisation et ses outils sont connus | Confirmée : le client se reconnaît dans la description qu'on lui en fait |
| P, la douleur | Inconnue | Supposée : c'est nous qui la voyons, ou le client l'a seulement approuvée | Dite : par le client, avec ses conséquences, dans ses mots | Partagée : dite par plusieurs personnes du compte |
| I, l'impact | Inconnu | Ressenti : sans chiffre, ou un chiffre dit par le commercial | Chiffré : par le client, en heures, en jours, en euros ou par une estimation crédible qu'il a faite lui-même | Repris : le chiffre est repris à son compte par un décideur |
| CE, l'événement critique | Inconnu | Sans date | Daté : un événement nommé, avec sa date dite par le client | Imminent : la date dite par le client tombe dans moins de trois mois |
| D, la décision | Inconnue | Décideur nommé, sans le circuit | Circuit connu : une personne du compte, pas forcément le décideur, a décrit qui décide, comment et sur quels critères, et a dit d'où vient l'argent ou quand le budget se décide | Confirmée : par le décideur lui-même |

## Les cas qui reviennent

- **Un chiffre en temps que le client n'a pas validé** (« une demi-journée, quarante cadres ») : c'est un chiffre dit par le client, donc I à 2. Le commercial le fait valider (« si je résume, cela vous coûte tant, c'est bien ça ? ») et le fait convertir en euros par le décideur pour viser le 3.
- **Un décideur connu par le seul récit du commercial** : D à 1 au plus, tant que le client ne l'a pas dit lui-même.
- **Un circuit décrit sans réponse sur l'argent** (« ça dépendra du prix », un budget de l'an prochain pas encore décidé) : D à 1. Le harnais donne au commercial la question qui fait passer à 2 : « Ce budget, il se décide quand, et par qui ? »
- **Un circuit décrit par un utilisateur** plutôt que par le décideur : il suffit pour le 2, s'il dit aussi d'où vient l'argent. Le 3 demande que le décideur confirme lui-même.
- **Un événement daté sans conséquence nommée** : CE à 2, ou à 3 si sa date tombe dans moins de trois mois. La conséquence ne change pas le score. Le risque qui reste se signale avec la question « si rien n'est en place à cette date, qu'est-ce qui se passe pour vous ? » (`evenement-critique.md`).
- **L'impact émotionnel** ne change pas le score du I : il s'écrit dans le compte rendu, en une phrase du client (`douleur-et-impact.md`).

- **Un CE à 2 qui devient imminent** : le CE monte à 3 de lui-même quand la date approche à moins de trois mois, sans nouvel échange. Le harnais le propose au commercial avec la preuve d'origine, la phrase et sa date.

## Quand le CRM n'a pas de champ pour une lettre

Le score s'écrit dans la note de qualification de l'affaire, une ligne par lettre, en début de ligne, sous la forme « CE : 2, <phrase du client>, <date de l'échange> ». Le harnais relit ces lignes à la place du champ. Sans champ et sans ligne, la lettre vaut 0.
