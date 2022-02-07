import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

@st.cache
def processa_dados():
    dados_voos = pd.read_csv('./dados/dados_basicos_voos.csv', sep=';', encoding='utf-8')
    dados_aeroportos = pd.read_excel('./dados/glossario_de_aerodromo.xls', skiprows=3)

    dados_aeroportos = dados_aeroportos.drop(['Unnamed: 0','País', 'Continente'], axis=1)
    dados_aeroportos.rename(columns={'Sigla OACI': 'ICAO Aeródromo Origem', 'Descrição': 'Nome Aeroporto'}, inplace=True)

    dados_voos = pd.merge(dados_voos, dados_aeroportos, on=['ICAO Aeródromo Origem'])
    return dados_voos

def main():

    dados_voos = processa_dados()


    lista_cidades=dados_voos['Cidade'].unique().tolist()
    lista_aeroportos=dados_voos['Nome Aeroporto'].unique().tolist()
    lista_empresas=dados_voos['ICAO Empresa Aérea'].unique().tolist()
    lista_voos=dados_voos['Número Voo'].unique().tolist()

    st.title("Previsão de Atraso de Voos Comerciais")
    st.markdown("Selecione os valores no menu lateral esquerdo (pode ser necessário expandir)")

    start_date = datetime.today()
    end_date = start_date + timedelta(days=3)

    cidade = st.sidebar.selectbox("Selecione a Cidade", lista_cidades)
    aeroporto = st.sidebar.selectbox("Selecione o Aeroporto", lista_aeroportos)
    empresa = st.sidebar.selectbox("Selecione a Empresa", lista_empresas)
    voo = st.sidebar.selectbox("Selecione o Voo", lista_voos)
    data = st.sidebar.date_input("Selecione a Data de Partida", min_value=start_date, max_value=end_date, value=start_date)
    data_texto = data.strftime('%d/%m/%Y')

    st.write(cidade)
    st.write(aeroporto)
    st.write(f'{empresa}{voo}')
    st.write(data_texto)

    if st.sidebar.button('Executar'):
        if voo == 'voo3':
            st.success(f'O voo "{empresa}{voo}" saindo de {cidade} em {data_texto} chegará no horário! :smiley:')
        else:
            st.error(f'O voo "{empresa}{voo}" saindo de {cidade} em {data_texto} **não** chegará no horário! :worried:')

if __name__ == "__main__":
    main()