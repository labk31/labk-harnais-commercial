# Le parcours client

Ce fichier regroupe tout ce qui rend le parcours du client fluide et qui doit être décidé dès le départ : les étapes des deux pipelines, les règles de cadrage, les motifs de refus attendus à chaque étape, et les règles de nurturing. Le SPICED de référence vit à côté, dans le dossier `spiced-reference/`.

La personne autorisée le remplit. Chez celui qui vend seul, c'est vous, avec le harnais, à l'installation. Les deux pipelines, celui des suspects et celui des prospects, sont immuables (référentiel LABK). Les étapes détaillées, les délais, les règles de cadrage et les règles de nurturing sont révisables. Ce fichier se remplit avec les demandes 10, 15, 16, 17, 18 et 21 de la liste minimale (`collecte/liste-minimale.md`), puis, avec LABK, par l'atelier du parcours cadré.

## Ce qu'il faut pour démarrer

Ce fichier est le plus long de l'OS, et personne ne le remplit d'un coup. Pour que le harnais tourne, il suffit de deux choses : les étapes du pipeline des prospects, en mots simples, avec la preuve qui fait passer de l'une à l'autre, et la preuve qu'une affaire est gagnée. Le cadrage vient ensuite, en commençant par les deux premières étapes. Aucune demande de la liste minimale ne vous fait écrire les étapes : le harnais part des étapes déjà écrites dans `crm/config.json`, les décrit ici en mots simples avec vos réponses sur la façon dont vos clients arrivent et achètent (demandes 10, 15, 16, 18 et 21), et vous corrigez ce qui ne ressemble pas à vos ventes. Si vous renommez une étape, il change le nom dans la configuration et le sens ici, aux deux endroits à la fois. Les motifs de refus reçoivent dès l'installation vos réponses aux demandes 16 et 18, en hypothèse. L'échéance de décision et le nurturing se remplissent plus tard, au fil des affaires, quand une situation réelle en a besoin.

## Trois mots, à tenir partout

Ces trois définitions sont immuables (référentiel LABK).

- **Suspect** : une entreprise dans la cible qui n'a donné aucun signe d'intérêt.
- **Prospect** : une entreprise qui a donné un signe d'intérêt, c'est-à-dire un échange humain réel : une réponse, un appel, une rencontre ou un rendez-vous accepté. Un clic ou une ouverture de mail ne suffit pas.
- **Client** : une entreprise qui a signé.

## Le pipeline des suspects

Un suspect est une entreprise du bon profil qui n'a encore donné aucun signal humain. Il devient un prospect au premier signal humain : une réponse, un appel, une rencontre. Ses étapes se tirent de la façon dont vos clients arrivent chez vous (demande 21).

| Étape, en mots simples | Ce qui la définit | Ce qui fait passer à la suivante |
|---|---|---|
| <étape> | <définition> | <signal> |

## Le pipeline des prospects

| Étape | Ce qui la définit | Ce qui fait passer à la suivante | Délai au-delà duquel l'affaire est en silence |
|---|---|---|---|
| <étape> | <définition> | <preuve attendue> | <délai> |

Chaque étape a sa ligne, y compris la négociation et la signature. La dernière ligne dit ce qui prouve qu'une affaire est gagnée (par exemple un devis signé, un bon de commande, ou un mail du client qui accepte, gardé dans le CRM) et ce qui se passe ensuite (la remise à ceux qui livrent). Sans cette preuve, le harnais propose l'étape d'avant et dit ce qui manque.

Ici, chaque étape se décrit en mots simples, par ce qu'elle veut dire pour le client. Son nom technique dans le CRM ne s'écrit qu'à un seul endroit, `crm/config.json`, rempli par l'architecte CRM après la pose (ou par le harnais avec celui qui vend seul). Le délai de silence de chaque étape est reporté de la même façon dans `crm/config.json` (`silence.jours_avant_statut_par_etape`). Sans CRM, il n'y a pas de nom technique : le registre porte, dans sa colonne `etape`, le nom en mots simples écrit ici. Si les deux ne se correspondent pas, c'est ce fichier-ci qui dit le sens, et la configuration qui dit le nom.

## Les trois temps du pipeline des prospects

Quand l'entreprise retient la méthode LABK complète, le pipeline des prospects se lit en trois temps. Celui qui vend seul peut s'en tenir à une seule suite d'étapes ; le harnais saute ce que la configuration ne désigne pas.

- **La Maturation** : de la première conversation (New deal) au projet défendable, une marche par lettre du SPICED. On y fait mûrir le projet du client, sans parler de prix.
- **La Signature** : ce qui se passe une fois le projet défendable, jusqu'au gagné. Ses étapes habituelles sont la proposition (un seul devis, envoyé après avoir parlé à celui qui décide), la négociation (ce qui se cède, selon la grille des contreparties s'il y en a une) et la signature (la preuve écrite que le client accepte). L'entreprise peut les renommer ; leurs noms techniques vont dans `crm.etapes_signature`.
- **Le gagné et le perdu** : le gagné porte la preuve de l'accord et déclenche la remise à ceux qui livrent ; le perdu porte toujours son motif.

