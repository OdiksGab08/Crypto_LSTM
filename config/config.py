import os
import serects
from dotenv import load_dotenv
load_dotenv()
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'production')
    FLASK_APP = os.environ.get('FLASK_APP', 'app')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', '0')
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', '1')
    SESSION_COOKIE_HTTPONLY = os.environ.get('SESSION_COOKIE_HTTPONLY', '1')
    SESSION_COOKIE_SAMESITE = os.environ.get('SESSION_COOKIE_SAMESITE', 'Lax')
    SESSION_COOKIE_DOMAIN = os.environ.get('SESSION_COOKIE_DOMAIN', None)
    SESSION_COOKIE_PATH = os.environ.get('SESSION_COOKIE_PATH', '/')
    SESSION_COOKIE_MAX_AGE = os.environ.get('SESSION_COOKIE_MAX_AGE', None)
    SESSION_COOKIE_SAMESITE = os.environ.get('SESSION_COOKIE_SAMESITE', 'Lax')
    PREDICTION_MODEL_PATH = os.environ.get('PREDICTION_MODEL_PATH', 'models/lstm_model.h5')
    PREDICTION_SCALER_PATH = os.environ.get('PREDICTION_SCALER_PATH', 'models/scaler.pkl')
    PREDICTION_MODEL_PATH = os.environ.get('PREDICTION_MODEL_PATH', 'models/lstm_model.h5')
    PREDICTION_SCALER_PATH = os.environ.get('PREDICTION_SCALER_PATH', 'models/scaler.pkl')
    PREDICTION_MODEL_PATH = os.environ.get('PREDICTION_MODEL_PATH', 'models/lstm_model.h5')
    PREDICTION_SCALER_PATH = os.environ.get('PREDICTION_SCALER_PATH', 'models/scaler.pkl')
    PREDICTION_MODEL_PATH = os.environ.get('PREDICTION_MODEL_PATH', 'models/lstm_model.h5')
    PREDICTION_SCALER_PATH = os.environ.get('PREDICTION_SCALER_PATH', 'models/scaler.pkl')
    PREDICTION_MODEL_PATH = os.environ.get('PREDICTION_MODEL_PATH', 'models/lstm_model.h5')
    PREDICTION_SCALER_PATH = os.environ.get('PREDICTION_SCALER_PATH', 'models/scaler.pkl')
    