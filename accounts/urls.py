# accounts/urls.py
from django.urls import path
from accounts.views import SignUpView

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
