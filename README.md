# Tehran House Prices Analysis

Exploratory Data Analysis (EDA) and data preprocessing pipeline for the Tehran House Prices dataset using Python.

The project focuses on cleaning raw housing data, generating meaningful features, and visualizing the dataset to better understand the relationships between different attributes before applying Machine Learning models.

---

## Features

- Dataset loading
- Data cleaning
- Missing value handling
- Outlier detection (IQR)
- Feature engineering
- Statistical analysis
- Data visualization
- Export processed datasets

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

---

## Project Structure

```
TehranHousePrices/
│
├── data/
│   ├── *.png
│   └── *.html
│
├── dataset/
│   ├── TehranHousePrice.csv
│   ├── clean_dataset.csv
│   └── sample.csv
│
├── src/
│   ├── main.py
│   ├── dataset.py
│   ├── analysis.py
│   ├── visualization.py
│   └── utils.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Generated Features

The preprocessing pipeline creates additional features including:

- Price Grade
- Area Grade
- Price per Square Meter
- Neighborhood Average Price

---

## Usage

Clone the repository:

```bash
git clone https://github.com/mohamadali-bl/tehran-house-prices-analysis.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python src/main.py
```

---

## Future Work

- Machine Learning models
- Price prediction
- Model evaluation
- Hyperparameter tuning

---

## Sample Visualizations

### Area Distribution

![](data/Area%20Distribution.png)

---

### Price Distribution

![](data/Price%20Distribution.png)

---

### Correlation Heatmap

![](data/Solidarity%20Distribution.png)

---

### Top 30 Neighborhood Prices

![](data/Price%20of%2030%20Address.png)

---

## License

This project is licensed under the MIT License.
