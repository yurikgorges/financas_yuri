import numpy as np
import pandas as pd
import streamlit as st


st.title("Finanças pessoais v0.1")

choice = st.selectbox('# O que fazer?',['Inserir novo pagamento','Visualizar pagamentos já feitos'])

if (choice=='Inserir novo pagamento'):    
    desc_gasto = st.text_input('Descrição do gasto')
    forma_pag = st.selectbox('Qual forma de pagamento',['Cartão Nubank','Cartão BB','Dinheiro/PIX'])
    valor_gasto = st.text_input('Valor (R$)')
    categoria = st.selectbox('Categoria',['Comida','Lazer','Eletro/Casa','Tech'])
    data = st.date_input('Insira a data')

d = {'Descrição':[desc_gasto],'Forma de pagamento':[forma_pag],'Valor gasto (R$)':[valor_gasto],'Categoria':[categoria],'Data':[data]}

df = st.dataframe(d)

st.text(df)

    







# st.selectbox('Escolha a forma de pagamento',['Cartão BB','Cartão Nubank','Dinheiro/PIX'])



