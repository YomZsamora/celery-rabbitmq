from rest_framework import serializers
from users.models import User
from django.db import transaction
from users.validators import email_validator, password_validator
from notifications.services import RegistrationEmailNotification

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    """
    Serializer for handling user registration.
    """
    
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    email = serializers.EmailField(max_length=100, validators=[email_validator])
    password = serializers.CharField(write_only=True, validators=[password_validator])
    last_login = serializers.ReadOnlyField(default=None)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'last_login']

    def create(self, validated_data):
        
        """
        Create a new user with the provided validated data.
        Args: validated_data (dict): Validated data for user creation.
        Returns: User: Newly created user instance.
        """
        
        with transaction.atomic():
            user = User(email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
            user.set_password(validated_data['password'])
            user.save()
            transaction.on_commit(lambda: self.send_notification(user))
            
        return user

    def send_notification(self, user: User) -> None:
        
        """
        Send registration notification email to the user.
        Args: user (User): The user object to notify.
        """
        
        email_service = RegistrationEmailNotification(user)
        email_service.send_registration_notification()
