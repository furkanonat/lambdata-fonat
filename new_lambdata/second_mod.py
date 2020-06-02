
# new_lambdata/second_mod.py

def data_wrangle(X):
    """
    X is a dataframe

    Function will split the datetime object to columns
    """

    # Convert date_recorded to datetime
    X['date_recorded'] = pd.to_datetime(X['date_recorded'], infer_datetime_format=True)

    # Split the datetime object into its components
    X['year_recorded']=X['date_recorded'].dt.year
    X['month_recorded']=X['date_recorded'].dt.month
    X['day_recorded']=X['date_recorded'].dt.day

    return X