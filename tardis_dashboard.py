import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.set_page_config(page_title="Tardis Dashboard", layout="wide")


def load_css():
    st.markdown(
        """
    <style>
    .stApp {
        background-color: black;
    h1 {
        color : #464869;
    }
    h3 {
        color : #9295BC;
    }
    p { border : solid;
        border-color : #1C1C26;
        padding : 20px;
        background-color : #09090B;
        border-radius : 10px;
    }
    .stMainBlockContainer {
        width : 100%;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


load_css()

df = pd.read_csv(
    "/home/aurelie/Bureau/sncf/B-DAT-200-TLS-2-1-tardis-6/cleaned_dataset.csv"
)
st.title("Tardis Dashboard")
col_left, col_right = st.columns([2, 1])
col_left2, col_right2 = st.columns([1, 1])

with col_left:
    with st.container(border=True):
        st.subheader("Trafic des trains", divider="gray")
        st.write("Statistiques")
        st.write("Statistiques")

with col_right:
    with st.container(border=True):
        st.subheader("Statistique", divider="gray")
        st.write(
            "Retard moyen : "
            + str(df["Retard moyen de tous les trains au départ"].mean())
            + " minutes",
        )
        st.write("Total des trains : " + str(len(df)))
        st.write(
            "Pourcentage des trains à l'heure : "
            + str(
                (df["Retard moyen de tous les trains au départ"] == 0).sum()
                / len(df["Retard moyen de tous les trains au départ"])
                * 100
            )
            + "%",
        )

with st.container(border=True):
    st.subheader("Delay Prediction", divider="gray")
    
    options = st.multiselect(
        "Gare de départ",
        [d for d in df["Gare de départ"].unique()],
        max_selections=1,
    )
    options = st.multiselect(
        "Gare d'arrivée",
        [d for d in df["Gare d'arrivée"].unique()],
        max_selections=1,
    )
    options = st.multiselect(
        "Month",
        [d for d in df["Month"].unique()],
        max_selections=1,
    )
    if st.button("Prédire"):
        st.toast("Tes prédictions sont prêtes!", icon="🎉")