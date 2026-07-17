from pandas import Timedelta, Timestamp, DataFrame
from os     import PathLike
# ----------------------------------------------------------------------------------
# Time Set

def dataset_age() -> Timedelta:
    """
    Calculate the age of the dataset.

    Returns:
        A pandas Timedelta representing the number of
        days since the dataset was last updated.
    """
    data_update = Timestamp("2024-9-20")
    dt = Timestamp.now() - data_update
    print(f"update dataset at: {dt.days} days ago")
    return dt
# ----------------------------------------------------------------------------------
# Final Data

def save(df: DataFrame, sample_file: str | PathLike, dataset_file: str | PathLike):
    """
    Save the processed dataset.

    Creates:

    - Full cleaned dataset
    - Random sample dataset
    """
    df.sample(frac=0.5).to_csv(sample_file)
    df.to_csv(dataset_file)
# ----------------------------------------------------------------------------------