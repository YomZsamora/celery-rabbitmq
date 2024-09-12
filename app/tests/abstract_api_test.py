from faker import Faker
from users.models import User
from rest_framework.test import APITestCase, URLPatternsTestCase

class AbstractAPITest(APITestCase, URLPatternsTestCase):
    
    def setUp(self) -> None:
        self.fake = Faker()
        
    def seed_registered_user(self):
        self.registered_user = User.objects.create(
            email=self.fake.email(),
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            password=self.fake.password()
        )
    