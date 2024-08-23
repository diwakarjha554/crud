from django.urls import path
from authentication.views import *

urlpatterns = [
    path('register/', userRegistration, name='register'),
    path('login/', userLogin, name='login'),
]
