import numpy as np
import pandas as pd
import streamlit as st


st.title("Finanças pessoais v0.1")

choice = st.selectbox('O que fazer?',['Inserir novo pagamnento','Visualizar pagamentos já feitos'])


st.text(choice)





# st.selectbox('Escolha a forma de pagamento',['Cartão BB','Cartão Nubank','Dinheiro/PIX'])



