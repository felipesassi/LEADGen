from sklearn.preprocessing import StandardScaler, LabelEncoder

class Transform_Bool_Data():
    def __init__(self, bool_features):
        self.bool_features = bool_features
    
    def fit(self, x, y=None):
        pass
    
    def transform(self, x, y=None):
        x = x.copy()
        for c in self.bool_features:
            x[c] = x[c].apply(lambda x: 1 if x else 0)
        return x
    
    def fit_transform(self, x, y=None):
        self.fit(x)
        x = self.transform(x)
        return x

class Transform_Categorical_Data():
    def __init__(self, categorical_features):
        self.categorical_features = categorical_features
    
    def fit(self, x, y=None):
        self.enc_dict = {}
        for c in self.categorical_features:
            LE = LabelEncoder()
            LE.fit(x[c])
            self.enc_dict[c] = LE
    
    def transform(self, x, y=None):
        x = x.copy()
        for c in self.categorical_features:
            x[c] = self.enc_dict[c].transform(x[c])
        return x
    
    def fit_transform(self, x, y=None):
        self.fit(x, y)
        x = self.transform(x)
        return x

class Tranform_Numerical_Data():
    def __init__(self, numerical_features):
        self.numerical_features = numerical_features
    
    def fit(self, x, y=None):
        self.SC = StandardScaler()
        self.SC.fit(x)
    
    def transform(self, x, y=None):
        x = x.copy()
        x = self.SC.transform(x)
        return x
    
    def fit_transform(self, x, y=None):
        self.fit(x)
        x = self.transform(x)
        return x

if __name__ == "__main__":
    pass