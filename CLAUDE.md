# Kit gratuit LABK : le harnais du commercial

Ce dossier contient deux parties, qui ne se mélangent jamais.

- `harnais/` : l'assistant de la personne qui vend. Ses instructions sont dans `harnais/CLAUDE.md` : lis-les, et suis-les. Tous les chemins qu'elles donnent se lisent depuis le dossier `harnais/`.
- `os-gabarit/` : le gabarit vide de l'OS, c'est-à-dire de la façon de vendre de la personne. Au début de l'installation, la skill `harnais/skills/installation/` le copie une seule fois vers `os/`, qui appartient ensuite à la personne et que les mises à jour ne touchent jamais.

Si `harnais/personnel/` n'existe pas, le harnais n'est pas encore installé : quand la personne écrit « installe-toi », lance la skill `harnais/skills/installation/`. Elle commence par vérifier les prérequis de `harnais/PREREQUIS.md`, et s'arrête en le disant s'ils manquent.
