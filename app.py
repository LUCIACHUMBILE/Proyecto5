import pandas as pd
import streamlit as st
import plotly_express as px
data = pd.read_csv(
    "C:/Users/LUCIA/OneDrive/ANÁLISIS DE DATOS/VISUAL BOX/Proyecto7/vehicles_us.csv")
st.header("Explorando Opciones: Resumen de Anuncios de Autos en Venta :red_car:",divider='rainbow')  # Título principal

hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Frecuencia de kilometraje')

    # crear un histograma
    fig = px.histogram(data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox("Construir gráfica de dispersión")
if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Precio vrs Kilometraje')
    fig1 = px.scatter(data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
