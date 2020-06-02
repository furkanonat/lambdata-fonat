
# new_lambdata/new_mod.py

def null_detector(X):
    """
    X is a dataframe

    Function will give the null values in the dataframe
    """
    return X.isnull().sum()



