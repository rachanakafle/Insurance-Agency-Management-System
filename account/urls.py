from django.urls import path

from account.views import signin, base, signout, signup
app_name="account"

urlpatterns = [
    path('signin/', signin,name='signin'),
    path('signup/', signup,name='signup'),
    path('',base,name="home"),
    path('signout',signout,name='signout')
    ]