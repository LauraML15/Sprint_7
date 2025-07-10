import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.header("Análisis de anuncios de venta de coches")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Histograma
if st.checkbox('Mostrar histograma de odómetro'):
    st.write('Histograma de la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión precio vs odómetro'):
    st.write('Gráfico de dispersión entre odómetro y precio')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)

