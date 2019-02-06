from django.db import models

# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
from django.db import models
from django.contrib.auth.models import PermissionsMixin
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
                email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    agent = models.BooleanField(default=True)
    client= models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_approve=models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # @property
    # def is_agent(self):
    #     return self.agent
    #
    # @property
    # def is_client(self):
    #     return self.client
    #
    # def get_full_name(self):
    #     return self.full_name
