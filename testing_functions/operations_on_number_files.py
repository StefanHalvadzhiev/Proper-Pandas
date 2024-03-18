import pandas as pd
import numpy as np


# MEDIAN
def median_rows(df: pd.DataFrame) -> pd.DataFrame:
    row_medians = df.median(axis=1)
    return pd.DataFrame(row_medians, columns=['Median'])
    

def median_columns(df: pd.DataFrame) -> pd.DataFrame:
    col_medians = df.median(axis=0)
    return pd.DataFrame(col_medians, columns=['Median'])
    

def median_rows_improved(df: pd.DataFrame) -> pd.DataFrame:
    row_medians = np.median(df.to_numpy(), axis=1)
    return pd.DataFrame(row_medians, columns=['Median'])
    

def median_columns_improved(df: pd.DataFrame) -> pd.DataFrame:
    col_medians = np.median(df.to_numpy(), axis=0)
    return pd.DataFrame(col_medians, columns=['Median'])
    

# MEAN
def mean_rows(df: pd.DataFrame) -> pd.DataFrame:
    row_means = df.mean(axis=1)
    return pd.DataFrame(row_means, columns=['Mean'])
    

def mean_columns(df: pd.DataFrame) -> None:
    row_means = df.mean(axis=0)
    return pd.DataFrame(row_means, columns=['Mean'])
    

def mean_rows_improved(df: pd.DataFrame) -> pd.DataFrame:
    row_means = np.mean(df.to_numpy(), axis=1)
    return pd.DataFrame(row_means, columns=['Mean'])
    

def mean_columns_improved(df: pd.DataFrame) -> None:
    col_means = np.mean(df.to_numpy(), axis=0)
    return pd.DataFrame(col_means, columns=['Mean'])
