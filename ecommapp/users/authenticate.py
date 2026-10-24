from django.contrib.auth.backends import ModelBackend
from . models import User

class Auth(ModelBackend):
    def authenticate(self, request, username=None, password =None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        user_password = user.check_password(password)

        user_is_active = self.user_can_authenticate(user)
        if user_password and user_is_active:
            return user
        return None

    def get_user(self, user_id):
      try:  
            user_i = User.objects.get(pk=user_id)
            if user_i:
                return user_i
      except User.DoesNotExist:
            raise Exception("User not available")