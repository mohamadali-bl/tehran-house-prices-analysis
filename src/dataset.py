from pandas import DataFrame, read_csv
from os     import PathLike
from typing import Literal
# ----------------------------------------------------------------------------------
# Dataset Read

def read_dataset(path: str | PathLike) -> DataFrame:
    """
    Load the dataset from a CSV file.

    Args:
        path:
            Path to the CSV dataset.

    Returns:
        Loaded DataFrame.

    Raises:
        RuntimeError:
            If the dataset cannot be found.
    """
    try:
        return read_csv(path)
    except FileNotFoundError:
        raise RuntimeError("dataset file dos not exist.")

def show_dataset(df: DataFrame, kind: str | Literal["processed", "raw"]) -> None:
    """
    Display general information about the dataset.

    The function prints:

    - First rows
    - Statistical summary
    - Column information

    Args:
        df:
            Dataset.

        kind:
            Dataset type ("raw" or "processed").
    """
    print('*' * 60)
    if kind in ["processed", "raw"]:
        print(f"{kind.capitalize()} Dataset (10 row) :")
        print(df.head(10))
        print('-' * 20)
        print(f"Describe of {kind.capitalize()} Dataset: ")
        print(df.describe())
        print('-' * 20)
        df.info()
    print('*' * 60)
# ----------------------------------------------------------------------------------

if __name__ == "__main__":

    DATASET = "dataset/TehranHousePrice.csv"
    df = read_dataset(DATASET)
    print("Dataset loaded successfully.\n")
    show_dataset(df, "raw")
