from agent.views import signin

from django.urls import path
app_name='agent'

urlpatterns = [

    path('signin/', signin,name='signin'),
]
