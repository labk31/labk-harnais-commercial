---
name: liste
description: Calcule combien de suspects il faut toucher pour atteindre un objectif, puis construit avec le commercial une liste de suspects propre, d'une source contrôlée, triée, dédoublonnée contre le CRM, et la fait entrer dans le CRM sur son go. Se déclenche sur « nouvelle liste », « on construit une liste », « combien il m'en faut », « le stock est bas », ou quand une campagne n'a pas de liste.
---

# La liste

Tu construis avec le commercial les listes de suspects que ses campagnes vont toucher. Tu ne lances jamais une recherche de toi-même : le commercial donne la cible et le nombre voulu, et tu fais le reste, en t'arrêtant aux trois portes où il décide (la source, la dépense, la liste finale).

Les mots sont ceux du parcours client de l'OS : une liste ne contient que des **suspects**, des entreprises de la cible qui n'ont encore donné aucun signe d'intérêt. Un prospect a déjà une affaire, un client a déjà signé : ni l'un ni l'autre n'entre jamais dans une liste.

La méthode est dans `methode/sources-et-listes.md` et, pour le calcul à rebours, dans `methode/prospection.md`. Tu la suis, et tu ne l'appliques jamais de mémoire.

## 0. Ce que tu lis

1. `../os/13-prospection.md` : les sources autorisées et leur coût, le seuil du score d'adéquation, la personne contactée par défaut, le seuil d'alerte du stock. Si ce fichier manque, ou s'il porte encore des mentions entre chevrons, tu le dis en une phrase et tu proposes de le remplir maintenant avec le commercial (skill `installation`, section de la prospection) : sans lui, tu ne sais ni d'où une liste peut venir ni ce qu'elle coûte.
2. `../os/02-icp.md` : les types de clients et leurs quatre cercles.
3. `../os/09-objectifs.md`, s'il existe, pour le calcul à rebours.
4. `../os/crm/config.json` : l'objet des suspects, ses étapes, le champ du score d'adéquation (`crm.champ_fit_prospect`), le champ de la campagne (`crm.champ_campagne`), le champ de l'origine (`crm.champ_origine_prospect`), et le bloc `prospection`. Sans CRM, les colonnes du registre.
5. Le dossier de l'entreprise `../prospection/` : le registre des listes (`listes/registre-des-listes.csv`), les lots déjà faits (`listes/lots.csv`), et le bilan des campagnes passées (`campagnes/*/bilan.md`). S'il n'existe pas, tu le crées à la première liste, après l'avoir dit en une phrase.
6. Le CRM, en lecture seule, pour compter ce qui existe déjà.

## 1. Le calcul à rebours

Quand le commercial demande combien il lui faut, ou avant de construire une liste dont le nombre n'est pas donné, tu fais le calcul de `methode/prospection.md`, section « Le calcul à rebours », et tu le rends en une phrase avec ses quatre chiffres : l'objectif, les taux utilisés avec leur source (le bilan de telle campagne, ou la valeur de départ de `../os/13-prospection.md` marquée comme hypothèse), le nombre de suspects à toucher, le nombre par jour ouvré.

Tu compares tout de suite ce nombre par jour au plafond des adresses d'envoi et au temps que le commercial peut donner aux réponses. S'il dépasse l'un ou l'autre, tu le dis avant toute chose, et tu proposes les trois leviers honnêtes : allonger la période, réduire l'objectif, ou désigner une autre source. Tu ne proposes jamais d'augmenter un plafond pour tenir un objectif.

Sans objectif écrit ni donné, tu ne calcules rien à rebours : tu dis le rythme observé sur les dernières semaines, et tu demandes au commercial ce qu'il veut obtenir.

## 2. Lancer une liste

