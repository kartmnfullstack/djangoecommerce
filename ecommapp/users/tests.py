from django.test import TestCase,SimpleTestCase
from django.urls import resolve,reverse
from users.models import User
from users.views import signin,register

#unit testing for user registration
class UserRegistrationTesting(TestCase):
    def test_input_fields(self):
        user = User(username="Test2",email="test@gmail.com",first_name="a",last_name="b")
        self.assertEqual(user.username,"Test2")
        self.assertEqual(user.email,"test@gmail.com")
        self.assertEqual(user.first_name,"a")
        self.assertEqual(user.last_name,"b")

    def test_user_display(self):
        user = User(username="Test2",email="test@gmail.com",first_name="a",last_name="b")
        display = user.__str__()
        self.assertEqual(display,"test@gmail.com")

    def test_register_view_ping(self):
        res = self.client.get("/register")
        self.assertEqual(res.status_code,200)
    
    def test_login_view_ping(self):
        res = self.client.get("/login")
        self.assertEqual(res.status_code,200)

    def test_register_view_content(self):
        res = self.client.get("/register")
        self.assertTemplateUsed(res,"pages/register.html")

    def test_login_view_content(self):
        res = self.client.get("/login")
        self.assertTemplateUsed(res,"pages/login.html")

#unit testing for user registration and login url testing
class RegistrationandLoginUrlTesting(SimpleTestCase):
    def test_register_url(self):
        url_link = reverse('register')
        self.assertEqual(resolve(url_link).func,register)

    def test_login_url(self):
        url_link = reverse('login')
        self.assertEqual(resolve(url_link).func,signin)
    
        
