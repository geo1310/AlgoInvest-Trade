## Configuration de l'environnement

### Installation et activation de l'environnement Virtuel
Ouvrez un nouveau terminal et taper  
```
python -m venv .venv-projet7
```
Selectionner l'environnement virtuel dans visual studio code ou l'activer en se plaçant dans le dossier **.venv-projet7/scripts** et taper
```
./activate
```
Installer les dependances necessaires au projet
```
pip install -r requirements.txt
```

---

### Procédure en cas de restriction de sécurité sur le lancement des scripts

Sous Windows ouvrez PowerShell en mode Admin, tapez la commande suivante pour afficher la politique d'exécution actuelle :
```
Get-ExecutionPolicy
```

Vous pouvez modifier la politique d'exécution en utilisant la commande Set-ExecutionPolicy. Par exemple, pour permettre l'exécution de scripts locaux (ce qui est généralement sûr), vous pouvez définir la politique d'exécution sur "RemoteSigned". Tapez la commande suivante :
```
Set-ExecutionPolicy RemoteSigned
```

Vous pouvez également définir la politique sur "Bypass" pour permettre l'exécution de tous les scripts sans restriction, mais cela comporte des risques de sécurité. Utilisez cette option avec prudence.

---



# Lancement et Fonctionnement de l'Application

## AlgoInvest&Trade

Algorithmes qui d'aprés une liste d'actions comportant pour chacunes le nom , le prix et le profit, fait ressortir une liste d'actions avec un profit maximum pour un portefeuille donné ( 500€ par défaut ) en ne pouvant prendre qu'une unité par action.

Plusieurs méthodes sont utilisées :

Les méthodes utilisent deux modules communs :

* `display.py` pour l'affichage des résultats
* `performances.py` pour le calcul des performances

### 1.  **Force Brute :** 
Toutes les combinaisons d'actions sont calculées afin de faire ressortir la meilleure.

### Usage : `bruteforce.py`

Dans ce script on peut régler deux variables

* `amount` : la valeur du portefeuille
* `datas_actions_file` : le fichier csv contenant la liste des actions à analysées ( les fichiers csv doivent etre placés dans le dossier data du projet)

Ce script execute deux fonctions : 

1. `itertools_brute_force(amount: float, actions_list: list)`

    Calcule toutes les combinaisons possibles en utilisant la fonction `combinations` du module `itertools`, qui génère toutes les combinaisons possibles d'une séquence avec une longueur donnée.

2. `recursive_brute_force(amount: float, actions_list: list, actions_selection: list = None)`

    Calcule toutes les combinaisons possibles en utilisant la récursivité

```bash
python bruteforce.py  # ou python3 bruteforce.py
```

Aprés lancement du script la console affiche le résultat pour les deux fonctions, le temps d'execution de chaque fonction ainsi que l'utilisation de la memoire et la charge CPU.




### 2. **Programmation Dynamique :** 
Une matrice est crée, comprenant d'une part toutes les valeurs possibles du portefeuille de 0 au max et d'autre part une ligne pour chaque action de la liste en commencant par 0 action.
le but étant de construire la solution petit à petit pour chaque valeur de Portefeuille et en maximisant les valeurs d'actions pouvant y etre insérée par rapport à la ligne precedente.
Avec cette méthode on uitlise les calculs deja effectués des lignes precedentes augmentant ainsi les performances.
La derniere case de la matrice representant la solution optimale.

### Usage : `optimized.py`

Dans ce script on peut régler deux variables

* `amount` : la valeur du portefeuille
* `datas_actions_file` : le fichier csv contenant la liste des actions à analysées ( les fichiers csv doivent etre placés dans le dossier data du projet)

Ce script execute la fonction : 

1. `dynamic_method(amount: float, actions_list: list, type: int)`

La fonction est lancée deux fois avec un type different :

1. Type 1 : on garde la précision des prix d'actions ( 2 décimales )
    amount et toutes les valeurs sont multipliées par 100 afin d'assurer le bon fonctionnement de la matrice et de l'indexage ( nombres entiers).

2. Type 2 : on garde l'amount et on arrondi les prix d'actions au nombre entier le plus proche.


```bash
python optimized.py  # ou python3 optimized.py
```

Aprés lancement du script la console affiche le résultat pour les deux types de calculs, le temps d'execution ainsi que la charge mémoire et la charge CPU.

---- 

### Vérification du Code : 

#### Procédure pour générer un rapport flake8 en HTML


Dans le terminal dans le dossier du projet , tapez la commande suivante pour afficher la politique d'exécution actuelle :
```
flake8 --format=html --htmldir=rapports_flake8 --exclude=.venv-projet4
```
Le rapport sera sauvegardé dans le dossier rapports_flake8, il suffira de lancer le fichier index.html


