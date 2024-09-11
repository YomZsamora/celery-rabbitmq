from users.models import User
from .email_service import send_email

class RegistrationEmailNotification:
    
    def __init__(self, user: User):
        self.user = user
        
    def send_registration_notification(self) -> None:
        
        mail_data = {
            "subject": "User Registration Confirmation",
            "message": "Your account has been successfully registered.",
            "recipients": [self.user.email]
        }
        send_email(mail_data)
        