from sklearn.metrics import precision_score, recall_score, fbeta_score
import matplotlib.pyplot as plt
import numpy as np

class Metrics():
    def __init__(self, dataframe, beta=1):
        self.y_train = dataframe["Client"]
        self.y_pred = dataframe["Similarity"]
        self.beta = beta

    def show_model_performance(self):
        n_points = 10
        thr = np.linspace(0, 1, n_points)
        precision = np.zeros(n_points)
        recall = np.zeros(n_points)
        fb_score = np.zeros(n_points)
        for i, t in enumerate(thr):
            y_pred = self.y_pred.copy()
            y_pred[y_pred < t] = 0
            y_pred[y_pred >= t] = 1
            precision[i] = precision_score(self.y_train, y_pred, zero_division = 0)
            recall[i] = recall_score(self.y_train, y_pred,zero_division = 0)
            fb_score[i] = fbeta_score(self.y_train, y_pred, beta = self.beta, zero_division = 0)
        self.__plot_metrics(precision, recall, fb_score)

    def __plot_metrics(self, precision, recall, fb_score):
        plt.plot(precision)
        plt.plot(recall)
        plt.plot(fb_score)
        plt.legend(["Precision", "Recall", "FB_Score"])
        plt.title("Model performance")
        plt.xlabels("Threshold")
        plt.ylabel("Metrics value (%)")
        plt.show()

if __name__ == "__main__":
    pass