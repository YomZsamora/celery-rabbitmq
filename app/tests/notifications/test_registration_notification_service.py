from unittest import mock
from tests.abstract_api_test import AbstractAPITest
from notifications.services import RegistrationEmailNotification

class UserRegistrationServiceTest(AbstractAPITest):
    
    urlpatterns = []
    
    def setUp(self) -> None:
        super().setUp()
        self.seed_registered_user()
        
    def test_send_registration_notification(self):
        
        email_notification = RegistrationEmailNotification(self.registered_user)
        with mock.patch('notifications.services.email_service.send_email.delay') as mock_send_email:
            
            email_notification.send_registration_notification()
            
            expected_mail_data = {
                "subject": "User Registration Confirmation",
                "message": "Your account has been successfully registered.",
                "recipients": [self.registered_user.email]
            }
            
            mock_send_email.assert_called_once_with(expected_mail_data)
            