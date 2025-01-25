from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email']


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['city', 'phone_number', 'image']