import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

# **********************************************************
# **********************************************************

class Imp_0 (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X.fillna(0, inplace = True)
        
        if self.remove_origin:
            pass
            # Remove original fields
        
        return X
    
# **********************************************************
# **********************************************************
# Вика
class T_O_T (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X['Type of Travel'] = X['Type of Travel'].map({'Business travel':0, 'Personal Travel':1})
        
        if self.remove_origin:
            pass
            #X.drop(['Type of Travel'], axis = 1, inplace = True)
            # Remove original fields
        
        return X

# **********************************************************
# **********************************************************
# Алексей
class Imp_class (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X['Class'] = X['Class'].map({'Eco': 0, 'Eco Plus': 1, 'Business': 2})
        
        if self.remove_origin:
            pass
            # Remove original fields
        
        return X

# **********************************************************
# **********************************************************
   
# Арина
class C_T(BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X['Customer Type'] = X['Customer Type'].map({'Loyal Customer': 1, 'disloyal Customer': 0})
        
        if self.remove_origin:
            # Remove original fields
            pass
        
        return X    

# **********************************************************
# **********************************************************
# Настя
class Gnd (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X['Gender'] = X['Gender'].map({'Female': 0, 'Male':1}) # inplace = True - чтобы изменения сразу сохранялись без присваивания
        
        if self.remove_origin:
            pass
            # Remove original fields
        
        return X

# **********************************************************
# **********************************************************
# Елена
class stat (BaseEstimator, TransformerMixin): 
     
    def __init__(self, remove_origin = False): 
        self.remove_origin = remove_origin 
     
    def fit(self, X, y = None): 
        return self 
     
    def transform(self, X, y = None): 
        # Transformation 
        X['satisfaction'] = X['satisfaction'].map({'neutral or dissatisfied': 0, 'satisfied': 1}) 
         
        if self.remove_origin: 
            pass 
         
        return X    

    
# **********************************************************
# **********************************************************
# **********************************************************
# **********************************************************

myPipe = Pipeline ([('Imp_0',Imp_0()),
                    ('T_O_T',T_O_T()), 
                    ('Imp_class',Imp_class()), 
                    ('C_T',C_T()),
                    ('Gnd',Gnd()),
                    ('stat',stat())])



