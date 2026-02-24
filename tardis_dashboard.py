import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("/home/aurelie/Bureau/sncf/B-DAT-200-TLS-2-1-tardis-6/cleaned_dataset.csv")
st.title("Tardis Dashboard")

container = st.container(border=True)
container.header("Trafique des trains", divider="gray")
container.subheader("Statistique", divider="gray")
container.subheader("Statistique", divider="gray")


container2 = st.container(border=True)
container2.header("Statistique", divider="gray")
container2.subheader("Retard moyen : ", divider="gray")
container2.subheader("Total des trains : " + str(len(df)), divider="gray")
container2.subheader("Pourcentage des trains à l'heure :", divider="gray")


container3 = st.container(border=True)
container3.subheader("Delay Prediction", divider="gray")

if st.button("Validate"):
    st.toast("Your prediction is ready!", icon="🎉")

if st.button("Send balloons!"):
    st.balloons()
    
st.snow()