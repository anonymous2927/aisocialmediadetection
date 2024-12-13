import os

class Config:
    # Secret key to secure the session, cookies, etc.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-hard-to-guess-secret-key'

    # Database configuration (using SQLite as an example)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for performance reasons

    # Email configuration (for sending OTPs)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Set this to your Gmail username
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Set this to your Gmail password
    MAIL_DEFAULT_SENDER = 'your_email@example.com'  # Set your default sender email address

    # Stripe or Payment Gateway Configuration
    STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY')  # Add your Stripe API key if you're using Stripe
    # OR use Paytm API credentials if you're integrating Paytm for payments
    PAYTM_MERCHANT_KEY = os.environ.get('PAYTM_MERCHANT_KEY')  # Example placeholder for Paytm key

    # Additional configurations can be added here as needed
