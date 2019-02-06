

from django.contrib import admin

# Register your models here.
from account.models import MyUser

admin.site.register(MyUser)


