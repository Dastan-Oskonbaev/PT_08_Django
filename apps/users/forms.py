from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email']
