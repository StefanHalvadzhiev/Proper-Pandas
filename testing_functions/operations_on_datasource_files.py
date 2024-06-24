import pandas as pd
import numpy as np

def apply_to_lowercase(df: pd.DataFrame) -> pd.DataFrame:
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    return df


def to_lowercase_without_apply(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower()
    return df
    