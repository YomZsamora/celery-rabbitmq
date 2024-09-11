from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
    
@shared_task
def send_email(mail_data: dict[str, any]) -> None:
    
    """
    Asynchronous task that sends an email using Django's EmailMessage class.
    Args: mail_data (dict): A dictionary containing email data.
    - 'subject': Subject of the email (str)
    - 'message': Body of the email (str)
    - 'recipients': List of recipient email addresses (list)
    Returns: None
    """
    
    email = EmailMessage(
        mail_data['subject'], 
        mail_data['message'], 
        settings.DEFAULT_FROM_EMAIL, 
        mail_data['recipients']
    )
    email.send()    
    