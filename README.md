# Automatisation des Réponses pour Kahoot avec Selenium

Cette application permet d'automatiser la participation et la collecte de réponses à des questionnaires Kahoot à l'aide de Selenium pour gagné 1k poing à chaque réponse. Elle se compose de deux scripts principaux :
1. **Script de collecte des réponses** : Enregistre les questions et réponses dans un fichier JSON (`information.json`).
2. **Script de participation automatisée** : Utilise les réponses préenregistrées pour participer automatiquement à un questionnaire.

---

## Fonctionnalités principales

### Collecte des réponses
- Enregistrement des questions et des réponses à partir d'un lien Kahoot.
- Création automatique d'un fichier `information.json` contenant les données.
- Gestion de plusieurs questionnaires (chaque lien est une clé unique dans le fichier JSON).

### Participation automatisée
- Connexion automatique à Kahoot avec un pseudo généré.
- Réponses aux questions en fonction des données préenregistrées dans `information.json`.
- Prise en charge des questions de type :
  - Choix multiple.
  - Vrai/Faux.

### Gestion multi-utilisateurs
- Génère des pseudos uniques pour chaque utilisateur.
- Permet de simuler plusieurs utilisateurs participant simultanément.

---

## Prérequis

1. **Python 3.10 ou supérieur**
2. **Google Chrome installé**
3. **Chromedriver correspondant à votre version de Chrome**
4. **Bibliothèques nécessaires** :
   - `selenium`
   - `json`
   - `os`

Installez les dépendances avec :
```bash
pip install selenium

