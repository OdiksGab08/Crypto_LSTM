# Crypto Prediction MVP 🚀

## Overview

**Crypto Prediction MVP** is a web-based machine learning application that predicts short-term cryptocurrency prices using historical market data and a Long Short-Term Memory (LSTM) neural network model.

The system retrieves cryptocurrency price data from the **CoinGecko API**, processes the data, feeds it into a trained LSTM model, and displays predictions through an interactive web interface built with **Flask** and **Chart.js**.

The application allows users to select different cryptocurrencies and view:

* Current market price
* Predicted next-day price
* 7-day price forecast
* Visual trend chart of predicted prices

This project demonstrates the integration of **data acquisition, machine learning, backend APIs, and frontend visualization** into a complete predictive analytics system.

---

# Features

* Real-time cryptocurrency price retrieval
* Historical market data collection
* Machine learning prediction using LSTM
* 7-day price forecasting
* Interactive data visualization with Chart.js
* Web-based user interface using Flask
* Support for multiple cryptocurrencies (Bitcoin, Ethereum, Solana, etc.)

---

# System Architecture

The system follows a **modular architecture**, separating responsibilities into different components.

```
Frontend (HTML + JavaScript)
        ↓
Flask Backend (API Routes)
        ↓
Data Fetcher (CoinGecko API)
        ↓
Data Preprocessing
        ↓
LSTM Model Prediction
        ↓
JSON Response
        ↓
Interactive Chart Visualization
```

---

# Project Structure

```
crypto-prediction-mvp/

app/
 ├── templates/
 │    └── index.html
 ├── static/
 └── app.py

models/
 ├── lstm_model.py
 ├── hybrid.py
 └── trained_models/
      └── lstm_crypto.h5

utils/
 ├── data_fetcher.py
 └── helpers.py

config/
 └── config.py

train_lstm.py
requirements.txt
README.md
```

### Description of Key Components

**app/app.py**

Main Flask backend application responsible for routing requests, interacting with the machine learning model, and returning predictions.

**utils/data_fetcher.py**

Handles API requests to retrieve cryptocurrency historical data and current prices from CoinGecko.

**models/lstm_model.py**

Contains the LSTM-based prediction logic used to forecast future prices.

**models/trained_models/**

Stores the trained machine learning model used during inference.

**train_lstm.py**

Script used to train the LSTM model on historical cryptocurrency data.

---

# Data Source

The project uses the **CoinGecko public REST API** to retrieve cryptocurrency data.

Example API endpoint:

```
https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart
```

Data retrieved includes:

* Historical price
* Market capitalization
* Trading volume

---

# Machine Learning Model

The system uses a **Long Short-Term Memory (LSTM) neural network**, a specialized type of Recurrent Neural Network (RNN) designed for time-series forecasting.

### Why LSTM?

Cryptocurrency prices are sequential and time-dependent. LSTM models can learn long-term patterns from historical data, making them suitable for financial time-series prediction.

### Model Workflow

1. Historical price data is collected.
2. Data is normalized using MinMaxScaler.
3. Time sequences are created (e.g., 60 days of past prices).
4. The LSTM model is trained to predict the next price value.
5. Predictions are generated for the next 7 days.

---

# Technologies Used

### Programming Language

* Python

### Backend Framework

* Flask

### Machine Learning

* TensorFlow / Keras
* NumPy
* Pandas
* Scikit-learn

### Data Visualization

* Chart.js

### API

* CoinGecko Cryptocurrency API

---

# Installation

## 1. Clone the Repository

```
git clone https://github.com/yourusername/crypto-prediction-mvp.git
cd crypto-prediction-mvp
```

## 2. Create a Virtual Environment

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# Running the Application

Start the Flask server:

```
python app/app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

You will see the crypto prediction dashboard.

---

# Example Workflow

1. User selects a cryptocurrency.
2. The system fetches historical data from CoinGecko.
3. Data is processed and passed into the LSTM model.
4. The model predicts the next 7 days of prices.
5. Results are returned to the frontend.
6. Predictions are displayed as an interactive chart.

---

# Limitations

* Cryptocurrency markets are highly volatile and unpredictable.
* Predictions are based only on historical price patterns.
* External factors such as news, regulations, or macroeconomic events are not included.

This system is intended for **educational and research purposes only**.

---

# Future Improvements

Possible enhancements include:

* Integration of additional technical indicators (RSI, MACD, Moving Averages)
* Support for more cryptocurrencies
* Real-time streaming market data
* Advanced models such as Transformer or Hybrid CNN-LSTM
* Deployment to cloud platforms

---

# License

This project is released for academic and educational purposes.

---

# Author

Developed as a **Cryptocurrency Price Prediction System using Machine Learning**.

---
