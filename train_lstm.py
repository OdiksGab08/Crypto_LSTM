from utils.data_fetcher import fetch_historical_data
from utils.helpers import scale_prices, create_sequences
from models.lstm_model import create_lstm_model, train_lstm_model, save_model

# Fetch data
df = fetch_historical_data("bitcoin", days=60, interval="daily")
prices = df['price'].values

# Scale prices
scaler, scaled_prices = scale_prices(prices)

# Create sequences (24 timesteps)
X, y = create_sequences(scaled_prices, sequence_length=24)

# Build model
model = create_lstm_model(input_shape=(X.shape[1], 1))

# Train model
train_lstm_model(model, X, y, epochs=50, batch_size=16)

# Save model
save_model(model)
