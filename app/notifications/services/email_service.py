from users.models import User
from django.conf import settings
from django.core.mail import EmailMessage
from celery import shared_task

class RegistrationEmailNotification:
    
    def __init__(self, user: User):
        self.user = user
        
    def send_registration_notification(self) -> None:
        
        mail_data = {
            "subject": "User Registration Confirmation",
            "message": "Your account has been successfully registered."
        }
        self.__send_email(mail_data)
        
    
    @shared_task
    def __send_email(self, mail_data: dict[str, any]) -> None:
        
        email = EmailMessage(
            mail_data['subject'], 
            mail_data['message'], 
            settings.DEFAULT_FROM_EMAIL, 
            [self.user.email]
        )
        email.send()    
    