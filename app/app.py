# CRYPTO PREDICTION APP


from flask import Flask, render_template, request, jsonify
from utils.data_fetcher import fetch_historical_data, fetch_current_price
from models.lstm_model import predict_next_days

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    crypto = request.json["crypto"]

    # Fetch historical data
    df = fetch_historical_data(crypto, 60)

    # Fetch LIVE current price
    current_price = fetch_current_price(crypto)

    # Predict next 7 days
    forecast, dates = predict_next_days(df, days=7)

    return jsonify({
        #"crypto": crypto,
        "current_price": current_price,
        "next_prediction": forecast[0],
        "forecast": forecast,
        "dates": dates
    })


if __name__ == "__main__":
    app.run(debug=True)