from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone, password, **kwargs):
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **kwargs):
        user = self.create_user(phone, password, **kwargs)
        user.is_superuser = True
        user.save()
        return user
