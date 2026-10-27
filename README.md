# 🐦 Flappy Bird — IA par réseau de neurones

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-5A9A28)
![Type](https://img.shields.io/badge/Projet-Jeu%20%2B%20IA-blueviolet)
![Licence](https://img.shields.io/badge/Licence-MIT-informational)

Un clone du jeu **Flappy Bird** développé en Python avec Pygame, doublé d'une **intelligence artificielle** : un petit réseau de neurones décide, à chaque instant, si l'oiseau doit battre des ailes ou se laisser tomber. Le réseau est aussi **dessiné en direct à l'écran**, ce qui rend visible son fonctionnement interne.

Deux modes sont disponibles : jouer soi-même au clavier, ou laisser l'IA chercher, de tentative en tentative, une configuration qui lui permet de franchir les tuyaux.

---

## 📑 Sommaire

1. [Le concept](#-le-concept)
2. [Aperçu du fonctionnement](#-aperçu-du-fonctionnement)
3. [L'intelligence artificielle en détail](#-lintelligence-artificielle-en-détail)
4. [Structure du projet](#-structure-du-projet)
5. [Prérequis et installation](#-prérequis-et-installation)
6. [Lancer le jeu](#-lancer-le-jeu)
7. [Commandes](#-commandes)
8. [Pistes d'amélioration](#-pistes-damélioration)
9. [Auteur](#-auteur)

---

## 🎯 Le concept

Dans Flappy Bird, un oiseau avance tout seul et le joueur ne peut faire qu'une chose : lui faire battre des ailes pour monter, sinon la gravité le fait descendre. Le but est de passer entre des tuyaux sans les toucher. C'est un jeu simple en apparence, mais difficile à maîtriser, ce qui en fait un **terrain de jeu idéal pour une IA**.

Ce projet reconstruit le jeu de A à Z, puis branche à la place du joueur un **réseau de neurones** : à partir de la position de l'oiseau et de celle du prochain tuyau, le réseau choisit à chaque image s'il faut sauter. L'ensemble du réseau — ses entrées, ses neurones et sa sortie — est affiché dans le jeu, ce qui en fait autant un outil pédagogique qu'un jeu.

---

## 🎬 Aperçu du fonctionnement

À chaque instant, le programme mesure trois distances entre l'oiseau et le prochain tuyau :

- **dx** : distance horizontale jusqu'au tuyau ;
- **dy1** : distance verticale par rapport au tuyau du haut ;
- **dy2** : distance verticale par rapport au tuyau du bas.

Ces trois nombres sont les **entrées** du réseau de neurones. Le réseau produit une **sortie** entre 0 et 1 : si elle est inférieure à 0,5, l'oiseau bat des ailes ; sinon, il tombe. Des lignes de couleur tracées à l'écran relient l'oiseau au tuyau pour visualiser ces distances, et le réseau lui-même est dessiné à côté du jeu.

Le programme tient aussi le compte des **générations** (chaque mort fait repartir une nouvelle tentative), du **score** courant et du **record**, et met en évidence le « meilleur oiseau » obtenu jusque-là.

---

## 🧠 L'intelligence artificielle en détail

Le cœur du projet se trouve dans `game_code/neural_network.py`. Il s'agit d'un réseau de neurones **entièrement codé à la main**, sans aucune bibliothèque de machine learning.

### Architecture : 3 → 4 → 1

```
   Entrées            Couche cachée          Sortie
  (3 neurones)        (4 neurones)         (1 neurone)

   dx  ●──────────────────● h0 ──┐
        ╲ ╳ ╱              ● h1 ──┤
  dy1  ●──────────────────● h2 ──┼──────────● sortie → saut ?
        ╱ ╳ ╲              ● h3 ──┘
   dy2 ●──────────────────┘
```

- **3 neurones d'entrée** : `dx`, `dy1`, `dy2`.
- **4 neurones cachés** : chacun calcule une somme pondérée des trois entrées, à laquelle on applique une fonction **sigmoïde** pour obtenir une valeur entre 0 et 1.
- **1 neurone de sortie** : combine les quatre neurones cachés, repasse par une sigmoïde, et donne la décision finale.

Au total, le réseau utilise **16 poids** (12 entre l'entrée et la couche cachée, 4 entre la couche cachée et la sortie). Ce sont ces poids qui déterminent le comportement de l'oiseau.

### Comment l'IA « apprend »

Il est important d'être transparent sur la méthode employée, qui n'est pas celle d'un réseau de neurones classique :

- Il n'y a **pas de rétropropagation** ni de descente de gradient. Le réseau ne s'entraîne pas au sens habituel.
- À chaque mort de l'oiseau, de **nouveaux poids sont tirés au hasard** et une nouvelle tentative commence. Il s'agit donc d'une **recherche aléatoire** : on essaie des configurations jusqu'à en trouver une qui franchit des tuyaux.
- Dès qu'une tentative **bat le record**, ses poids et sa génération sont mémorisés et mis en avant comme « meilleur oiseau ».

En résumé, le programme explore l'espace des poids par essais successifs et conserve la meilleure trouvaille. C'est une approche simple et visuelle, qui montre bien le lien entre les poids d'un réseau et le comportement qui en résulte, même si elle ne constitue pas un apprentissage par gradient. Des pistes pour aller vers un vrai algorithme d'optimisation (génétique) sont proposées [plus bas](#-pistes-damélioration).

---

## 📂 Structure du projet

```
Flappy_Bird-AI-neural-network/
├── FlappyBird.py                  # Programme principal : boucle de jeu, physique, collisions, score
├── game_code/
│   ├── neural_network.py          # Le réseau de neurones (3→4→1) et son affichage
│   ├── bird.py                    # L'oiseau, ses sprites, le choix du mode (clavier/IA) au lancement
│   ├── pipes.py                   # Les tuyaux et leur déplacement
│   ├── background.py              # Fond, textes, affichage du score et du « meilleur oiseau »
│   ├── colors_background.py       # Définition des couleurs
│   └── sounds.py                  # Chargement des effets sonores
├── sprites/                       # Images : oiseaux de 10 couleurs, tuyaux, arrière-plan
├── sounds/                        # Effets sonores : battement d'ailes, point, collision, record
└── fonts/                         # Police d'affichage
```

**Flux général :** `FlappyBird.py` lance la boucle de jeu. À chaque image, il met à jour la physique de l'oiseau (saut / gravité) et des tuyaux, calcule les trois distances `dx`, `dy1`, `dy2`, puis — en mode IA — les transmet au réseau de `neural_network.py` qui renvoie la décision. Les collisions font mourir l'oiseau, incrémentent le compteur de générations et relancent une tentative. Tout est dessiné à l'écran, réseau de neurones compris.

---

## 🛠 Prérequis et installation

- **Python 3** (testé avec Python 3.8 et versions ultérieures).
- La bibliothèque **Pygame**.

### Installation

```bash
# 1. Récupérer le projet
git clone https://github.com/hugorako947/Flappy_Bird-AI-neural-network.git
cd Flappy_Bird-AI-neural-network

# 2. (Recommandé) créer un environnement virtuel
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

# 3. Installer Pygame
pip install pygame
```

---

## ▶ Lancer le jeu

> [!IMPORTANT]
> Lancez toujours le programme **depuis la racine du projet**, car les images, sons et polices sont chargés par des chemins relatifs (`sprites/…`, `sounds/…`, `fonts/…`). Exécuter le script depuis un autre dossier provoque une erreur de fichier introuvable.

```bash
python FlappyBird.py
```

Au démarrage, deux questions sont posées **dans le terminal** (et non dans la fenêtre de jeu) :

1. **`manual or AI ? (m/ai) :`**
   - `m` : vous jouez vous-même au clavier.
   - `ai` : le réseau de neurones prend les commandes.
2. **`show results ? (Y/N) :`**
   - `Y` : les poids du meilleur réseau et les scores sont affichés dans le terminal au fil des records.
   - `N` : affichage silencieux.

La fenêtre de jeu s'ouvre ensuite.

---

## 🎮 Commandes

| Touche / action | Effet |
|---|---|
| **Flèche du haut** | Faire battre des ailes à l'oiseau (mode manuel `m` uniquement) |
| **Échap** | Quitter le jeu |
| **Fermer la fenêtre** | Quitter le jeu |

En mode IA, il n'y a rien à faire : il suffit de regarder l'oiseau tenter sa chance, tentative après tentative, et le réseau de neurones réagir en direct à l'écran.

---

## 💡 Pistes d'amélioration

- **Passer à un véritable algorithme génétique** : faire évoluer plusieurs oiseaux en parallèle, sélectionner les meilleurs et croiser / muter leurs poids, au lieu de tirer de nouveaux poids entièrement au hasard à chaque mort. L'IA progresserait alors réellement de génération en génération.
- **Initialiser les 16 poids indépendamment** : actuellement, une même valeur aléatoire est répétée sur les 16 poids à chaque réinitialisation (`[valeur] * 16`), ce qui réduit fortement la diversité explorée. Tirer chaque poids séparément élargirait la recherche.
- **Simuler plusieurs oiseaux simultanément** pour accélérer la découverte d'une bonne configuration.
- **Sauvegarder le meilleur réseau** dans un fichier pour le recharger sans tout recommencer.
- **Déplacer les questions de mode** depuis le terminal vers un menu dans la fenêtre de jeu, pour une expérience plus fluide.
- Ajouter un fichier `requirements.txt` (`pygame`) pour simplifier l'installation.

---

## 👤 Auteur

Projet réalisé par **Hugo Rakotonanahary** — [@hugorako947](https://github.com/hugorako947)

Un projet qui réunit développement de jeu vidéo (Pygame : physique, collisions, sprites, sons) et intelligence artificielle, avec un réseau de neurones codé à la main et visualisé en temps réel.
