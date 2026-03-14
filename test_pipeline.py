# ==========================================
# TEST ENTIRE LSTM PIPELINE
# ==========================================

from utils.data_fetcher import fetch_historical_data
from utils.helpers import scale_prices, create_sequences
from models.lstm_model import create_lstm_model, train_lstm_model, save_model, load_lstm_model
import numpy as np
import os

# ------------------------------
# Step 1: Fetch historical data
# ------------------------------
print("Fetching historical data...")
df = fetch_historical_data("bitcoin", days=30, interval="daily")
print("Data fetched successfully!")
print("Data shape:", df.shape)
print(df.head(), "\n")

# ------------------------------
# Step 2: Scale prices
# ------------------------------
print("Scaling prices...")
prices = df['price'].values
scaler, scaled_prices = scale_prices(prices)
print("First 5 scaled prices:", scaled_prices[:5])
print("Min:", scaled_prices.min(), "Max:", scaled_prices.max(), "\n")

# ------------------------------
# Step 3: Create sequences
# ------------------------------
print("Creating sequences for LSTM...")
X, y = create_sequences(scaled_prices, sequence_length=24)
print("X shape:", X.shape)
print("y shape:", y.shape)
print("First sequence:\n", X[0])
print("First target:", y[0], "\n")

# ------------------------------
# Step 4: Build LSTM model
# ------------------------------
print("Building LSTM model...")
model = create_lstm_model(input_shape=(X.shape[1], 1))
model.summary()

# ------------------------------
# Step 5: Quick training test (1 epoch)
# ------------------------------
print("Training model for 1 epoch as test...")
train_lstm_model(model, X, y, epochs=1, batch_size=16)
print("Training test completed!\n")

# ------------------------------
# Step 6: Save and load model
# ------------------------------
print("Saving model...")
save_model(model, "test_lstm.h5")
print("Loading model...")
model_loaded = load_lstm_model("test_lstm.h5")
model_loaded.summary()
print("Model save/load successful!\n")

# ------------------------------
# Step 7: Make prediction
# ------------------------------
print("Making prediction with last sequence...")
sample_input = X[-1].reshape(1, X.shape[1], 1)
pred_scaled = model_loaded.predict(sample_input)
pred_price = scaler.inverse_transform(pred_scaled)
print("Scaled prediction:", pred_scaled)
print("Predicted price in USD:", pred_price[0][0])
