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

pd.set_option('max_colwidth', 50)

@st.cache
def load_data():
    df = pd.read_csv("data/data_final.csv")
    or_df = pd.read_csv("data/original_data_formated.csv")
    return df, or_df

def open_file():
    file = st.file_uploader("Selecione o banco de dados de clientes.")
    if file is not None:
        emp = pd.read_csv(file)
        return emp
    else:
        st.write("Nenhum arquivo selecionado!")
        return None

def get_cluster_plot(model, dataframe):
    P_C_A = PCA(n_components = 2)
    P_C_A.fit(dataframe.drop(columns = ["id", "emp"]))
    data = P_C_A.transform(dataframe.drop(columns = ["id", "emp"]))
    cluster = model.KM.predict(dataframe.drop(columns = ["id", "emp"]))
    data = pd.DataFrame(data = {"x": data[:, 0], "y": data[:, 1], "Cluster": cluster})
    data["Cluster"] = data["Cluster"].apply(lambda x: str(x))
    fig = px.scatter(data, x = "x", y = "y", color = "Cluster")
    fig.update_xaxes(title_text="PCA_1")
    fig.update_yaxes(title_text="PCA_2")
    fig.update_layout(coloraxis_showscale=False, showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

def get_cossine_similarity(clusters, data):
    sim = 1e6*np.ones(clusters.shape[0])
    ids = []
    for i in range(clusters.shape[0]):
        ids.append(" ")
    for i, c in enumerate(clusters):
        for j, d in enumerate(data.drop(columns = ["id", "emp"]).values):
            c_sim = np.sqrt(np.sum(np.power(c.reshape(1, -1) - d.reshape(1, -1), 2)))
            if c_sim <= sim[i]:
                sim[i] = c_sim
                ids[i] = data["id"].values[j]
    return ids

def get_clusters_examples(model, train_dataframe, original_portfolio):
    clusters = model.centers
    ids = get_cossine_similarity(clusters, train_dataframe)
    df_show = original_portfolio[original_portfolio["id"].isin(ids)].reset_index(drop = True)
    df_show["Cluster"] = df_show["id"].apply(lambda x: ids.index(x))
    columns_name = ["Natureza jurídica", "SG - UF", "Ramo", "Setor", "Idade da empresa", "Divisão", "Segmento", "SG - UF - Matriz",
            "Saúde tributária", "Nível de atividade", "Meso região", "Quantidade de sócios", "Faturamento estimado", "Quantidade de filiais", "Identificador", "Cluster"]
    df_show.columns = columns_name
    st.dataframe(df_show)

def search_company(id, database):
    database_ids = list(database["id"].values)
    company = None
    if id in database_ids:
        company = database[database["id"] == id]
    return company

def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<center><h3><a href="data:file/csv;base64,{b64}">Realizar download das predições</a></h3></center>'
    return href

if __name__ == "__main__":
    main()