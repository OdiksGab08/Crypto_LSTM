"""
lstm_model.py
----------------------------------
Handles LSTM training & forecasting
----------------------------------
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
#from tensorflow.keras.layers import Bidirectional, Dense, Dropout #for advanced model


def create_sequences(data, sequence_length=10):
    X = []
    y = []

    for i in range(len(data) - sequence_length):
        X.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])

    return np.array(X), np.array(y)


def predict_next_days(df, days=7):

    prices = df["price"].values.reshape(-1, 1)

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(prices)

    sequence_length = 10
    X, y = create_sequences(scaled_data, sequence_length)

    model = Sequential([
        LSTM(50, return_sequences=False, input_shape=(sequence_length, 1)),
        Dense(1)
    ])

    model.compile(optimizer="adam", loss="mse")
    model.fit(X, y, epochs=5, batch_size=16, verbose=0)

    last_sequence = scaled_data[-sequence_length:]
    forecast = []

    for _ in range(days):
        prediction = model.predict(
            last_sequence.reshape(1, sequence_length, 1),
            verbose=0
        )

        forecast.append(prediction[0][0])

        last_sequence = np.append(
            last_sequence[1:],
            prediction,
            axis=0
        )

    forecast = scaler.inverse_transform(
        np.array(forecast).reshape(-1, 1)
    )

    forecast = forecast.flatten().tolist()

    dates = pd.date_range(
        start=df["date"].iloc[-1],
        periods=days+1
    )[1:]

    dates = [str(date.date()) for date in dates]

    return forecast, dates