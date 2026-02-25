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
        plt.figure(figsize=(10, 3))
        sns.histplot(
            df["Retard moyen de tous les trains au départ"], bins=2, kde=True, color="skyblue"
        )
        plt.title("Distribution des retards moyens au départ")
        plt.xlabel("Retard moyen (minutes)")
        plt.ylabel("Nombre de trains")
        st.pyplot(plt.gcf())
        plt.close()
        st.write("Statistiques")
        plt.figure(figsize=(10, 5))
        top_gare_retard = (
            df.groupby("Gare de départ")["Retard moyen de tous les trains au départ"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

        sns.barplot(x=top_gare_retard.index, y=top_gare_retard.values, palette="magma")
        plt.xticks(rotation=45)
        plt.ylabel("Retard moyen (minutes)")
        plt.title("Top 10 des gares avec les retards les plus élevés au départ")
        st.pyplot(plt.gcf())
        plt.close()

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
    
    départ = st.multiselect(
        "Gare de départ",
        [d for d in df["Gare de départ"].unique()],
        max_selections=1,
    )
    arrivée = st.multiselect(
        "Gare d'arrivée",
        [d for d in df["Gare d'arrivée"].unique()],
        max_selections=1,
    )
    mois = st.multiselect(
        "Mois",
        [n for n in df["Month"].unique()],
        max_selections=1,
    )
    year = st.multiselect(
        "Année",
        [2026, 2027, 2028, 2029, 2030],
        max_selections=1,
    )
    service = st.multiselect(
        "Service",
        [d for d in df["Service"].unique()],
        max_selections=1,
    )
    nb_trains_annules = st.multiselect(
        "Nombre de trains annulés",
        [d for d in df["Nombre de trains annulés"].unique()],
        max_selections=1,
        default=2
    )
    nb_retard_15 = st.multiselect(
        "Nombre de trains en retard de plus de 15 minutes",
        [d for d in df["Nombre trains en retard > 15min"].unique()],
        max_selections=1,
        default=10
    )
    nb_retard_30 = st.multiselect(
        "Nombre de trains en retard de plus de 30 minutes",
        [d for d in df["Nombre trains en retard > 30min"].unique()],
        max_selections=1,
        default=10
    )
    nb_retard_60 = st.multiselect(
        "Nombre de trains en retard de plus de 60 minutes",
        [d for d in df["Nombre trains en retard > 60min"].unique()],
        max_selections=1,
        default=10
    )
    if st.button("Prédire"):
        if not départ or not arrivée or not mois or not year:
            st.warning("Merci de sélectionner une gare de départ, une gare d'arrivée, un mois et une année.")
        else:
            dep = départ[0]
            arr = arrivée[0]
            m = mois[0]

            df_filtre = df[
                (df["Gare de départ"] == dep) &
                (df["Gare d'arrivée"] == arr) &
                (df["Month"] == m)
            ]

            if df_filtre.empty:
                st.error("Aucun trajet trouvé pour ce mois.")
            else:
                total_trains = df_filtre["Nombre de circulations prévues"].sum()
                trains_retard = df_filtre["Nombre de trains en retard à l'arrivée"].sum()
                trains_annules = df_filtre["Nombre de trains annulés"].sum()

                proba_retard = (trains_retard / total_trains) * 100

                st.metric(
                    "Probabilité qu'un train soit en retard",
                    f"{proba_retard:.1f} %",
                )

                st.metric(
                    "Nombre de trains analysés",
                    int(total_trains),
                )

                st.metric(
                    "Trains annulés",
                    int(trains_annules),
                )
        
        
