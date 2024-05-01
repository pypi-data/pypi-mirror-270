# Contrôle de Maison Virtuelle avec Home IO

Ce code Python permet de contrôler une maison virtuelle via le serveur web intégré de Home IO. Il offre des fonctionnalités pour interagir avec différents éléments de la maison tels que les lumières, le chauffage, les volets et le portail.

## Installation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Clonez ce dépôt sur votre machine :
    ```bash
    git clone https://github.com/votre_utilisateur/home-io-control.git
    ```
3. Accédez au répertoire du projet :
    ```bash
    cd home-io-control
    ```
4. Installez les dépendances en exécutant :
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Avant d'utiliser le script, assurez-vous de configurer le fichier `config.yml` avec les paramètres de votre serveur Home IO.

Exemple de configuration :

```yaml
serveur_home_io: "192.168.1.100"
port_home_io: 9797
```

## Utilisation

Le script Python offre plusieurs classes pour contrôler différents appareils de la maison virtuelle :

### Lumière

```python
from controle_maison import ConnexionHomeIO, Lumiere

# Créer une connexion
connexion = ConnexionHomeIO()

# Créer une instance de lumière pour la pièce A
lumiere_A = Lumiere(connexion, "A")

# Allumer la lumière
lumiere_A.allumer()

# Éteindre la lumière
lumiere_A.eteindre()

# Régler l'intensité lumineuse
lumiere_A.regler_intensite(5)
```

### Chauffage

```python
from controle_maison import Chauffage

# Créer une instance de chauffage pour la pièce M
chauffage_M = Chauffage(connexion, "M")

# Allumer le chauffage
chauffage_M.allumer()

# Éteindre le chauffage
chauffage_M.eteindre()

# Régler la température
chauffage_M.regler_temperature(22)
```

### Volet

```python
from controle_maison import Volet

# Créer une instance de volet pour la pièce B
volet_B = Volet(connexion, "B")

# Monter le volet
volet_B.monter()

# Descendre le volet
volet_B.descendre()

# Arrêter le volet
volet_B.arreter()
```

### Portail

```python
from controle_maison import Portail

# Créer une instance de portail pour le portail d'entrée
portail_entree = Portail(connexion, "portail")

# Ouvrir le portail
portail_entree.ouvrir()

# Fermer le portail
portail_entree.fermer()
```

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request pour des améliorations ou des corrections.

## Licence

Ce projet est sous licence [GNU GPL v3](LICENSE).
```

Cela devrait vous donner un bon point de départ pour expliquer comment utiliser votre code dans un fichier README.md. Si vous avez d'autres questions ou des modifications à apporter, n'hésitez pas à demander !