import numpy as np
from sklearn.preprocessing import MinMaxScaler


def scale_prices(prices):
    """
    Scale price series to range [0,1] for LSTM training.

    Args:
        prices (numpy.array or list): Raw price series

    Returns:
        scaler: Fitted MinMaxScaler
        scaled_prices: Numpy array of scaled prices
    """
    # Reshape to 2D because scaler expects 2D input
    prices = np.array(prices).reshape(-1, 1)

    # Create scaler object
    scaler = MinMaxScaler(feature_range=(0, 1))

    # Fit scaler and transform prices
    scaled_prices = scaler.fit_transform(prices)

    return scaler, scaled_prices


def create_sequences(scaled_prices, sequence_length=24):
    """
    Convert scaled prices into sequences for LSTM training.

    Args:
        scaled_prices (numpy.array): Array of scaled prices
        sequence_length (int): Number of timesteps per input sequence

    Returns:
        X: Input sequences (samples, timesteps, features)
        y: Corresponding next-step outputs
    """
    X = []
    y = []

    for i in range(sequence_length, len(scaled_prices)):
        X.append(scaled_prices[i-sequence_length:i, 0])
        y.append(scaled_prices[i, 0])

    # Convert to numpy arrays
    X = np.array(X)
    y = np.array(y)

    # Reshape X for LSTM: (samples, timesteps, features)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    return X, y
