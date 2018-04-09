import pandas as pd
"""
Helper module for time series predictions
"""

def forecast_MAE():
    """
    Provides the mean average error for a model given a test data set
    """
    return NotImplementedError

def make_df_prophet_ready(my_df):
    """
    Strips the timezone and renames the timezone ds. The function assumes that
    the time column is the index of the pandas dataframe
    Args:
        df (pandas DataFrame): dataframe with time column as the index
    """
    df = my_df.copy()
    if df.empty:
        raise Exception
    index_col_name = df.index.name
    df['ds'] = df.index
    df = df.reset_index()
    df = df.drop([index_col_name], axis=1)
    df['ds'] = df.ds.dt.tz_localize(None)
    return df
