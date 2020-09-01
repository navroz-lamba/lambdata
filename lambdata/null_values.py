""" It will return a table with total and percentage of Null values in a given dataframe """
import pandas as pd

def null_values(df):

    total_nan = df.isna().sum().sort_values(ascending=False)
    # percentage of NaN values in a dataset
    percentage_nan = (total_nan / df.shape[0]) * 100
    # concat them together 
    table = pd.concat(
        [total_nan, percentage_nan], 
        axis=1, 
        keys = ['Total Null Values', 'Percentage of Null values']
    )

    return table 