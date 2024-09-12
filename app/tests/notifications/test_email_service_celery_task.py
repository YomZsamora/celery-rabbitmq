from unittest import mock
from core.settings import DEFAULT_FROM_EMAIL
from notifications.services import send_email
from tests.abstract_api_test import AbstractAPITest

class EmailServiceCeleryTaskTest(AbstractAPITest):
    
    urlpatterns = []
    
    def setUp(self) -> None:
        super().setUp()
        self.seed_registered_user()
        self.mail_data = {
            "subject": "Test Subject",
            "message": "Test Message",
            "recipients": [self.registered_user.email]
        }
        
    def test_send_email(self):
        
        with mock.patch('notifications.services.email_service.EmailMessage') as mock_send_email:
            
            send_email(self.mail_data)
            mock_send_email.assert_called_once_with(
                self.mail_data['subject'],
                self.mail_data['message'],
                DEFAULT_FROM_EMAIL,  
                self.mail_data['recipients']
            )
            