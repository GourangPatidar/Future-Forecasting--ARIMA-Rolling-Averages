
---

# Future Forecasting: ARIMA, Rolling Averages, and A/B Testing

## Introduction
In this project, we explore various techniques for forecasting future trends in time-series data. We primarily focus on three methods:

1. ARIMA (AutoRegressive Integrated Moving Average) models
2. Rolling averages
3. A/B testing for analyzing the impact of interventions or changes in the data.

## Project Overview
This project aims to provide a comprehensive understanding of time-series forecasting and the application of statistical methods to predict future trends. By using ARIMA models, rolling averages, and A/B testing, we can analyze past data to make informed predictions and assess the impact of changes or interventions.

## Methods

### 1. ARIMA Models
ARIMA models are powerful tools for time-series forecasting. They combine three components:
- **AutoRegressive (AR)**: Uses the dependency between an observation and a number of lagged observations (i.e., previous values).
- **Integrated (I)**: Uses differencing of raw observations to make the time series stationary.
- **Moving Average (MA)**: Uses the dependency between an observation and a residual error from a moving average model applied to lagged observations.

In this project, we demonstrate how to build and evaluate ARIMA models for forecasting future values in time-series data.

### 2. Rolling Averages
Rolling averages are used to smooth out short-term fluctuations and highlight longer-term trends or cycles. By calculating the average of the data points within a specified window, rolling averages provide a clearer view of the underlying trends in the data.

We implement rolling averages to analyze and forecast trends, demonstrating how to apply this method to various datasets.

### 3. A/B Testing
A/B testing is a statistical method used to compare two or more groups to determine if there are any significant differences between them. This technique is often used in marketing and product development to test the impact of changes or interventions.

In this project, we perform A/B testing to analyze the effect of different interventions on the time-series data, providing insights into how changes can impact future trends.

## Project Structure
- **AssignmentData.xlsx**: Contains the dataset used for analysis and forecasting.
- **GOURANG PATIDAR 17-03-2024.ipynb**: Jupyter notebook containing the implementation and analysis of ARIMA models, rolling averages, and A/B testing.
- **Guided Assessment.ipynb**: Jupyter notebook providing a guided assessment of the forecasting techniques.
- **LICENSE**: License information for the project.
- **README.md**: Project documentation (this file).
- **Streamlit.py**: Script for deploying the forecasting models and analysis using Streamlit.

## Installation and Setup
To run the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/GourangPatidar/Future-Forecasting--ARIMA-Rolling-Averages-and-A-B-Testing.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd Future-Forecasting--ARIMA-Rolling-Averages-and-A-B-Testing
    ```


## Usage
To explore the forecasting techniques and perform analysis:

1. **Open the Jupyter notebooks**:
    - `GOURANG PATIDAR 17-03-2024.ipynb`: Contains detailed implementation and analysis.
    - `Guided Assessment.ipynb`: Provides a guided assessment of the techniques.
2. **Run the Streamlit application**:
    ```bash
    streamlit run Streamlit.py
    ```
    Follow the instructions in the application to interact with the forecasting models and analyze the results.

## Evaluation
The project includes evaluation metrics and visualizations to assess the performance of the forecasting models and the impact of interventions. These evaluations help in understanding the effectiveness of different techniques and their applicability to various datasets.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
Special thanks to the developers and contributors of the libraries and tools used in this project, including pandas, NumPy, statsmodels, and Streamlit.

## Contact
For any queries or issues, please contact Gourang Patidar at gourangpatidar2003@gmail.com

---

