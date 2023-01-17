import streamlit as st
import pickle
import pandas as pd
import numpy as np


# Charger le modèle depuis le fichier
with open("model.pkl", 'rb') as file:
    model_lr = pickle.load(file)





col1, mid, col2 = st.columns([1,1,20])
with col1:
    st.image('/home/apprenant/Bureau/Brief-ML-Assurance/logo-assur-aimant.jpeg', width=60)
with col2:
    st.title("Assur'Aimant")

st.subheader("Faites votre devis d'assurance en 2 minutes !")

# Ajout d'une image
st.image(image = "/home/apprenant/Bureau/Brief-ML-Assurance/Assuraimant.jpeg", width=550)


# Demande des informations à l'utilisateur
age = st.number_input("Quel est votre âge?", min_value=18, max_value=120)
sexe = st.radio("Quel est votre sexe?", ("Homme", "Femme"))
if sexe == "Homme":
        sexe = "male"
elif sexe == "Femme":
        sexe = "femelle"
bmi = st.number_input("Quel est votre IMC?", min_value=0.0, max_value=50.0)
nombre_enfants = st.number_input("Combien avez-vous d'enfants?", min_value=0, max_value=20)
fumeur = st.radio("Êtes-vous fumeur?", ("Oui", "Non"))
if fumeur == "Oui":
        fumeur = "yes"
elif fumeur == "Non":
        fumeur = "no"
region = st.selectbox("Quelle est votre région?", ["northeast", "northwest", "southeast", "southwest"])



liste = [int(age), sexe, float(bmi), int(nombre_enfants), fumeur, region]

liste_col = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

if st.button("Démarrez l'estimation"):
    df = pd.DataFrame(np.array(liste).reshape(1, -1),columns = liste_col)

    charges = int(model_lr.predict(df))
    st.success("Votre estimation de prime d'assurance est de {} $".format(charges))