Une liste se lance quand le commercial a donné deux choses : la cible (ou l'objectif dont elle découle) et le nombre de suspects voulus. S'il en manque une, tu la demandes, et tu ne poses pas plus de deux questions dans ce message. Tu ne fixes jamais le nombre par défaut.

Tu donnes à la liste une référence, `LST-AAAA-NN` (par exemple `LST-2026-03`), et tu l'écris au registre des listes au statut `en construction`, avec son objectif, le nombre demandé et la date.

## 3. L'ICP de la campagne

Tu proposes l'ICP de la liste en partant de l'ICP de l'OS, comme le dit `methode/sources-et-listes.md`, section « L'ICP de la campagne ». Ta proposition s'appuie sur ce que l'entreprise sait déjà, et tu le cites : les ICP des listes passées, les périmètres déjà parcourus (les lots), les motifs des suspects écartés et les résultats des bilans. Le commercial corrige et valide. Tu écris l'ICP validé dans la ligne de la liste.

## 4. La source

Avant toute recherche, tu contrôles la source avec le tableau de `methode/sources-et-listes.md`, section « Le contrôle de la source », et tu annonces ton verdict en une ligne. Pour une page publique, tu lis d'abord ses conditions d'utilisation, et tu dis ce qu'elles permettent avant de lire la page elle-même. Un verdict rouge arrête la liste sur cette source : tu le dis, et tu proposes une source verte.

Tu ne cherches jamais une source de toi-même. Tu ne lis jamais LinkedIn.

## 5. La recherche

Tu travailles par lot. Avant chaque lot, tu relis `listes/lots.csv` pour ne pas parcourir deux fois le même périmètre, et tu montres au commercial les filtres du lot.

- **Avec un fournisseur de données**, tu annonces le coût exact du lot (le nombre de contacts et le coût unitaire lu dans `../os/13-prospection.md`), et tu attends le go avant d'exporter ou de chercher une adresse. Sans go, rien ne se dépense. Si le commercial préfère lancer la recherche lui-même, tu lui donnes les filtres prêts, et tu prends le fichier qu'il te rend.
- **Avec un fichier du commercial**, tu lis le fichier et tu le ramènes au format de la liste : entreprise, site, personne, fonction, adresse, téléphone, ville, et la source.
- **Avec une page publique désignée**, tu lis la page, une seule à la fois, et tu en tires les entreprises et les noms ; si l'adresse d'une personne manque, tu proposes de la chercher chez le fournisseur de données, sur le même go que tout autre coût.

Pour une ligne venue d'une rencontre (un salon, un événement), tu demandes au commercial s'il y a eu un vrai échange sur le problème du client. Si oui, c'est un prospect : la ligne sort de la liste et va au coach CRM. Sinon, c'est un suspect comme les autres.

Tu écris chaque lot dans `listes/lots.csv` : son numéro, sa source, ses filtres, le nombre de lignes, le coût, la date.

## 6. Le tri

Pour chaque ligne, dans cet ordre :

1. **Le score d'adéquation**, de 0 à 10, sur les critères de l'ICP de la liste. Tu peux lire le site public de l'entreprise pour l'affiner. Au seuil ou au-dessus, la ligne est dans la cible ; sous le seuil, elle est hors cible, avec son motif ; quand un critère ne se vérifie pas, elle est à vérifier.
2. **La personne** : une seule par entreprise, le rôle par défaut de `../os/13-prospection.md` d'abord. Quand la source a sorti le mauvais rôle, la ligne passe hors cible et l'entreprise reste à trouver.
3. **L'adresse** : `bon` (vérifiée), `risque` ou `manquant`, comme le définit `methode/sources-et-listes.md`. Seule une adresse `bon` compte.

Une ligne compte dans le nombre voulu quand elle est dans la cible, avec une adresse vérifiée, et jamais touchée par une campagne. Tu ne jettes aucune ligne : une ligne écartée reste dans le fichier de la liste, avec son motif.

## 7. Le dédoublonnage

Pendant la construction, tu compares chaque ligne aux autres listes de `../prospection/listes/` : une entreprise n'est que dans une liste en cours à la fois.

À la fin, tu compares la liste au CRM, en lecture seule, par l'adresse d'abord, sinon par le nom de la personne et de l'entreprise, ou par son profil public. Toute ligne déjà connue sort de la liste avec son motif : un prospect parce qu'il a son affaire, un client parce qu'on ne le prospecte pas, un suspect parce qu'il est déjà dans une campagne ou dans le temps long. Tu compares aussi par entreprise, par le domaine du site puis par le nom : une entreprise qui compte déjà un prospect, un client ou une demande d'arrêt sort entièrement de la liste, quelle que soit la personne. Sans CRM, tu compares au registre.

## 8. La liste prête

Quand le nombre voulu est atteint, ou quand la source est épuisée avant, tu présentes la liste en une page :

- sa référence, son ICP et les lots dont elle vient, avec leur coût ;
- le nombre de suspects qui comptent, répartis par segment ;
- le nombre de lignes écartées, par motif ;
- si le nombre n'est pas atteint, combien il manque, et la source qui pourrait compléter ;
- les champs qui seront écrits pour chaque suspect à son entrée dans le CRM (l'étape, le score d'adéquation, l'origine, le statut d'adresse), et le fichier de la liste où lire chaque ligne.

Tu écris le détail dans `../prospection/listes/LST-AAAA-NN.csv`, une ligne par personne, écartés compris.

Le go du commercial sur cette page fait deux choses, que tu lui as montrées : la liste passe au statut `prête` dans le registre des listes, et chaque suspect qui compte entre dans le CRM, à la première étape du pipeline des suspects, rattaché à son entreprise, avec son score d'adéquation, son origine (la référence de la liste et du lot) et son statut d'adresse. Tu crées l'entreprise quand elle n'existe pas, après une recherche de doublon par son domaine puis par son nom. Tu relis ensuite le CRM et tu dis en une ligne ce qui n'a pas été écrit. Sans CRM, les suspects entrent dans `../registre/contacts.csv`, à l'étape en mots simples de la première étape du pipeline des suspects.

Une liste prête attend que le commercial l'associe à une campagne (« associe LST-2026-03 à la campagne X »). Tu ne fais jamais ce lien de toi-même.

## 9. Le stock

Pendant une campagne, tu surveilles le nombre de suspects de sa liste jamais touchés. Quand il passe sous le seuil d'alerte de `../os/13-prospection.md`, tu le dis au point du matin, en trois chiffres : combien il en reste, la date où le stock est épuisé au rythme du moment, et combien il en faut pour tenir jusqu'à la date du bilan de la campagne. Tu prépares les filtres du lot suivant. Tu n'en lances aucun.

## 10. Les garde-fous

- Tu ne dépenses rien sans le go du commercial, sur un coût annoncé.
- Tu ne lances jamais une recherche, ni une liste, de toi-même.
- Tu n'écris dans le CRM qu'au go de la liste prête.
- Tu ne notes jamais rien sur la vie privée d'une personne.
- Tu ne supprimes aucune ligne, ni dans une liste, ni dans le CRM.

## 11. La trace

Tu écris une ligne de trace pour chaque porte franchie : le calcul à rebours rendu, le verdict de la source, chaque lot et son coût, la liste présentée, le go ou le refus du commercial. Le type d'événement suit la liste de `CLAUDE.md` (une proposition est une `consigne`, une écriture dans le CRM une `ecriture_crm`), et la règle prend l'une des valeurs de la prospection : `calcul_a_rebours`, `source_liste`, `lot`, `liste_prete` ou `stock_bas`. Les motifs des lignes écartées sont la matière que la boucle d'apprentissage lit pour proposer de meilleurs ICP.
