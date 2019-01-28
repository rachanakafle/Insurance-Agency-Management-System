from django.urls import path

from django.urls import path
from CMS.views import base,signin,signup,signout,agent,client
app_name='CMS'

urlpatterns = [
    path('', base,name='base'),
    path('signin/', signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('signout/', signout,name='signout'),
    path('agent/', agent,name="agentregister"),
    path('client/', client,name='clientregister'),


]

