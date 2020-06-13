import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scripts.data_selection import separate_data
from scripts.model import LeadGenerator
from sklearn.decomposition import PCA
import plotly.express as px
import base64
import os
from dashboard.dashboard_design import *

def main():
    st.title("LEADGen - Geração de leads")
    df, or_df, n_rows = load_data()
    st.sidebar.title("O que deseja realizar?")
    options = ("Predição de clientes", "Análise de resultados", "Análise de clientes")
    opt = st.sidebar.selectbox("Selecione uma opção", options)
    if opt == options[0]:
        emp = open_file()
        if type(emp) == pd.core.frame.DataFrame:
            train_df, client_df = separate_data(df, emp, train = False)
            txt = "<center><h4>Número de clientes selecionados: {}. </center></h4>" .format(emp.shape[0])
            st.markdown(txt, unsafe_allow_html = True)
            LG = LeadGenerator(train_df)
            LG.fit()
            st.markdown("<center><h3>Apresentação gráfica das empresas clusterizadas</center></h3>", unsafe_allow_html = True)
            get_cluster_plot(LG, train_df, or_df[or_df["id"].isin(train_df["id"])].reset_index(drop = True))
            st.markdown("<center><h3>Centros de cada cluster</h3></center>", unsafe_allow_html = True)
            get_clusters_examples(LG, train_df, or_df)
            st.markdown("<center><h3>Predição de possíveis clientes</center></h3>", unsafe_allow_html = True)
            pred = st.checkbox("Realizar predições?")
            if pred == True:
                try:
                    os.remove("data/temp_results.csv")
                except:
                    pass
                predict = LG.predict_leads(client_df[:n_rows])
                predict.to_csv("data/temp_results.csv", index = False)
                st.markdown(get_table_download_link(predict), unsafe_allow_html = True)
    elif opt == options[1]:
        try:
            predict_temp = pd.read_csv("data/temp_results.csv")
            st.markdown("<center><h3>Resultados detalhados</h3></center>", unsafe_allow_html = True)
            min_value = predict_temp["Similarity"].min()
            min_sim = st.slider("Similaridade mínima", min_value = min_value, max_value = 1.0, step = 0.01)
            max_sim = st.slider("Similaridade máxima", min_value = min_sim, max_value = 1.0, step = 0.01)
            sel = (predict_temp["Similarity"] >= min_sim) & (predict_temp["Similarity"] <= max_sim)
            st.table(predict_temp[sel].sort_values(by = "Similarity", ascending = False).reset_index(drop = True).head(15))
            st.markdown("<center><h3>Download das previsões selecionadas</h3></center>", unsafe_allow_html = True)
            if predict_temp[sel].shape[0] > 10000:
                n_rows_temp = int(predict_temp[sel].shape[0]/4)
            else:
                n_rows_temp = predict_temp[sel].shape[0]
            st.markdown(get_table_download_link(predict_temp[sel].reset_index(drop = True)[:n_rows_temp]), unsafe_allow_html = True)
        except:
            st.write("Nenhum conjunto de dados para analisar!")
    elif opt == options[2]:
        id_selected = st.text_input("Insira o identificador de determinada empresa para maiores detalhes")
        search = search_company(id_selected, or_df)
        if type(search) == pd.core.frame.DataFrame: 
            print(search.columns)           
            columns_name = ["Natureza jurídica", "SG - UF", "Ramo", "Setor", "Idade da empresa", "Divisão", "Segmento", "SG - UF - Matriz",
            "Saúde tributária", "Nível de atividade", "Meso região", "Quantidade de sócios", "Faturamento estimado", "Quantidade de filiais", "Identificador"]
            search.columns = columns_name
            for i, c in enumerate(columns_name):
                if c != "Identificador":
                    if pd.isna(search.values[0][i]):
                        txt = "**{}:** {}" .format(c, "NaN")
                    elif search.values[0][i] == True:
                        txt = "**{}:** {}" .format(c, "Sim")
                    elif search.values[0][i] == False and search.values[0][i] != 0:
                        txt = "**{}:** {}" .format(c, "Falso")
                    else:
                        txt = "**{}:** {}" .format(c, search.values[0][i])
                    st.markdown(txt, unsafe_allow_html = True)
        else: 
            st.write("Nada para mostrar")

if __name__ == "__main__":
    main()