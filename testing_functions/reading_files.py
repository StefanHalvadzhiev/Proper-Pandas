import pandas as pd
import polars as pl


# Reading csv files
def load_small_data(file_paths: [str])-> None:
    for file_path in file_paths:
        pd.read_csv(file_path)


def load_medium_data(file_paths: [str])-> None:
    for file_path in file_paths:
        pd.read_csv(file_path)


def load_big_data(file_paths: [str])-> None:
    for file_path in file_paths:
        pd.read_csv(file_path)


def load_small_data_improved(file_paths: [str])-> None:
    for file_path in file_paths:
        pl.read_csv(source=file_path).to_pandas()


def load_medium_data_improved(file_paths: [str])-> None:
    for file_path in file_paths:
        pl.read_csv(source=file_path).to_pandas()


def load_big_data_improved(file_paths: [str])-> None:
    for file_path in file_paths:
        pl.read_csv(source=file_path).to_pandas()
