import pandas as pd
import numpy as np


# Function without inplace keyword
def fillna(df: pd.DataFrame) -> pd.DataFrame:
    return df.fillna(np.nan)


# Function with inplace keyword
def fillna_inplace(df: pd.DataFrame):
    return df.fillna(np.nan, inplace=True)