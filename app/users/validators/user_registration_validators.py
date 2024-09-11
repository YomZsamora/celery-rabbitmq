from users.models import User
from utils.exceptions.custom_exceptions import SerializerValidationsError

def email_validator(email: str):
    if User.objects.filter(email=email).exists():
        raise SerializerValidationsError(f"{email} already has an account.")
    return email

def password_validator(password: str):
    if not (any(c.isdigit() for c in password) and any(c.islower() for c in password) and any(c.isupper() for c in password)):
        raise SerializerValidationsError("Password must contain at least one uppercase, lowercase, and digit.")
    return password
