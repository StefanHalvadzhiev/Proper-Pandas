import pandas as pd


def sort_strings_inplace(df: pd.DataFrame) -> pd.DataFrame:
    df.apply(lambda x: x.sort_values(inplace=True), axis=0)


def sort_strings(df: pd.DataFrame) -> pd.DataFrame:
    return df.apply(lambda x: sorted(x), axis=0)

