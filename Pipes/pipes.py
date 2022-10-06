from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

class Gen_coder (BaseEstimator, TransformerMixin):
    def __init__(self, remove_origin):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        X["G"] = X.Gender.map({'Male':0, 'Female':1})
        
        if self.remove_origin:
            X.drop(['Gender'], axis = 1, inplace = True)
        
        return X
    
class TT_coder (BaseEstimator, TransformerMixin):
    def __init__(self, remove_origin):
        
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        X["TT"] = X['Type of Travel'].map({'Business travel':0, 'Personal Travel':1})
        
        return X
    
class Delay_coder (BaseEstimator, TransformerMixin):
    def __init__(self, remove_origin):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        X["Delay"] = X['Departure Delay in Minutes'] + X['Arrival Delay in Minutes']
        return X
    

myPipe = Pipeline ([('G',Gen_coder(True)), ('TT',TT_coder(False)), ('Delay',Delay_coder(False))])
    