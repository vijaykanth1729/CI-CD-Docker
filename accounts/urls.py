from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('register/', signUp, name='register'),
    path('logout/',  auth_views.LogoutView.as_view(), name='logout'),
]
