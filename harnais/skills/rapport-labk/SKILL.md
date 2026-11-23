---
name: rapport-labk
description: Prépare le rapport que l'entreprise envoie à LABK pour améliorer la méthode : versions installées, constats du terrain, consignes suivies et ignorées, règles personnelles posées contre la base, blocages, sans aucun nom de prospect ou de client, sans montant et sans contenu d'échange. Se déclenche sur « prépare le rapport pour LABK » ou « rapport LABK ».
---

# Le rapport pour LABK

Ce rapport sert à améliorer la méthode LABK à partir de ce que le harnais vit chez l'entreprise. C'est l'utilisateur qui le demande, qui le relit et qui l'envoie lui-même à LABK, par mail ou autrement. Chez celui qui vend seul, l'utilisateur, l'entreprise et le commercial sont la même personne : c'est lui qui le relit et qui l'envoie. Tu ne l'envoies jamais.

Le rapport parle de la méthode, jamais du commerce de l'entreprise. LABK n'a pas besoin de savoir à qui l'entreprise vend pour savoir quelle règle ne marche pas.

## 1. La période

Le rapport couvre la période qui commence à la date du dernier rapport, lue dans `personnel/rapports/`, ou à la date d'installation, lue dans `personnel/journal.md` s'il n'y a pas encore de rapport. Il s'arrête aujourd'hui.

## 2. Ce que tu lis

- `JOURNAL.md` pour la version de la base du harnais, et la ligne « Version » de `../os/00-sommaire.md` pour celle de l'OS.
- `../os/10-constats-du-terrain.md`, pour les constats de la période, s'il existe, et `personnel/constats-a-remonter.md`, pour ceux que l'OS n'a pas pu recevoir.
- La sortie de `src/wiki_loop.py rapport`, lancé depuis le dossier du harnais avec la commande Python notée dans `personnel/profil.md` (`python3` par défaut), comme le dit `CLAUDE.md`, pour les consignes suivies et ignorées, règle par règle. Tu n'en recopies pas la ligne « Instance » : c'est le nom écrit dans la configuration, parfois resté au gabarit. Si le script dit qu'aucune consigne n'est encore tracée, la section 3 le dit en une phrase.
- `personnel/wiki/skill-impact.md`, pour les verdicts de la boucle, s'il existe : il n'apparaît qu'après le premier contrôle d'une règle par la boucle.
- `personnel/regles-personnelles.md`, pour les règles posées par le commercial.
- `personnel/journal.md`, pour les blocages de la période.

## 3. Ce que contient le rapport

Tu écris le rapport en phrases complètes, dans cet ordre :

1. **Les versions et la période** : la version de la base du harnais, celle de l'OS, le nom de l'entreprise de l'utilisateur (la sienne, jamais celle d'un client), le rôle de l'utilisateur, l'édition de l'OS (solo ou équipe, lue dans `../os/00-sommaire.md`), la période couverte, et le nombre de sessions tracées.
2. **Les constats du terrain** : pour chaque constat de la période, ce qui a été constaté, la règle ou le fichier qu'il touche, et la suite donnée par l'entreprise (en attente, retenu, écarté). Pour un constat de `personnel/constats-a-remonter.md`, la suite se lit dans la colonne « Reporté le » : une date seule veut dire retenu et reporté dans l'OS à cette date, « écarté le AAAA-MM-JJ » veut dire écarté, et une case vide veut dire en attente. Tu dis si la règle touchée vient de l'OS de l'entreprise ou de la méthode LABK. La colonne « Preuve » d'un constat ne passe jamais dans le rapport telle quelle : elle nomme une affaire, et tu la remplaces par le type de client et l'étape (section 4).
3. **Les consignes suivies et ignorées** : pour chaque règle qui a donné au moins une consigne, le nombre de consignes, combien ont été suivies, combien refusées ou ignorées, et le verdict de la boucle s'il existe. Tu commences par les règles les plus ignorées, parce que ce sont elles qui disent ce qui ne marche pas.
4. **Les règles personnelles posées contre la base** : chaque règle que le commercial a posée pour lui et qui contredit une règle de la base, avec sa raison et sa date.
5. **Ce qui a bloqué** : une installation, une mise à jour, un champ du CRM absent, une écriture qui n'est pas passée, une demande que le harnais n'a pas su traiter.

Quand une section est vide, tu l'écris en une phrase.

## 4. Ce que le rapport ne contient jamais

- Aucun nom de prospect, de client ou de concurrent de l'entreprise, et aucun nom de personne en dehors de l'utilisateur.
- Aucun montant, aucun chiffre d'affaires, aucune remise.
- Aucun contenu d'échange : ni citation d'un client, ni extrait de mail, ni compte rendu.

Une affaire est citée par son type de client et son étape, jamais par son nom. Exemple : « une affaire chez une PME industrielle, en Problème reconnu », et non « l'affaire Dupont ». Un constat se dit de la même façon, par ce qu'il apprend sur la règle et non par ce qui s'est dit : « la règle de silence après un devis déclenche trop tôt pour les clients qui votent leur budget en comité », et non « le client nous a parlé d'un incident pendant le discours de son dirigeant ».

Avant de montrer le rapport, tu le relis en entier, et tu remplaces tout nom ou tout chiffre qui aurait échappé à cette règle.

## 5. La remise

Tu écris le rapport dans `personnel/rapports/rapport-labk-AAAA-MM-JJ.md`, en créant le dossier `personnel/rapports/` s'il n'existe pas encore, puis tu le montres à l'utilisateur. Il le relit et retire ce qu'il veut. Tu lui rappelles en une phrase qu'il l'envoie lui-même à LABK : une entreprise accompagnée l'envoie à son consultant ; celui qui utilise le kit gratuit l'envoie à Laurent Bouloc par un message sur LinkedIn (linkedin.com/in/laurent-bouloc), où le rapport se colle tel quel. Tu notes ensuite dans `personnel/journal.md` la date du rapport et la période qu'il couvre.
