import streamlit as st
import plotly.express as px

from database import init_db,insert_data,load_data
from recommender import recommend
from analytics import dataframe
from ml_model import train

from lunar_cycles import get_moon_phase
from tides import tide_recommendation
from weather import get_weather

init_db()

st.title("🌊 Ancestral Surf AI")

st.subheader("Condiciones naturales")

st.write("Fase lunar:",get_moon_phase())

st.write("Clima:",get_weather())

st.subheader("Registra tu día")

energy=st.slider("Energía",1,10)

mood=st.slider("Ánimo",1,10)

stress=st.slider("Estrés",1,10)

sleep=st.slider("Sueño",0,12)

surf=st.slider("Horas surf",0,5)

fishing=st.slider("Horas pesca",0,8)

cannabis=st.slider("Cannabis",0,5)

food=st.slider("Calidad comida",1,10)

notes=st.text_area("Notas")

if st.button("Guardar"):

    insert_data((energy,mood,stress,sleep,surf,cannabis,fishing,food,notes))

    st.success("Datos guardados")

rows=load_data()

if rows:

    df=dataframe(rows)

    st.subheader("Evolución energía")

    fig=px.line(df,y="energy")

    st.plotly_chart(fig)

    st.subheader("Recomendaciones")

    rec=recommend(energy,stress,mood)

    for r in rec:
        st.write("•",r)

    st.subheader("IA aprendiendo")

    model=train(df)

    if model:

        pred=model.predict([[sleep,surf,cannabis,fishing,food]])

        st.write("Predicción energía:",round(pred[0],2))

    st.subheader("Consejos mar")

    for t in tide_recommendation():

        st.write("•",t)
