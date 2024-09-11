from users.models import User

class RegistrationEmailService:
    
    def __init__(self, user: User):
        self.user = user