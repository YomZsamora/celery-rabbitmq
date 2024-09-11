from users.models import User
from utils.exceptions.custom_exceptions import SerializerValidationsError

def email_validator(email: str):
    exists = User.objects.filter(email=email).exists()
    if exists:
        raise SerializerValidationsError(f"{email} already has an account registered.")
    return email    

def password_validator(password: str):
    requirements = {
        'digit': any(char.isdigit() for char in password),
        'lower_case': any(char.islower() for char in password),
        'upper_case': any(char.isupper() for char in password)
    }
    if not all(requirements.values()):
        raise SerializerValidationsError("Kindly provide a strong password.")
    return password