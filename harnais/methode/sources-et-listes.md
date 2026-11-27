# Construire une liste

Cette méthode dit comment une liste de suspects se construit, d'où elle peut venir, et quand elle est prête. Elle sert à la skill `liste`. Les sources autorisées et leur coût sont des réglages de l'entreprise, dans `../os/13-prospection.md`.

## Le principe

Une liste est prête quand chaque suspect qu'elle contient a une raison d'être là, une adresse vérifiée, une entreprise rattachée, et qu'aucun n'est déjà connu de l'entreprise. Une liste plus courte et propre vaut mieux qu'une longue liste qui use l'adresse et le temps du commercial.

La liste ne se construit jamais de la propre initiative du harnais. Le commercial donne la cible et le nombre voulu. Le harnais peut dire que le stock baisse et combien il manque, il ne lance jamais seul une recherche.

## L'ICP de la campagne

L'ICP de la campagne se dérive de l'ICP de l'OS (`../os/02-icp.md`) : il en prend un cercle, ou une partie d'un cercle, et il y ajoute ce qui rend la campagne précise (une région, un secteur, une taille, un signal). Le harnais le propose en relisant ce que l'entreprise sait déjà : les ICP des campagnes passées, les périmètres déjà parcourus, les motifs des suspects écartés et les résultats des bilans. Le commercial corrige et valide.

Un suspect hors de l'ICP de l'OS n'entre pas dans la liste, sauf si le commercial le décide pour cette liste. Le harnais lui dit alors une fois pourquoi ce suspect est hors cible, puis il l'ajoute et note que c'est le choix du commercial.

## Le contrôle de la source

Avant toute recherche, la source est contrôlée. Le contrôle se fait en tête, parce qu'une liste construite sur une source interdite est perdue tout entière.

| Source | Verdict par défaut | Ce que fait le harnais |
|---|---|---|
| Un fournisseur de données sous licence pour la prospection, nommé dans `../os/13-prospection.md` | Vert | Il annonce le coût avant toute dépense et attend le go |
| Un fichier que le commercial fournit (ses contacts, une liste d'exposants, un annuaire acheté) | À vérifier | Il demande d'où vient le fichier et si son usage pour prospecter est permis |
| Une page publique désignée par le commercial (annuaire de membres, liste de lauréats) | À vérifier, cas par cas | Il lit les conditions d'utilisation du site et annonce un verdict vert, orange ou rouge avant de lire la page |
| Les sites d'offres d'emploi | Rouge | Il refuse |
| LinkedIn | Rouge pour un outil | Il ne lit jamais LinkedIn. Il peut donner au commercial une liste de profils à ouvrir lui-même |

Le harnais ne cherche jamais une source de lui-même. Une source web est toujours désignée par le commercial, une à la fois, et on ne moissonne pas largement.

## Les lots

Une recherche dans une source se fait par lot, avec un numéro et ses filtres. Avant une nouvelle recherche, le harnais relit les lots déjà faits, pour ne jamais parcourir deux fois le même périmètre et payer deux fois les mêmes contacts.

## Le score d'adéquation

Chaque suspect reçoit un score d'adéquation de 0 à 10, calculé sur les critères de l'ICP de la campagne. Le seuil est un réglage de `../os/13-prospection.md` (6 par défaut).

- Au seuil ou au-dessus, le suspect est **dans la cible**.
- Sous le seuil, il est **hors cible**, et son motif est noté. Il reste dans la trace, jamais supprimé, parce que les motifs des écartés nourrissent les ICP suivants.
- Quand un critère ne peut pas être vérifié, il est **à vérifier** et ne compte pas dans le nombre voulu.

Le harnais peut lire le site public de l'entreprise pour affiner un score. Il ne note jamais une personne sur sa vie privée.

## Ce qui fait entrer un suspect dans le nombre

Un suspect compte dans le nombre voulu quand trois choses sont vraies : il est dans la cible, son adresse est vérifiée, et il n'a jamais été touché par cette campagne. Une adresse est vérifiée (`bon`) quand un fournisseur l'a vérifiée ou, sans fournisseur, quand le commercial la déclare bonne pour ce fichier, ce que le harnais trace comme sa décision. Une adresse générique (contact, info) ou personnelle est risquée (`risque`). Une adresse risquée ou manquante (`manquant`) ne part pas : le suspect reste noté, et son entreprise reste à trouver.

## Le dédoublonnage

Le dédoublonnage se fait deux fois.

1. **Pendant la construction**, contre les autres listes et les autres campagnes : un suspect n'est que dans une campagne à la fois.
2. **À la fin**, contre le CRM, en lecture seule : tout suspect déjà connu (cherché par l'adresse d'abord, sinon par le nom et l'entreprise) sort de la liste, avec son motif. La comparaison se fait aussi par entreprise, par le domaine du site puis par le nom : une entreprise qui compte déjà un prospect, un client ou une demande d'arrêt sort entièrement, quelle que soit la personne. S'il est déjà prospect, il a une affaire que le coach CRM suit. S'il est déjà client, il ne reçoit jamais de message de prospection. S'il est déjà suspect, il est déjà dans une campagne ou dans le temps long.

Avec le registre au lieu d'un CRM, le dédoublonnage de fin se fait contre `../registre/contacts.csv`.

## Une entreprise, une personne contactée

Le suspect est l'entreprise, et la campagne écrit à une seule personne chez elle : le dirigeant ou le fondateur d'abord, sauf si l'ICP de la campagne désigne un autre rôle. Quand la source sort le mauvais rôle, on ne jette pas l'entreprise : la personne passe hors cible, et l'entreprise reste à trouver, pour chercher la bonne personne.

Chaque personne contactée est rattachée à son entreprise. Il n'y a jamais de contact sans entreprise.

## Une entreprise qui a parlé

Quand une personne d'une entreprise s'engage (rendez-vous, réponse sur le fond, conversation en cours) ou refuse, l'entreprise entière sort des listes et des campagnes. Le harnais le dit au commercial, qui décide de la suite. Une demande d'arrêt d'une personne vaut pour toutes les campagnes.

## Quand la liste est prête

Quand le nombre est atteint, le harnais présente la liste en une page : sa référence, les lots dont elle vient, la répartition par segment, le nombre de suspects écartés et leurs motifs. La liste n'est prête qu'après le go du commercial. Elle attend ensuite qu'il l'associe à une campagne : le harnais ne fait jamais ce lien de lui-même.

## Le stock

Pendant une campagne, le harnais surveille le stock de suspects encore jamais touchés. Quand il tombe sous un seuil (par défaut, dix jours ouvrés d'envois au rythme du moment), il le dit au point du matin, en trois chiffres : combien il en reste, à quelle date le stock est épuisé, et combien il en faut pour tenir jusqu'à la date du bilan. Il alerte, il ne bloque rien, et il prépare les filtres de la recherche suivante. C'est le commercial qui la lance.

*Version 0.1 du 27/11/2026, reprise de la machine à listes de LABK (fiche du 13/07/2026) et du règlement de prospection de LABK, sur la décision de Laurent du 27/11/2026.*
