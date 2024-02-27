import pandas as pd
import polars as pl

import config


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


# USE POLARS
def load_small_data_polars(file_paths: [str])-> None:
    for file_path in file_paths:
        pl.read_csv(source=file_path).to_pandas()


def load_medium_data_polars(file_paths: [str])-> None:
    for file_path in file_paths:
        pl.read_csv(source=file_path).to_pandas()


def load_big_data_polars(file_paths: [str])-> None:
    for file_path in file_paths:
        pl.read_csv(source=file_path).to_pandas()


# USE CHUNK READING WITH PANDAS
def load_small_data_chunked(file_paths: [str])-> None:
    for file_path in file_paths:
        for chunk in pd.read_csv(file_path, chunksize=config.READING_CHUNK_SIZE):
            pass


def load_medium_data_chunked(file_paths: [str])-> None:
    for file_path in file_paths:
        for chunk in pd.read_csv(file_path, chunksize=config.READING_CHUNK_SIZE):
            pass


def load_big_data_chunked(file_paths: [str])-> None:
    for file_path in file_paths:
        for chunk in pd.read_csv(file_path, chunksize=config.READING_CHUNK_SIZE):
            pass