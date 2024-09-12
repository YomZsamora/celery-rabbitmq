import json
from unittest import mock
from users.models import User
from rest_framework import status
from unittest.mock import MagicMock
from django.urls import path, include, reverse
from tests.abstract_api_test import AbstractAPITest
from users.serializers import UserRegistrationSerializer

class MockUserRegistrationService:
    
    def __enter__(self):
        self.email_service_instance = MagicMock()
        return self.email_service_instance

    def __exit__(self, *args):
        pass

    def __call__(self, *args, **kwargs):
        return self

class UserRegistrationAPITest(AbstractAPITest):
    
    urlpatterns = [
        path('v1/users/', include('users.urls'))
    ]
    
    def setUp(self) -> None:
        super().setUp()
        self.user_email = self.fake.email()
        self.payload = {
            "email": self.user_email,
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "password": "@MyPassword2024"
        }
        
    def test_user_registration_successful(self):
        
        with mock.patch('notifications.services.user_registration_service.RegistrationEmailNotification.send_registration_notification', new_callable=MockUserRegistrationService):
        
            response = self.client.post(reverse("user-registration"), json.dumps( self.payload), content_type="application/json")
            
            assert response.status_code == status.HTTP_201_CREATED
            assert response.data['message'] == f"{self.user_email} has been registered successfully!"
            
            response_data = response.data['data']
            registered_user = User.objects.get(email=response_data["email"])
            
            assert str(registered_user) == self.user_email
                 
            assert response_data['email'] == registered_user.email
            assert response_data['first_name'] == registered_user.first_name
            assert response_data['last_name'] == registered_user.last_name
            assert response_data['last_login'] == registered_user.last_login

    def test_required_fields_exception_raised(self):
        
        self.payload = {}
        serializer = UserRegistrationSerializer(data=self.payload)
        is_valid = serializer.is_valid()
        errors = serializer.errors
        
        assert not is_valid
        assert errors['email'][0] == "This field is required."
        assert errors['password'][0] == "This field is required."
        assert errors['first_name'][0] == "This field is required."
        assert errors['last_name'][0] == "This field is required."
        
    def test_existing_or_registered_email_exception_raised(self):
        
        self.seed_registered_user()
        self.payload['email'] = self.registered_user.email
        
        response = self.client.post(reverse("user-registration"), json.dumps( self.payload), content_type="application/json")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['message'] == f"{self.registered_user.email} already has an account registered."
        
    def test_weak_password_exception_raised(self):
        
        self.payload["password"] = "password"
        
        response = self.client.post(reverse("user-registration"), json.dumps( self.payload), content_type="application/json")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['message'] == "Password must contain at least one uppercase, lowercase, and digit."
        
        