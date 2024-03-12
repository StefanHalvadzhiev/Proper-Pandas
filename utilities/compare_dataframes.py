import pandas as pd

def compare_dataframes(df_1: pd.DataFrame, df_2: pd.DataFrame) -> bool:
    """
    This function compares two dataframes and returns a boolean indicating if they are equal.

    Parameters:
    `df_1 (pd.DataFrame)`: The first dataframe to compare.
    `df_2 (pd.DataFrame)`: The second dataframe to compare.

    Returns:
    `bool`: A boolean indicating if the dataframes are equal.

    """
    # Sort the dataframes by their column names
    sorted_df_1 = df_1.sort_values(by=df_1.columns.tolist()).reset_index(drop=True)
    sorted_df_2 = df_2.sort_values(by=df_2.columns.tolist()).reset_index(drop=True)

    # Check if the sorted dataframes are equal
    return sorted_df_1.equals(sorted_df_2)