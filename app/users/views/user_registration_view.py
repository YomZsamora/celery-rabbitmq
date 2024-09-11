from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from users.serializers import UserRegistrationSerializer
from utils.exceptions.custom_exceptions import SerializerValidationsError

class UserRegistrationView(APIView):
    
    """
    API view for handling POST requests for user registration.
    """

    def post(self, request: Request) -> Response:
        
        """
        Handles POST requests to register a new user.
        Args: request: Request object containing user registration data.
        Returns: Response: JSON response confirming successful registration or error details.
        Raises: SerializerValidationsError: If serializer validation fails.
        """
        
        serializer = UserRegistrationSerializer(data=request.data)
        self._validate_serializer(serializer)
        user = serializer.save()
        return Response({"message": f"{user.email} has been registered successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
    
    def _validate_serializer(self, serializer):
        
        """
        Validates the serializer and raises an exception if it is not valid.
        Args: serializer: The serializer instance.
        Raises: SerializersValidationError: If the serializer is not valid.
        """
        
        if not serializer.is_valid():
            raise SerializerValidationsError(
                message="An error occured while registering new account.",
                detail=[serializer.errors]
            )
