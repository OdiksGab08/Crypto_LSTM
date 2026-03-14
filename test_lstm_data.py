from utils.data_fetcher import fetch_historical_data
from utils.helpers import scale_prices, create_sequences

# Fetch last 30 days data
df = fetch_historical_data("bitcoin", 30)

# Scale
scaler, scaled_prices = scale_prices(df['price'].values)

# Create sequences
X, y = create_sequences(scaled_prices, sequence_length=24)

print("X shape:", X.shape)
print("y shape:", y.shape)
print("First sequence:\n", X[0])
print("First target:", y[0])
