# Inclusion Financière en Afrique

## Contexte du projet

Ce projet porte sur l'inclusion financière en Afrique de l’Est. L'objectif est d'identifier quelles personnes sont les plus susceptibles de posséder ou d'utiliser un compte bancaire, à partir de données démographiques et financières. L’inclusion financière permet aux individus et aux entreprises d’accéder à des services financiers utiles et abordables (transactions, paiements, épargne, crédit, assurance) de manière responsable et durable.

---

## Contenu du projet

- `sample_1000.csv` : échantillon du dataset original (1 000 lignes pour tests rapides)  
- `app.py` : application Streamlit permettant de faire des prédictions en local  
- `model.pkl` : modèle RandomForest entraîné sur l’échantillon  
- `.gitignore` : pour exclure les fichiers volumineux et l’environnement virtuel  

---

## Dataset

- Nom : `Financial_inclusion_dataset.csv`  
- Taille originale : 23 525 lignes  
- Colonnes principales :
  - Données démographiques : âge, genre, région, état matrimonial, etc.  
  - Données financières : possession de compte bancaire, type de services utilisés, épargne, crédit, assurance  
  - Target : indicateur d’inclusion financière (`target`)  

---

## Prétraitement et nettoyage

- Gestion des valeurs manquantes : remplacement par la médiane pour les colonnes numériques et par le mode pour les colonnes catégorielles  
- Encodage des variables catégorielles avec `LabelEncoder`  
- Possibilité de supprimer les doublons et de gérer les valeurs aberrantes si nécessaire  

---

## Modèle de Machine Learning

- Algorithme utilisé : RandomForestClassifier  
- Données : échantillon `sample_1000.csv`  
- Séparation train/test : 80/20  
- Le modèle est sauvegardé avec `joblib` (`model.pkl`)  
- Permet de prédire la probabilité qu’une personne soit incluse financièrement  

---

## Application Streamlit

L’application permet de :

1. Saisir les informations d’un individu via un formulaire  
2. Cliquer sur “Prédire” pour obtenir le résultat  

Pour lancer l’application en local :

\`\`\`bash
source venv/bin/activate
streamlit run app.py
\`\`\`

---

## Visualisation et profilage

Il est possible de générer un rapport de profilage complet avec `pandas-profiling` :

\`\`\`python
from pandas_profiling import ProfileReport
import pandas as pd

df = pd.read_csv("sample_1000.csv")
profile = ProfileReport(df, title="Profilage du dataset Inclusion Financière")
profile.to_file("profiling_report.html")
\`\`\`

---

## Déploiement

- Dépôt GitHub : [https://github.com/bulba-1984/structure-projet-Financial-Inclusion](https://github.com/bulba-1984/structure-projet-Financial-Inclusion)  
- L’application peut être déployée sur Streamlit Cloud pour un accès en ligne  

---

## Instructions pour contribuer

1. Cloner le dépôt
2. Créer un environnement virtuel :

\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

3. Installer les dépendances :

\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Ajouter vos scripts, modèles ou analyses, puis committer :

\`\`\`bash
git add .
git commit -m "Description de vos changements"
git push
\`\`\`

---

## Auteur

YFZ 2025 Bulba
