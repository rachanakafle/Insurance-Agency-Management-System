
from client.views import signin

from django.urls import path
app_name='client'

urlpatterns = [

    path('signin/', signin,name='signin'),
]
