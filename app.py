import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import streamlit as st

# Charger les données
df = pd.read_csv("sample_1000.csv")

# Gestion des valeurs manquantes (remplacer par mode ou mediane)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])
for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(df[col].median())

# Encoder les colonnes catégorielles
le_dict = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    le_dict[col] = le

# Séparer features et target
X = df.drop("target", axis=1, errors='ignore')
y = df["target"] if "target" in df.columns else None

# Entraîner un modèle simple
if y is not None:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    joblib.dump(clf, "model.pkl")

# Interface Streamlit
st.title("Application Inclusion Financière")
inputs = {}
for col in X.columns:
    val = st.text_input(f"Entrez {col}")
    inputs[col] = val

if st.button("Prédire"):
    input_df = pd.DataFrame([inputs])
    # Encoder les colonnes catégorielles
    for col in input_df.columns:
        if col in le_dict:
            input_df[col] = le_dict[col].transform(input_df[col])
        else:
            input_df[col] = pd.to_numeric(input_df[col])
    prediction = clf.predict(input_df)
    st.write("Prédiction : ", prediction[0])
