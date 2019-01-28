from django.contrib import admin

# Register your models here.
from policy.models import Policy, Applied_Policy

admin.site.register(Policy)
admin.site.register( Applied_Policy)