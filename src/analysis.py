from pandas import DataFrame, cut
from numpy  import int64, uint16, uint8, inf
# ----------------------------------------------------------------------------------
# Analyzing

def analyzing(df: DataFrame) -> None:
    """
    Perform exploratory analysis.

    The function reports:

    - Large area outliers
    - Address statistics
    - Missing values
    - Invalid records
    """
    MAX_AREA = 5000
    df["Area"] = df["Area"].str.replace(',', '').astype(int64)
    print(f"Area > 1000:\n{df[df["Area"] > MAX_AREA]}") #in this dataset if area > 4000, area is nosier
    print('-' * 20)
    print(f"Address count: {df.groupby("Address").count()}")
    print('-' * 20)
    print(f"Null Columns:\n{df.isna().any()}")
    print('-' * 20)
    print(f"NaN Index of Address: {df[df["Address"].isna()].index.values}")
    print('-' * 20)
# ----------------------------------------------------------------------------------
# Cleaning and Set

def iqr_filter(df: DataFrame, column: str, k: float):
    """
    Remove outliers using the IQR method.

    Args:
        df:
            Dataset.

        column:
            Target numeric column.

        k:
            IQR multiplier.

    Returns:
        Filtered DataFrame.
    """
    print(df[column].describe())
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    df = df[
        (df[column] >= Q1 - k * IQR) &
        (df[column] <= Q3 + k * IQR)
        ]
    print(df[column].describe())
    return df
def usd_price() -> int | None:
    """
    Retrieve the latest USD to IRR exchange rate
    from the Navasan API.

    Returns:
        Exchange rate in IRR.

    Returns None if the API key is unavailable.
    """
    from requests import get
    try:
        with open("data/API_KEY.txt") as f:
            API_KEY = f.read().strip()
        response = get(f"https://api.navasan.tech/latest/?api_key={API_KEY}", timeout=10)
        response.raise_for_status()
        return int(response.json()["usd_sell"]["value"]) * 10  # Exchanging USD to IRR
    except FileNotFoundError | FileExistsError:
        print("API_KEY Not Found.")
        return

def clean_data(df: DataFrame, feature: bool = True, exchange: bool = False) -> DataFrame:
    """
    Clean the dataset and generate additional features.

    Operations:

    - Remove missing values
    - Remove noisy records
    - Convert data types
    - Generate engineered features
    - Optionally convert USD to IRR

    Returns:
        Cleaned DataFrame.
    """
    MAX_AREA = 5000
    df = df.drop(columns="Price").dropna(ignore_index=True)
    df = df[df["Area"] <= MAX_AREA] # Selecting a manual range based on data

    df = df.astype({
        "Area": uint16,
        "Room": uint8,
        "Address": "string"
    })

    if feature:

        df["PriceGrade"] = cut(
            df["Price(USD)"],
            10,
            labels=[
                "Budget",
                "Affordable",
                "Economy",
                "Standard",
                "MidRange",
                "UpperMid",
                "Premium",
                "HighEnd",
                "Luxury",
                "UltraLuxury"
            ]
        )
        df["AreaGrade"] = cut(
            df["Area"],
            bins=[0, 40, 60, 90, 120, 200, 500, inf],
            labels=[
                "Tiny",
                "Small",
                "Medium",
                "Large",
                "VeryLarge",
                "Huge",
                "Massive"
            ]
        )
        df["Price(meter²)"] = (df["Price(USD)"] / df["Area"])
        df["Price(Neighborhood)"] = df.groupby("Address")["Price(USD)"].transform("mean")

    if exchange:
        df["Price(IRR)"] = (df["Price(USD)"] * usd_price()).round(3)

    return df
# ----------------------------------------------------------------------------------

if __name__ == "__main__":
    from dataset import read_dataset, show_dataset

    DATASET = "dataset/TehranHouse.csv"
    df = read_dataset(DATASET)
    analyzing(df)
    df = clean_data(df)
    print("\nProcessed Dataset\n")
    show_dataset(df, "processed")
