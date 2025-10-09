# 🌡️ NYC January Temperature Trend Analysis

This project explores long-term temperature trends in New York City during January, using historical data from 1895 to 2018. It applies regression modeling and visualization techniques to analyze climate patterns and predict future temperatures.

---

## 📁 Dataset

- **Source**: `ave_hi_nyc_jan_1895-2018.csv`
- **Fields**:
  - `Date`: Year and month in `YYYYMM` format
  - `Value`: Average high temperature in °F
  - `Anomaly`: Deviation from the long-term average temperature (in °F)


---

## 🧪 Methodology

### 1. Data Cleaning
- Converted `Date` from `YYYYMM` to `YYYY`
- Renamed `Value` to `Temperature` for clarity

### 2. Regression Modeling
- **SciPy `linregress`**: Quick slope and intercept estimation
- **Scikit-learn `LinearRegression`**:
  - Train/test split (75/25)
  - Model training and prediction
  - Evaluation using actual vs predicted comparison

### 3. Predictions
- **2024 Forecast**:
  - SciPy: 38.59°F
  - Scikit-learn: 38.94°F
- **1890 Backcast**:
  - Scikit-learn: 34.83°F

---

## 📊 Visualizations

- Scatter plots of actual temperature data
- Regression line overlay
- Highlighted predictions for 2024 and 1890

---

## 🔍 Key Findings

- NYC January temperatures show a **consistent warming trend** over the past century.
- Forecasts for 2024 suggest continued warming, with average highs nearing 39°F.
- Backcasting to 1890 reveals significantly cooler winters, reinforcing the long-term climate shift.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- SciPy
- Scikit-learn

---

## 🚀 How to Run

1. git clone https://github.com/YOUR_USERNAME/datafun-07-ml.git
2. cd datafun-07-ml
