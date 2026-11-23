# Ce qu'il faut pour faire tourner le harnais

Le harnais est un dossier de fichiers texte, avec un petit programme en Python. Pour qu'il marche, votre outil d'IA doit savoir faire deux choses, et c'est tout.

## Les deux choses que votre IA doit savoir faire

1. **Ouvrir un dossier de votre ordinateur, y lire et y écrire.** Le harnais garde sa mémoire dans des fichiers : vos réglages, votre suivi, ce qu'il apprend. Une IA qui ne voit que ce que vous collez dans la conversation oublie tout à la fermeture.
2. **Lancer un programme Python.** La boucle d'apprentissage, qui regarde chaque semaine les conseils que vous suivez et ceux que vous écartez, est un programme de quelques centaines de lignes, sans rien à installer en plus de Python lui-même.

## Trois situations qui ne se valent pas

Une IA peut avoir accès à vos fichiers de trois façons, et seule la troisième fait vraiment tourner le harnais :

1. **Elle lit un fichier que vous lui donnez dans la conversation.** Elle peut examiner le kit, mais elle ne garde rien d'une conversation à l'autre.
2. **Elle travaille dans un dossier temporaire**, le temps d'une conversation. Elle peut décompresser le kit et lancer Python, mais tout disparaît à la fin.
3. **Elle travaille dans un dossier de votre ordinateur, qu'elle retrouve à chaque séance.** C'est ce qu'il faut au harnais : sa mémoire et votre suivi y vivent.

## Les outils, selon ce qu'ils permettent

| Ce que permet l'outil | Exemples | Ce que vous pouvez faire |
|---|---|---|
| Un dossier de votre ordinateur, retrouvé à chaque séance | Claude dans l'application sur ordinateur, avec un dossier ouvert ; Claude Code | Tout : c'est l'usage prévu, avec lequel le kit est conçu et essayé. |
| Un dossier temporaire et Python, le temps d'une conversation | ChatGPT avec un fichier joint (essai du 23/11/2026, ci-dessous) | Découvrir le kit et l'essayer. Pour s'en servir au quotidien, il faudrait lui redonner à chaque séance un zip de vos dossiers `harnais/personnel/`, `os/` et `registre/`, puis récupérer le zip mis à jour en fin de séance. C'est possible, mais lourd, et rien ne se fait sans vous. |
| Une simple fenêtre de conversation | Un assistant sans fichiers ni Python | Rien de durable : le harnais ne peut pas fonctionner. |

**Claude, dans l'application sur ordinateur.** D'après l'aide de Claude (consultée le 23/11/2026), le travail dans un dossier de votre ordinateur demande un abonnement payant, et Claude y lit et écrit seulement dans les dossiers que vous lui avez ouverts. Il y lance ses programmes dans un environnement isolé, séparé de votre ordinateur : selon la version de l'application, sur les serveurs d'Anthropic ou dans une machine virtuelle sur votre ordinateur. Vous n'avez donc pas Python à installer `[hyp : à revérifier, ces outils évoluent vite]`.

**Claude Code** sert à ceux qui travaillent dans un terminal. Là, c'est le Python de votre ordinateur qui tourne : il est souvent déjà présent sur un Mac, et il s'installe depuis python.org sur Windows.

**L'essai du 23/11/2026 avec ChatGPT.** LABK a remis le kit en zip à ChatGPT, dans une conversation, avec un fichier joint. ChatGPT a pu décompresser le kit, lire tous les fichiers, écrire dans un dossier temporaire et lancer le script Python. Il n'a pas pu travailler dans un dossier de l'ordinateur de la personne, ni garder ses fichiers d'une séance à l'autre, ni lire sa messagerie, son agenda ou un CRM. Ces outils évoluent vite : refaites l'essai avec votre propre abonnement avant de vous décider.

Un autre outil d'IA convient s'il sait faire les deux choses du début de cette page. Il n'a pas été essayé, et c'est à vous de le vérifier.

## Le test, avant de commencer

Une fois le dossier du kit ouvert dans Claude, écrivez cette phrase :

> Liste les dossiers que tu vois ici, puis lance python3 --version.

Si Claude vous répond en citant le dossier `harnais` (et, dans le kit gratuit, le dossier `os-gabarit`), puis un numéro de version qui commence par 3, tout est prêt. S'il vous dit qu'il ne voit aucun dossier, c'est que le dossier n'est pas encore ouvert dans l'application. Dans l'application de bureau, le mode qui travaille dans un dossier s'appelle aujourd'hui Cowork : ouvrez-le, puis reliez-y le dossier du kit `[hyp : le nom et le geste changent avec les versions de l'application]`. L'aide de Claude décrit le geste à jour : https://support.claude.com/en/articles/13345190

Si Claude voit le dossier mais ne lance pas Python, ou si vous préférez sauter ce test, écrivez « installe-toi » : le harnais refait ces deux vérifications au début de l'installation, essaie aussi les autres noms de Python (python, puis py sous Windows), et vous dit tout de suite ce qui manque.

## Ce qui aide, sans être obligatoire

- **Un CRM relié à votre IA** par un connecteur (MCP). Un CRM est le logiciel où l'on suit ses clients et ses affaires. Sans CRM, le harnais tient votre suivi dans le registre : deux fichiers de tableur, fournis vides avec le kit, qu'il range dans un dossier `registre` à côté du harnais. Si vous passez un jour à un CRM, le registre s'y reprend tel quel.
- **Votre messagerie et votre agenda reliés à votre IA.** Le harnais y lit ce que votre suivi ne sait pas, et, si vous l'y autorisez, il prépare vos invitations. Sans eux, vous lui collez ce qu'il doit savoir.

## Le temps à prévoir

- **Seul** : quatre à six heures au total, en séances d'environ une heure, selon le nombre de prospects à reprendre et la facilité à dire ce que vous vendez `[hyp : estimation à vérifier à la première vraie installation]`. Le harnais vous rend un premier point du matin sur vos trois affaires les plus chaudes dès la deuxième séance. Ensuite, quelques minutes par jour.
- **En équipe, avec LABK** : l'OS de l'entreprise se pose avant l'installation, avec le dirigeant, lors d'une mission d'accompagnement. Chaque commercial installe ensuite son harnais en trois séances.

## Vos données

Le harnais ne vous demande rien d'autre que ce que vous avez déjà. Ce qu'il lit et ce qu'il fait de vos données est expliqué dans `CONFIDENTIALITE.md`, dans ce même dossier.
