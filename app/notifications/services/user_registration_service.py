from users.models import User
from .email_service import send_email

class RegistrationEmailNotification:
    
    """
    A service to handle sending registration email notifications to users.
    Attributes:  user (User): The user for whom the registration email notification is intended.
    """
    
    def __init__(self, user: User):
        
        """
        Initializes a RegistrationEmailNotification object with the specified user.
        Args: user (User): The user for whom the registration email notification will be sent.
        """
        
        self.user = user
        
    def send_registration_notification(self) -> None:
        
        """
        Sends a registration email notification to the user using a background task.
        Constructs the email data and delegates the email sending to email service.
        """
        
        mail_data = {
            "subject": "User Registration Confirmation",
            "message": "Your account has been successfully registered.",
            "recipients": [self.user.email]
        }
        send_email.delay(mail_data)
        