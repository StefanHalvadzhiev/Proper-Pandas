import pandas as pd
import numpy as np


# MEDIAN
def median_rows(df: pd.DataFrame) -> None:
    pass


def median_columns(df: pd.DataFrame) -> None:
    pass


def median_rows_improved(df: pd.DataFrame) -> None:
    pass


def median_columns_improved(df: pd.DataFrame) -> None:
    pass


# MEAN
def mean_rows(df: pd.DataFrame) -> pd.DataFrame:
    row_means = df.mean(axis=1)
    result_df = pd.DataFrame(row_means, columns=['Mean'])
    return result_df


def mean_columns(df: pd.DataFrame) -> None:
    row_means = df.mean(axis=0)
    result_df = pd.DataFrame(row_means, columns=['Mean'])
    return result_df


def mean_rows_improved(df: pd.DataFrame) -> pd.DataFrame:
    row_means = np.mean(df.to_numpy(), axis=1)
    result_df = pd.DataFrame(row_means, columns=['Mean'])
    return result_df


def mean_columns_improved(df: pd.DataFrame) -> None:
    row_means = np.mean(df.to_numpy(), axis=0)
    result_df = pd.DataFrame(row_means, columns=['Mean'])
    return result_df
