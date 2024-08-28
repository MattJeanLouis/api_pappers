# API Pappers - Recherche et Détails d'Entreprises

Ce projet démontre l'utilisation de deux API Pappers distinctes pour la recherche et l'obtention de détails sur les entreprises françaises.

## Les API Pappers

1. **API de Recherche d'Entreprises**
   - Objectif : Permet de rechercher des entreprises selon divers critères (nom, SIREN, code postal, etc.).
   - Utilisation : Idéale pour trouver rapidement une liste d'entreprises correspondant à des critères spécifiques.
   - Exemple d'utilisation : Rechercher toutes les boulangeries dans une ville donnée.

2. **API de Détails d'Entreprise**
   - Objectif : Fournit des informations détaillées sur une entreprise spécifique à partir de son numéro SIREN.
   - Utilisation : Parfaite pour obtenir des données complètes sur une entreprise particulière.
   - Exemple d'utilisation : Obtenir les états financiers, les dirigeants et l'historique d'une entreprise.

## Cibles de recherche pour l'API Pappers

L'API de recherche de Pappers permet de cibler différents aspects des entreprises lors de la recherche. Les principales cibles sont :

1. **nom_entreprise** : Recherche dans le nom officiel de l'entreprise.
2. **siren** : Recherche par numéro SIREN (9 chiffres).
3. **siret** : Recherche par numéro SIRET (14 chiffres).
4. **dirigeant** : Recherche dans les noms des dirigeants de l'entreprise.
5. **marque** : Recherche dans les noms de marques déposées par l'entreprise.
6. **denomination** : Recherche dans la dénomination usuelle de l'entreprise.
7. **nom_complet** : Recherche dans le nom complet de l'entreprise (incluant la forme juridique).
8. **siege** : Recherche dans l'adresse du siège social.
9. **etablissement** : Recherche dans les adresses de tous les établissements.
10. **representant** : Recherche dans les noms des représentants légaux.
11. **convention_collective** : Recherche dans les conventions collectives.
12. **objet_social** : Recherche dans l'objet social de l'entreprise.

Pour utiliser plusieurs cibles dans une recherche, vous pouvez les séparer par des virgules. Par exemple :

```python
cibles = "nom_entreprise,siren,dirigeant"
````

## Prérequis

- Python 3.9 ou supérieur
- Docker (optionnel)

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre-nom/api-pappers-recherche.git
   cd api-pappers-recherche
   ```

2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

3. Créez un fichier `.env` à la racine du projet et ajoutez votre token API Pappers :
   ```
   API_TOKEN=votre_token_api_pappers
   ```

## Utilisation

### Recherche d'entreprises

Exécutez le script `recherche_entreprises.py` :

```python
python recherche_entreprises.py
````

Suivez les instructions pour effectuer une recherche d'entreprises.

### Détails d'une entreprise

Exécutez le script `details_entreprise.py` :

```python
python details_entreprise.py
`````
Entrez le numéro SIREN de l'entreprise dont vous souhaitez obtenir les détails.

## Utilisation avec Docker

1. Construisez l'image Docker :
   ```
   docker build -t api-pappers-recherche .
   ```

2. Exécutez le conteneur :
   ```
   docker run -it --rm api-pappers-recherche
   ```

## Structure du projet

- `recherche_entreprises.py` : Script pour rechercher des entreprises
- `details_entreprise.py` : Script pour obtenir les détails d'une entreprise
- `requirements.txt` : Liste des dépendances Python
- `Dockerfile` : Configuration pour créer une image Docker du projet
