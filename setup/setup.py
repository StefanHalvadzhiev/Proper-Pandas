import pandas as pd
import numpy as np
import typer


def create_dataframe_file(
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
    print(f"Number of rows provided {num_rows}")
    print(f"Number of columns provided {num_cols}")
    print(f"Seed provided {seed}")
    print(f"File location provideed {name}")

    # set random seed
    np.random.seed(seed)

    # create DataFrame with random values
    data = np.random.rand(num_rows, num_cols)
    df = pd.DataFrame(data)

    # save DataFrame to CSV file
    df.to_csv(name, index=False)

    print(f"Generation done.")


if __name__ == "__main__":
    typer.run(create_dataframe_file)
