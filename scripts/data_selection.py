import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
            
def remove_outliers(dataframe):
    P_C_A = PCA(2)
    P_C_A.fit(dataframe.drop(columns = ["id", "emp"]))
    data = P_C_A.transform(dataframe.drop(columns = ["id", "emp"]))
    df = pd.DataFrame(data = {"x": data[:, 0], "y": data[:, 1], "id": dataframe["id"].values})
    sel = (np.abs(df["x"]) < 10) & (np.abs(df["y"] < 10))
    id_final = df[sel]["id"].values
    return dataframe[dataframe["id"].isin(id_final)].reset_index(drop = True)

def separate_data(dataframe, static_portfolio, train=True, train_perc=0.5):
    dataframe = dataframe.copy()
    total_ids = len(list(static_portfolio["id"].values))
    port_id = list(static_portfolio["id"].values)
    static_portfolio = shuffle(static_portfolio, random_state = 0).reset_index(drop = True)
    dataframe["emp"] = dataframe["id"].apply(lambda x: 1 if x in port_id else 0)
    if train == True:
        n_rows = int(train_perc*static_portfolio.shape[0])
        train_id = list(static_portfolio["id"].values[:n_rows])
        train_df = dataframe[dataframe["id"].isin(train_id)].reset_index(drop = True)
        train_df = remove_outliers(train_df)
        other_df = dataframe[~dataframe["id"].isin(train_id)]
        x_val, x_test, y_val, y_test = train_test_split(other_df, 
                                                        other_df["emp"].values, 
                                                        test_size = 0.5,
                                                        stratify = other_df["emp"].values,
                                                        random_state = 0)
        return train_df, x_val.reset_index(drop = True), x_test.reset_index(drop = True), y_val, y_test
    else:
        n_rows = static_portfolio.shape[0]
        train_id = list(static_portfolio["id"].values[:n_rows])
        train_df = dataframe[dataframe["id"].isin(train_id)].reset_index(drop = True)
        train_df = remove_outliers(train_df)
        other_df = dataframe[~dataframe["id"].isin(train_id)].reset_index(drop = True)
        return train_df, other_df

if __name__ == "__main__":
    pass