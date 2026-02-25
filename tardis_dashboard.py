import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Tardis Dashboard", layout="wide")


@st.cache_resource
def load_model():
    model = joblib.load("model.joblib")
    le_service = joblib.load("encoder_service.joblib")
    le_dep = joblib.load("encoder_gare_dep.joblib")
    le_arr = joblib.load("encoder_gare_arr.joblib")
    features = joblib.load("features_list.joblib")

    return model, le_service, le_dep, le_arr, features


model, le_service, le_dep, le_arr, features = load_model()


def load_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: black;
        }
        h1 {
            color: #464869;
        }
        h3 {
            color: #9295BC;
        }
        p {
            border: solid;
            border-color: #1C1C26;
            padding: 20px;
            background-color: #09090B;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


load_css()


df = pd.read_csv("cleaned_dataset.csv")

st.title("Tardis Dashboard - Prédiction Retards SNCF")

st.subheader("Statistiques Générales")

col_left, col_right = st.columns([1, 1])

with col_left:
    with st.container(border=True):
        st.write("Distribution des retards au départ")
        plt.figure(figsize=(10, 3))
        sns.histplot(
            df["Retard moyen de tous les trains au départ"],
            bins=20,
            kde=True,
            color="skyblue",
        )
        plt.title("Distribution des retards moyens au départ")
        plt.xlabel("Retard moyen (minutes)")
        plt.ylabel("Nombre de trajets")
        st.pyplot(plt.gcf())
        plt.close()

with col_right:
    with st.container(border=True):
        st.write("Top 10 gares avec le plus de retards")
        plt.figure(figsize=(10, 4))

        top_gare = (
            df.groupby("Gare de départ")["Retard moyen de tous les trains au départ"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

        sns.barplot(x=top_gare.index, y=top_gare.values, palette="magma")
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Retard moyen (minutes)")
        plt.title("Top 10 des gares avec retards élevés")
        st.pyplot(plt.gcf())
        plt.close()


st.write("---")
st.subheader("Prédire un retard")

with st.container(border=True):
    col1, col2 = st.columns([1, 1])

    with col1:
        service = st.selectbox(
            "Service", df["Service"].unique(), help="Type de service"
        )

        gare_dep = st.selectbox(
            "Gare de départ",
            sorted(df["Gare de départ"].unique()),
            help="Sélectionnez la gare de départ",
        )

        duree = st.slider(
            "Durée moyenne du trajet (minutes)",
            min_value=int(df["Durée moyenne du trajet"].min()),
            max_value=int(df["Durée moyenne du trajet"].max()),
            value=141,
            step=5,
        )

    with col2:
        gare_arr = st.selectbox(
            "Gare d'arrivée",
            sorted(df["Gare d'arrivée"].unique()),
            help="Sélectionnez la gare d'arrivée",
        )

        nb_annules = st.slider(
            "Nombre de trains annulés",
            min_value=0,
            max_value=int(df["Nombre de trains annulés"].max()),
            value=2,
            step=1,
        )

        nb_retard_15 = st.slider(
            "Nombre de trains en retard > 15min",
            min_value=0,
            max_value=int(df["Nombre trains en retard > 15min"].max()),
            value=10,
            step=1,
        )

    nb_retard_30 = st.slider(
        "Nombre de trains en retard > 30min",
        min_value=0,
        max_value=int(df["Nombre trains en retard > 30min"].max()),
        value=5,
        step=1,
    )

    nb_retard_60 = st.slider(
        "Nombre de trains en retard > 60min",
        min_value=0,
        max_value=int(df["Nombre trains en retard > 60min"].max()),
        value=1,
        step=1,
    )
    mois = st.slider("Mois", min_value=1, max_value=12, value=3, step=1, format="%d")

    if st.button(" PRÉDIRE LE RETARD", use_container_width=True):
        try:
            service_enc = le_service.transform([service])[0]
            gare_dep_enc = le_dep.transform([gare_dep])[0]
            gare_arr_enc = le_arr.transform([gare_arr])[0]

            X = pd.DataFrame(
                [
                    [
                        2026,
                        mois,
                        service_enc,
                        gare_dep_enc,
                        gare_arr_enc,
                        duree,
                        nb_annules,
                        nb_retard_15,
                        nb_retard_30,
                        nb_retard_60,
                    ]
                ],
                columns=features,
            )

            prediction = model.predict(X)[0]

            col_result1, col_result2 = st.columns([2, 1])

            with col_result1:
                st.metric("RETARD ESTIMÉ", f"{prediction:.1f} minutes")

        except Exception as e:
            st.error(f"Erreur: {str(e)}")
