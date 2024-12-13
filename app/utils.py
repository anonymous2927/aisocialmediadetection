from flask_mail import Message
from app import mail

def send_otp(email, otp):
    msg = Message('Your OTP', sender='your-email@gmail.com', recipients=[email])
    msg.body = f"Your OTP is {otp}"
    mail.send(msg)

def analyze_profile(profile_id):
    # Placeholder for ML-based profile analysis
    return "Scam detected" if "scam" in profile_id.lower() else "Safe"
