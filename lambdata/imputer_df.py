# imputes the missing categorical values using Simple Imputer and returns a dataframe 
import pandas as pd
import sklearn
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin

class ImputerDF(BaseEstimator, TransformerMixin):
    def __init__(self, strategy='mean'):
        self.imputer = SimpleImputer(strategy=strategy)
        self.cols = []
        
    def fit(self, X, y=None):
        self.imputer.fit(X)
        self.cols = list(X.columns)
        return self
    
    def transform(self, X):
        X_t = self.imputer.transform(X)
        return pd.DataFrame(X_t, columns=self.cols)