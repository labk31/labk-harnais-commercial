---
name: mise-a-jour
description: Met à jour la base du harnais avec la dernière version publiée par LABK, sans toucher à la partie personnelle du commercial ni à l'OS de l'entreprise, et explique ce qui change. Se déclenche sur « mets-toi à jour » ou « y a-t-il une nouvelle version ».
---

# La mise à jour

LABK publie les nouvelles versions de la base du harnais. Le commercial décide quand il la récupère. Le kit gratuit se met à jour depuis son dépôt public sur GitHub ; l'édition entreprise reçoit chaque nouvelle version de LABK, sous forme d'archive ou de dossier.

## 1. Ce que la mise à jour touche, et ce qu'elle ne touche jamais

Elle remplace la base : `CLAUDE.md`, `skills/`, `methode/`, `src/`, `gabarits/`, `assets/`, `JOURNAL.md`, `PREREQUIS.md`, `CONFIDENTIALITE.md`, et, dans l'édition entreprise, `README.md` et `LICENCE.md`. Dans le kit gratuit, elle remplace aussi, à la racine du kit, la page de garde `README.md`, le `CLAUDE.md` d'entrée, `LICENSE`, `.gitignore` et le gabarit `os-gabarit/`.

Elle ne touche jamais `personnel/`, ni `../os/`, ni `../registre/`. Si une commande risquait de les modifier, tu t'arrêtes et tu le dis.

## 2. Comment tu fais

1. Tu lis la version installée, en tête de `JOURNAL.md`.
2. Tu gardes une copie de la base installée, pour pouvoir revenir en arrière : si le harnais est un dépôt git, la version précédente reste dans son historique ; sinon, tu copies la base (tout sauf `personnel/`) dans `personnel/sauvegardes/base-v<version>/`, la seule écriture que la mise à jour fait dans `personnel/`.
3. Tu récupères la dernière version. Dans le kit gratuit, si le dossier du kit est un dépôt git, c'est `git pull` depuis la racine du kit : le `.gitignore` du kit protège `os/`, `registre/` et `harnais/personnel/`. S'il a téléchargé le kit en ZIP, ce qui est le cas le plus courant, tu lui demandes de télécharger le nouveau ZIP de la même façon (bouton « Code », puis « Download ZIP ») et de le décompresser dans le dossier du kit, sous le nom `nouvelle-version/`, à côté de `harnais/` : c'est le seul endroit où tu peux le lire, puisque tu ne vois que le dossier qu'il t'a ouvert. Puis tu copies les fichiers de `nouvelle-version/` par-dessus ceux de l'ancienne version, ceux de la base et ceux de la racine du kit, sans jamais toucher à `os/`, à `registre/` ni à `harnais/personnel/`. Une fois la copie faite et vérifiée, tu lui dis qu'il peut supprimer lui-même le dossier `nouvelle-version/`, puisque tu ne supprimes rien ; le `.gitignore` du kit l'exclut en attendant. Dans l'édition entreprise, le commercial te montre où est l'archive ou le dossier que LABK lui a remis, et tu copies la nouvelle base par-dessus l'ancienne, dossier par dossier, sans toucher à `personnel/` ni à `../os/`. Tu ne supprimes rien : un fichier de l'ancienne base absent de la nouvelle reste dans la copie de sauvegarde, et tu le signales.
4. Tu lis dans le nouveau `JOURNAL.md` les lignes des versions plus récentes que la sienne.
5. Dans le kit gratuit, le dépôt contient aussi le gabarit de l'OS, dans `../os-gabarit/`. Si la nouvelle version y ajoute un fichier qui n'existe pas encore dans `../os/`, tu proposes de le copier ; tu ne remplaces jamais un fichier de `../os/` que la personne a rempli.
6. Tu compares la version de l'OS (en bas de `../os/00-sommaire.md`) à celle que la nouvelle base demande (la ligne « Le harnais vX demande le gabarit de l'OS vY » du nouveau `JOURNAL.md`). Si l'OS est plus ancien, dans une équipe, tu ne le modifies pas : tu dis au commercial ce qui, faute de la bonne version, retombe sur une valeur par défaut, et tu proposes un constat du terrain pour que la personne autorisée de l'entreprise le mette à jour avec LABK. Chez celui qui vend seul, la personne autorisée, c'est lui : tu lui montres les lignes « ce qui change pour l'existant » de `../os-gabarit/JOURNAL.md`, et tu les reportes avec lui dans son OS, sur son go, sans écraser ce qu'il a écrit, puis tu mets à jour le numéro de version en bas de son sommaire et tu ajoutes la ligne au journal des changements de ce sommaire.
7. Tu lui expliques en deux lignes ce qui change pour lui.
8. Tu fais avec lui ce que disent les lignes « ce qui change pour l'existant », une à une. Ce qui touche sa partie personnelle se fait selon les règles de `CLAUDE.md` (une règle personnelle se cite et s'inscrit avec lui). Tu n'écris rien dans le CRM pour la migration : quand une nouvelle règle change le diagnostic d'une affaire, tu le dis au commercial avec la question qui permettra de compléter la donnée au prochain échange. Tu ne réécris jamais le passé.
9. Tu notes dans `personnel/journal.md` la date, la version installée, et ce qui reste à faire.

## 3. Quand la nouvelle version contredit une règle personnelle

Si une règle nouvelle de la base contredit une règle de `personnel/regles-personnelles.md`, c'est la règle du commercial qui garde la main. Tu lui signales la nouveauté une fois, sans bloquer.

## 4. Revenir en arrière

Si une version ne lui convient pas, tu peux revenir à la précédente : `git checkout` sur l'étiquette ou le commit de la version voulue, ou, sans git, la copie de `personnel/sauvegardes/base-v<version>/` remise à sa place. Tu le notes dans `personnel/journal.md` avec la raison, pour que LABK le sache.

## 5. Signaler une version

Au point du matin, si tu sais qu'une version plus récente existe, tu le dis en une ligne. Tu ne l'installes jamais seul.
