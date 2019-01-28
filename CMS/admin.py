from django.contrib import admin

# Register your models here.
from CMS.models import MyUser, Client,Agent

admin.site.register(MyUser)
admin.site.register(Agent)
admin.site.register(Client)
