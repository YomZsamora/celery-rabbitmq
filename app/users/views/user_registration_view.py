from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserRegistrationSerializer

class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            # Create user
            user = serializer.save()
            # Send notification
            serializer.send_notification(user)
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
