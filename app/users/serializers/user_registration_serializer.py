from rest_framework import serializers
from users.models import User
from users.validators import email_validator, password_validator
from notifications.services import RegistrationEmailNotification

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    email = serializers.EmailField(max_length=100, validators=[email_validator])
    password = serializers.CharField(write_only=True, validators=[password_validator])

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        
        user = User(email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def send_notification(self, user: User) -> None:
        
        email_service = RegistrationEmailNotification(user)
        email_service.send_registration_notification()
