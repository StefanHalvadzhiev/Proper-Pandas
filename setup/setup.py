import string
import random

import pandas as pd
import numpy as np
import typer


ALPHABET = string.ascii_lowercase + string.ascii_uppercase


def generate(
    num_rows: int = typer.Argument(
        ..., help="The number of rows to be generated."
    ),
    num_cols: int = typer.Argument(
        ..., help="The number of columns to be generated."
    ),
    seed: int = typer.Argument(
        ..., help="The seed that will be used for the random generation."
    ),
    name: str = typer.Argument(
        ...,
        help="The location where the file will be saved. The script will automatically rename all the files according to their contents.",
    ),
) -> None:
    # create_numeric_dataframe_file(num_rows, num_cols, seed, name)
    create_string_dataframe_file(
        num_rows, num_cols, seed, name.replace(".csv", "_string.csv")
    )


def log(
    function_name: str, num_rows: int, num_cols: int, seed: int, name: str
) -> None:
    print(f"GENERATING DATAFRAME USING {function_name}")
    print(f"Number of rows provided {num_rows}")
    print(f"Number of columns provided {num_cols}")
    print(f"Seed provided {seed}")
    print(f"File location provideed {name}")


def create_numeric_dataframe_file(
    num_rows: int, num_cols: int, seed: int, name: str
) -> None:
    log(create_numeric_dataframe_file.__name__, num_rows, num_cols, seed, name)

    # set random seed
    np.random.seed(seed)

    # create DataFrame with random values
    data = np.random.rand(num_rows, num_cols)
    df = pd.DataFrame(data)

    # save DataFrame to CSV file
    df.to_csv(name, index=False)

    print(f"Generation done.")


def create_string_dataframe_file(
    num_rows: int, num_cols: int, seed: int, name: str
) -> None:
    log(create_string_dataframe_file.__name__, num_rows, num_cols, seed, name)

    # Set the seed for the random number generator
    np.random.seed(seed)

    string_size = np.random.randint(0, 20)
    
    # Generate an array of random strings
    data = [[generate_random_string(string_size, seed + 2**j + i) 
             for j in range(num_cols)] for i in range(num_rows)]

    # Create a Pandas dataframe from the array
    df = pd.DataFrame(data, columns=[f"col_{i+1}" for i in range(num_cols)])

    # Export dataframe to CSV file
    df.to_csv(name, index=False)

    return df


def generate_random_string(length: int, seed: int) -> str:
    random.seed(a=seed)
    return ''.join((random.choice(ALPHABET)) for x in range(length))


def create_datasource_file(
    num_rows: int = typer.Argument(
        ..., help="The number of rows to be generated."
    ),
    num_cols: int = typer.Argument(
        ..., help="The number of columns to be generated."
    ),
    seed: int = typer.Argument(
        ..., help="The seed that will be used for the random generation."
    ),
    name: str = typer.Argument(
        ..., help="The location where the file will be saved."
    ),
) -> None:
    pass


if __name__ == "__main__":
    typer.run(generate)
