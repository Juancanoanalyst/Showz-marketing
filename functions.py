import pandas as pd

def standard_columns(df):
    '''
    This function standardizes the column names of a DataFrame by converting them to lowercase,
    replacing spaces with underscores, and removing any leading or trailing whitespace.
    df = dataframe
    '''

    n_columns=[]
    for column in df.columns:
        minus = column.lower()
        strip = minus.replace(" ","_")
        n_columns.append(strip)
        
    df.columns = n_columns
    df.info()
    return df.head(5)