import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import time
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.decomposition import PCA

class LeadGenerator():
    def __init__(self, train_data, val_data=None, test_data=None, val_label=None, test_label=None):
        self.train_data = train_data.drop(columns = ["id", "emp"])
        if type(val_data) == pd.core.frame.DataFrame:
            self.val_id = val_data["id"].values
            self.val_data = val_data.drop(columns = ["id", "emp"])
            self.val_label = val_label
        if type(test_data) == pd.core.frame.DataFrame:
            self.test_id = test_data["id"].values
            self.test_data = test_data.drop(columns = ["id", "emp"])
            self.test_label = test_label

    def fit(self):
        a = time.time()
        inertia_values = []
        Model = KMeans()
        Visualizer = KElbowVisualizer(Model, k = (3, 15), metric = "silhouette")
        Visualizer.fit(self.train_data)     
        plt.close()  
        elbow_value = Visualizer.elbow_value_
        if elbow_value == None:
            self.clusters = 5
        else:
            self.clusters = elbow_value
        self.KM = KMeans(self.clusters)
        self.KM.fit(self.train_data)
        self.centers = self.KM.cluster_centers_
        b = time.time()
        print("Fit time: {}s." .format(b - a))
        print("{} clusters are selected." .format(self.clusters))
        
    def predict(self):
        prediction_val = []
        print("Validation")
        for data in self.val_data.values:
            temp_values = np.zeros(self.clusters)
            for i, c in enumerate(self.centers):
                sim = cosine_similarity(c.reshape(1, -1), data.reshape(1, -1))
                temp_values[i] = sim
            prediction_val.append(np.max(temp_values))
        val_df = pd.DataFrame({"ID": self.val_id, "Similarity": prediction_val, "Client": self.val_label})
        self.val_df = val_df 
        test_val = []
        print("Test")
        for data in self.test_data.values:
            temp_values = np.zeros(self.clusters)
            for i, c in enumerate(self.centers):
                sim = cosine_similarity(c.reshape(1, -1), data.reshape(1, -1))
                temp_values[i] = sim
            test_val.append(np.max(temp_values))
        test_df = pd.DataFrame({"ID": self.test_id, "Similarity": test_val, "Client": self.test_label})
        self.test_df = test_df 
        return val_df, test_df

    def predict_leads(self, client_data):
        prediction = []
        prediction_cluster = []
        client_data_id = client_data["id"].values
        client_data = client_data.drop(columns = ["id", "emp"])
        for data in client_data.values:
            temp_values = np.zeros(self.clusters)
            for i, c in enumerate(self.centers):
                sim = cosine_similarity(c.reshape(1, -1), data.reshape(1, -1))
                temp_values[i] = sim
            prediction.append(np.max(temp_values))
            prediction_cluster.append(np.where(temp_values == np.min(temp_values))[0][0])
        prediction = np.array(prediction)
        prediction = 0.5*(1 + prediction)
        pred_df = pd.DataFrame({"ID": client_data_id, "Similarity": prediction, "Cluster": prediction_cluster})
        pred_df = pred_df.dropna()
        return pred_df

if __name__ == "__main__":
    pass