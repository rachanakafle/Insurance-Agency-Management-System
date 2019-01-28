from django.db import models

# Create your models here.
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
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
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
class Agent(models.Model):
        License_code = models.IntegerField(unique=True)
        Name = models.CharField(max_length=200, null=True, blank=True)
        Gender_choices = (('Male', 'MALE'), ('Female', 'FEMALE'))  # value ma agadi ko jancha paxi ko dispaly ma janxa
        gender = models.CharField(max_length=20, choices=Gender_choices, default=None)
        photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
        Temporary_Address = models.CharField(max_length=200)
        Permanent_address = models.CharField(max_length=200)
        # Birth_place=models.CharField(max_length=200)
        Contact_number = models.IntegerField()
        Email = models.EmailField(max_length=200, unique=True)
        password = models.CharField(max_length=200)
        Nationality = models.CharField(max_length=200)
        Education_level_choices = (('see', 'SEE'), ('Bachelors', 'BACHELORS'), ('Master', 'MASTER'))
        Education_level = models.CharField(max_length=200, choices=Education_level_choices, default=None)
        Citizenship = models.FileField(upload_to='uploads/',
                                       null=True, default="No file uploaded", blank=True)
        Citizenship_number = models.IntegerField(unique=True)
        Fathers_name = models.CharField(max_length=200)
        Mothers_name = models.CharField(max_length=200)
        Grandfathers_name = models.CharField(max_length=200)
        Name_of_institution = models.CharField(max_length=200, blank=True)
        Date_of_training = models.DateTimeField()
        location = models.CharField(blank=True, max_length=200)
        Bank_ac_no = models.IntegerField(max_length=None)
        Bank_branch_name = models.CharField(max_length=200)
        is_active = models.BooleanField(default=True)

        user = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                                 related_name="agents")

        def __str__(self):
            return self.Name


class Client(models.Model):
    Form_number = models.IntegerField(unique=True)
    Branch_name = models.CharField(max_length=200, null=True, blank=True)
    client_license_code = models.ForeignKey(Agent, on_delete=models.CASCADE, default=None,
                                            related_name='Client')
    Name = models.CharField(max_length=200, null=True, blank=True)
    Gender_choices = (('Male', 'MALE'), ('Female', 'FEMALE'))
    gender = models.CharField(max_length=20, choices=Gender_choices, default=None)
    photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
    Temporary_Address = models.CharField(max_length=200)
    Permanent_address = models.CharField(max_length=200)
    Contact_number = models.IntegerField()
    Email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    Nationality = models.CharField(max_length=200)
    Education_level_choices = (('see', 'SEE'), ('Bachelors', 'BACHELORS'), ('Master', 'MASTER'))
    Education_level = models.CharField(max_length=200, choices=Education_level_choices, default=None)
    Citizenship = models.FileField(upload_to='uploads/',
                                   null=True, default="No file uploaded", blank=True)
    Citizenship_number = models.IntegerField(unique=True)
    Company_name = models.CharField(max_length=200)
    Company_location = models.CharField(max_length=200)
    Income_source = models.BigIntegerField()
    Fathers_name = models.CharField(max_length=200)
    Mothers_name = models.CharField(max_length=200)
    Grandfathers_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                             related_name="clients")

    def __str__(self):
        return self.Name