## Les règles de cadrage

Ce que le commercial doit savoir avant d'engager un effort : un devis, une démonstration, un deuxième rendez-vous.

- <règle> (statut, source)

Exemple de règle : aucun devis ne part sans avoir parlé à la personne qui décide.

## L'échéance de décision

L'échéance est la date à laquelle le client doit avoir décidé, compte tenu de tout ce qu'il faut faire avant pour être prêt le jour J. Elle se calcule à rebours à partir d'une date de référence (`../harnais/methode/evenement-critique.md` dans la base du harnais).

- La date de référence de l'entreprise, tirée de ce qui se passe chez le client juste avant qu'il vous appelle (demande 10) : <la date de l'événement du client, si le métier en a une ; sinon « aucune, à trouver avec le client à chaque affaire »> (statut, source)
- Les délais de préparation qui servent au calcul à rebours : <délais, par type de prestation> (statut, source)
- Les options, si l'entreprise en pose : leur durée, ce qui se passe à leur échéance, et qui peut les prolonger : <règle> (statut, source)

## Le cadrage et la conversation de chaque étape

Pour chaque étape du parcours, l'entreprise écrit ce que le commercial annonce et ce qu'il cherche à obtenir. Le harnais s'en sert pour préparer chaque rendez-vous. Pendant une mission LABK, ce contenu sort de l'atelier du parcours cadré, qui se tient avant l'intervention de l'architecte CRM : l'architecte le reçoit et le traduit dans le CRM, il ne l'écrit pas. Les phrases sont des propositions tant que la personne autorisée ne les a pas validées.

Ne remplissez pas tout d'un coup. Cinq rubriques par étape, sur six étapes, font trente rubriques, et personne ne les écrit en une fois. Commencez par les deux premières étapes, celles où se jouent le premier échange et la découverte : ce sont elles qui font gagner le plus. Les autres se remplissent quand une affaire réelle y arrive ; d'ici là, le harnais prépare le rendez-vous avec la méthode LABK et le dit.

### <étape>

- **Ce que le commercial annonce** : pourquoi on se parle, combien de temps, ce qui va se passer, ce qu'on décidera ensemble à la fin. (statut, source)
- **Ce qu'il désamorce** : les mauvaises surprises et les objections possibles à cette étape, dites avant qu'elles arrivent (demande 17). (statut, source)
- **La phrase de cadrage** : le texte prêt à dire, qui finit par une question d'accord (« Ça vous va ? »). Sans ce oui, le commercial recadre avant d'avancer. (statut, source)
- **Ce qu'il cherche à savoir** : les lettres du SPICED que l'étape doit faire monter, et deux à quatre questions. (statut, source)
- **Ce qu'il apporte** : la preuve ou le contenu qui fait avancer (une raison de parler, un cas client, une démonstration centrée sur la douleur dite, le prix posé à côté du coût du problème). Les raisons pour lesquelles vous gagnez vos affaires (demande 15) en donnent la matière. (statut, source)

Quand une objection revient à une étape, le harnais propose un constat du terrain pour la désamorcer plus tôt, à cette étape ou à celle d'avant.

## Les motifs de refus attendus, par étape

Les raisons pour lesquelles une affaire s'arrête, telles qu'on les attend à chaque étape (demandes 16 et 18). Le harnais s'en sert pour classer une perte et pour repérer un motif nouveau.

| Étape | Motifs attendus |
|---|---|
| <étape> | <motif>, <motif> |

Motifs que l'entreprise n'accepte pas comme motif de perte : <motif> (statut, source).

## Les règles de nurturing

Ce que le harnais propose quand un suspect ou une affaire se tait ou s'arrête. Il applique ces règles, il ne les écrit pas, et aucune automatisation du CRM ne le fait à sa place.

Les motifs de perte qui demandent le même traitement se regroupent en familles (par exemple : attendre une date, faire naître le besoin, lever un frein, changer d'angle). Chaque motif qui a une suite appartient à une seule famille. Les suspects et les affaires n'ont pas toujours la même liste de motifs : rangez dans les familles les motifs des deux listes (par exemple « Pas le bon moment » d'un suspect et « Pas encore mûr » d'une affaire dans « attendre une date »).

| Famille | Les motifs qui y entrent | Ce que le commercial envoie (le type de contenu) | À quel rythme | Ce qui fait revenir l'affaire, et à quelle étape | Quand la fiche sort du nurturing |
|---|---|---|---|---|---|
| <famille> | <motifs> | <types de contenus> | <rythme> | <signal, étape de retour> | <condition> |

Les situations courantes :

| Situation | Ce que le harnais propose | Quand |
|---|---|---|
| Le prospect ne répond plus (ghosting) | <action> | <délai> |
| L'affaire est perdue face à un concurrent | <action> | <délai> |
| Le contrat du client chez un concurrent arrive à échéance | <action> | <délai> |
| Un devis est resté sans réponse | <action> | <délai> |
| Une rencontre sur un salon reste sans suite | <action> | <délai> |
