import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

@st.cache
def carrega_dados(caminho):
    pass

def main():

    lista_cidades=['Floripa', 'Palhoça']
    lista_aeroportos=['Hercílio Luz', 'Palhocense']
    lista_voos=['voo1', 'voo2', 'voo3']

    st.title("Previsão de Atraso de Voos Comerciais")
    st.markdown("Selecione os valores no menu lateral esquerdo")

    start_date = datetime.today()
    end_date = start_date + timedelta(days=3)

    cidade = st.sidebar.selectbox("Selecione a Cidade", lista_cidades)
    aeroporto = st.sidebar.selectbox("Selecione o Aeroporto", lista_aeroportos)
    voo = st.sidebar.selectbox("Selecione o Voo", lista_voos)
    data = st.sidebar.date_input("Selecione a Data de Partida", min_value=start_date, max_value=end_date, value=start_date)
    data_texto = data.strftime('%d/%m/%Y')

    st.write(cidade)
    st.write(aeroporto)
    st.write(voo)
    st.write(data_texto)

    if st.sidebar.button('Executar'):
        if voo == 'voo3':
            st.success(f'O voo "{voo}" saindo de {cidade} em {data_texto} chegará no horário! :smiley:')
        else:
            st.error(f'O voo "{voo}" saindo de {cidade} em {data_texto} **não** chegará no horário! :worried:')

if __name__ == "__main__":
    main()