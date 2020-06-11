import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_feature_data(dataframe, feature, data_type="N"):
    values = dataframe[feature].values
    plt.figure(figsize = (20, 5))
    if data_type == "C":
        sns.countplot(values)
    elif data_type == "N":
        sns.distplot(values, 100, kde = False)
    plt.xticks(rotation=90)
    plt.title(feature)
    plt.show()

def analyze_grouped_feature_data(dataframe, feature, data_type="N"):
    if data_type == "N":
        for emp, name in zip(["emp_1", "emp_2", "emp_3"], ["Empresa 1", "Empresa 2", "Empresa 3"]):
            print("###################################################")
            print(name)
            df_temp = dataframe.groupby([emp]).mean()[feature]
            for i, j in zip(df_temp.index, df_temp.values):
                print("{} - {}" .format(i, j))
    else:
        for emp, name in zip(["emp_1", "emp_2", "emp_3"], ["Empresa 1", "Empresa 2", "Empresa 3"]):
            print("###################################################")
            print(name)
            df_temp = dataframe.groupby([feature]).sum()[emp]
            for i, j in zip(df_temp.index, df_temp.values):
                print("{} - {}" .format(i, j))
                
if __name__ == "__main__":
    pass