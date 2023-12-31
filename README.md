## Configuration de l'environnement

### Installation et activation de l'environnement Virtuel
Ouvrez un nouveau terminal et taper  
```
python -m venv .venv-projet7
```
Selectionner l'environnement virtuel dans visual studio code ou l'activer en se plaçant dans le dossier **venv-projet4/scripts** et taper
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

### Procédure pour générer un rapport flake8 en HTML


Dans le terminal dans le dossier du projet , tapez la commande suivante pour afficher la politique d'exécution actuelle :
```
flake8 --format=html --htmldir=rapports_flake8 --exclude=.venv-projet4
```
Le rapport sera sauvegardé dans le dossier rapports_flake8, il suffira de lancer le fichier index.html
# Lancement et Fonctionnement de l'Application

## AlgoInvest&Trade

## Usage

```bash
python main.py  # ou python3 main.py
```

