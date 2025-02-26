import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()

x = df[["diametro"]] # Formato DataFrame
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("Insira o tamanho do diâmetro da pizza")

if diametro > 0:
  preco_previsto = modelo.predict([[diametro]])[0][0]
  st.write(f"O valor da pizza com o diâmetro de {diametro: .2f} cm é de {preco_previsto: .2f}€")
else:
  st.write("O valor do diâmetro da pizza tem de ser maior que 0")