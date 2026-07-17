"""
Main entry point for the Tehran House Price Analysis project.

Pipeline:
1. Load dataset
2. Perform exploratory analysis
3. Clean and preprocess data
4. Generate engineered features
5. Save processed datasets
6. Visualize the results
"""
from dataset       import read_dataset, show_dataset
from analysis      import analyzing, clean_data
from utils         import dataset_age, save
from visualization import plot_all
from pathlib       import Path

def main() -> None:

    ROOT = Path(__file__).resolve().parent.parent
    DATA_DIR       = ROOT / "dataset"
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DATASET        = DATA_DIR / "TehranHousePrice.csv"
    SAMPLE_DATASET = DATA_DIR / "sample.csv"
    CLEAN_DATASET  = DATA_DIR / "clean_dataset.csv"

    dataset_age()
    print()

    df = read_dataset(DATASET)
    show_dataset(df, "raw")

    analyzing(df)

    df = clean_data(df)

    show_dataset(df, "processed")

    save(df, SAMPLE_DATASET, CLEAN_DATASET)

    plot_all(df)
    print("\nDone.")

if __name__ == '__main__':
    main()
