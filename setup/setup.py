import string
import random
from datetime import datetime, timedelta

import pandas as pd
import numpy as np
import typer

import setup_config as config


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
    # create_string_dataframe_file(
    #     num_rows, num_cols, seed, name.replace(".csv", "_string.csv")
    # )
    create_datasource_file(
        num_rows, num_cols, seed, name.replace(".csv", "_datasource.csv")
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

    string_size = np.random.randint(0, config.RANDOM_STRING_MAX_LEN)

    # Generate an array of random strings
    data = [
        [
            generate_random_string(string_size, seed + 2**j + i)
            for j in range(num_cols)
        ]
        for i in range(num_rows)
    ]

    # Create a Pandas dataframe from the array
    df = pd.DataFrame(data, columns=[f"col_{i+1}" for i in range(num_cols)])

    # Export dataframe to CSV file
    df.to_csv(name, index=False)

    return df


def generate_random_string(length: int, seed: int) -> str:
    random.seed(a=seed)
    return "".join((random.choice(ALPHABET)) for x in range(length))


def generate_random_datetime(
    length: int, seed: int, start_date: [int], end_date: [int]
) -> pd.Series:
    random.seed(seed)
    start_date = datetime(
        year=start_date[2],
        month=start_date[1],
        day=start_date[0],
        hour=random.randint(0, 23),  # Random hour between 0 and 23
        minute=random.randint(0, 59),  # Random minute between 0 and 59
    )

    end_date = datetime(
        year=end_date[2],
        month=end_date[1],
        day=end_date[0],
        hour=random.randint(0, 23),  # Random hour between 0 and 23
        minute=random.randint(0, 59),  # Random minute between 0 and 59
    )

    random_dates = [
        start_date
        + timedelta(days=random.randint(0, (end_date - start_date).days))
        for _ in range(length)
    ]

    return pd.Series(random_dates)


def pick_random_column_type(seed: int) -> str:
    datatypes = ["int64", "str"]
    random.seed(seed)
    return datatypes[random.randint(0, len(datatypes) - 1)]


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
    """
    The parameter num_cols gives the amonut of additional columns to be generated. Mandatory
    columns have been provided in the setup_config.py file.
    """
    # log(
    #     name=create_datasource_file.__name__,
    #     num_rows=num_rows,
    #     num_cols=num_cols,
    #     seed=seed,
    # )

    # Generate mandatory datetime columns
    df = pd.DataFrame(columns=config.DATASOURCE_FILE_MANDATORY_COLUMNS)
    df["reference_date"] = generate_random_datetime(
        length=num_rows,
        seed=seed,
        start_date=config.DATASOURCE_FILE_REFERENCE_DATE_FROM,
        end_date=config.DATASOURCE_FILE_REFERENCE_DATE_TO,
    )
    df["delivery_begin"] = generate_random_datetime(
        length=num_rows,
        seed=seed,
        start_date=config.DATAOSURCE_FILE_DELIVERY_FROM,
        end_date=config.DATASOURCE_FILE_DELIVERY_TO,
    )
    df["delivery_end"] = df["reference_date"] + timedelta(hours=1)
    df["created_at"] = datetime.utcnow().strftime(
        config.DATASOURCE_FILE_TIME_FORMAT
    )

    # Generate pure data columns
    for column_index in range(0, num_cols):
        np.random.seed(seed)
        data_type = np.random.choice(config.DATASOURCE_TYPES)
    
        # Generate random data based on the selected data type
        data = None
        if data_type == str:
            data = [generate_random_string(config.MAX_STRING_LENGTH, (seed + row) * 2) for row in range(0, num_rows)  ]
        else:
            data = np.random.randint(0, 100, num_rows)
        
        # Create a column with the generated data and data type
        col_name = f'Column_{column_index}'
        df = df.assign(**{col_name:data})
        seed += 1

    df.to_csv(name, index=False)


if __name__ == "__main__":
    typer.run(generate)
