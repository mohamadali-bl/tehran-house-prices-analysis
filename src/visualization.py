from pandas              import DataFrame
from pathlib             import Path
import matplotlib.pyplot as plt
import plotly.express    as px
import seaborn           as sns
# ----------------------------------------------------------------------------------
# Plot

def plot_all(df: DataFrame):
    """
    Generate all exploratory plots.

    Generated plots include:

    - Distribution plots
    - Histograms
    - Scatter plots
    - Box plots
    - Heatmap
    - Interactive 3D plots
    """
    ROOT = Path(__file__).resolve().parent.parent
    PLOT_DIR = ROOT / "data"
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    # ----------------------------------
    df["Area"].plot()
    plt.grid()
    plt.title("Area Distribution")
    plt.savefig(PLOT_DIR / "Area Distribution.png")
    plt.show()
    #----------------------------------
    df["Price(USD)"].plot()
    plt.grid()
    plt.title("Price Distribution")
    plt.savefig(PLOT_DIR / "Price Distribution.png")
    plt.show()
    # ----------------------------------
    (
        df.groupby("AreaGrade")["Area"]
        .count()
        .plot(kind="pie", subplots=True, autopct="%1.2f%%", radius=1.5)
    )
    plt.show()
    plt.title("AreaGrade Distribution")
    plt.savefig(PLOT_DIR / "AreaGrade Distribution.png")
    plt.show()
    # ----------------------------------
    (
        df.groupby("Address")["Price(USD)"]
        .mean()
        .sort_values()
        .tail(30)
        .plot(kind="bar")
    )
    plt.grid()
    plt.title("Price of 30 Address")
    plt.savefig(PLOT_DIR / "Price of 30 Address.png")
    plt.show()
    # ----------------------------------
    sns.histplot(df["Area"], kde=True)
    plt.grid()
    plt.title("Area Count Distribution")
    plt.savefig(PLOT_DIR / "Area Count Distribution.png")
    plt.show()
    # ----------------------------------
    sns.histplot(df["Price(USD)"], kde=True)
    plt.grid()
    plt.title("Price Count Distribution")
    plt.savefig(PLOT_DIR / "Price Count Distribution.png")
    plt.show()
    # ----------------------------------
    sns.scatterplot(
        data=df,
        x="Area",
        y="Price(USD)"
    )
    plt.grid()
    plt.title("Price of Area Distribution")
    plt.savefig(PLOT_DIR / "Price of Area Distribution.png")
    plt.show()
    # ----------------------------------
    sns.scatterplot(
        data=df,
        x="AreaGrade",
        y="Price(meter²)"
    )
    plt.grid()
    plt.title("Price of AreaGrade meter²")
    plt.savefig(PLOT_DIR / "Price of AreaGrade meter².png")
    plt.show()
    # ----------------------------------
    sns.scatterplot(
        data=df,
        x="Area",
        y="Price(USD)",
        hue="Parking"
    )
    plt.grid()
    plt.title("Price of Area with Parking Distribution")
    plt.savefig(PLOT_DIR / "Price of Area with Parking Distribution.png")
    plt.show()
    # ----------------------------------
    sns.scatterplot(
        data=df,
        x="Area",
        y="Price(USD)",
        hue="Room"
    )
    plt.grid()
    plt.title("Price of Area with Room Distribution")
    plt.savefig(PLOT_DIR / "Price of Area with Room Distribution.png")
    plt.show()
    # ----------------------------------
    sns.barplot(
        data=df,
        x="Room",
        y="Price(USD)"
    )
    plt.grid()
    plt.title("Price of Room")
    plt.savefig(PLOT_DIR / "Price of Room.png")
    plt.show()
    # ----------------------------------
    sns.boxplot(
        data=df,
        x="Parking",
        y="Price(USD)"
    )
    plt.grid()
    plt.title("Price of Parking")
    plt.savefig(PLOT_DIR / "Price of Parking.png")
    plt.show()
    # ----------------------------------
    sns.boxplot(
        data=df,
        x="Elevator",
        y="Price(USD)"
    )
    plt.grid()
    plt.title("Price of Elevator")
    plt.savefig(PLOT_DIR / "Price of Elevator.png")
    plt.show()
    # ----------------------------------
    sns.boxplot(
        data=df,
        x="Warehouse",
        y="Price(USD)"
    )
    plt.grid()
    plt.title("Price of Warehouse")
    plt.savefig(PLOT_DIR / "Price of Warehouse.png")
    plt.show()
    # ----------------------------------
    sns.boxplot(
        data=df[df["Address"].isin(df["Address"].value_counts().head(10).index)],
        x="Address",
        y="Price(USD)"
    )
    plt.grid()
    plt.title("Price of 10 Address")
    plt.savefig(PLOT_DIR / "Price of 10 Address.png")
    plt.show()
    # ----------------------------------
    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True
    )
    plt.grid()
    plt.title("Solidarity Distribution")
    plt.savefig(PLOT_DIR / "Solidarity Distribution.png")
    plt.show()
    # ----------------------------------
    fig = px.scatter_3d(
        df,
        x="Area",
        y="Room",
        z="Price(USD)",
        color="Parking",
        title="Price of Area with Room"
    )
    fig.write_html(PLOT_DIR / "Price of Area with Room.html")
    fig.show()
    # ----------------------------------
    fig = px.scatter_3d(
        df,
        x="AreaGrade",
        y="Room",
        z="Price(meter²)",
        color="Parking",
        title="Price of AreaGrade meter² with Room"
    )
    fig.write_html(PLOT_DIR / "Price of AreaGrade meter² with Room.html")
    fig.show()
    # ----------------------------------
# ----------------------------------------------------------------------------------