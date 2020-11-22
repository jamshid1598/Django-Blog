from django.urls import path

from .views import NewUserCreationForm

app_name = 'Members'

urlpatterns = [
    path('register/', NewUserCreationForm.as_view(), name='register'),
]