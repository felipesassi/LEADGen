def get_data_type(dataframe):
    bool_data = []
    object_data = []
    numerical_data = []
    for col in dataframe.columns:
        if dataframe[col].dtype == "bool":
            bool_data.append(col)
        elif dataframe[col].dtype == "O":
            object_data.append(col)
        else:
            numerical_data.append(col)
    numerical_data.remove("emp_1")
    numerical_data.remove("emp_2")
    numerical_data.remove("emp_3")
    return bool_data, object_data, numerical_data