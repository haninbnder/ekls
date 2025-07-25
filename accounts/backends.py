from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if username:
            try:
                if username.startswith('05'):
                    user = UserModel.objects.get(phone_number=username)
                else:
                    user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return None

            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None
