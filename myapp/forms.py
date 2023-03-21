from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
class Students(forms.Form):
    name=forms.CharField(max_length=20)
    roll_no=forms.CharField(max_length=20)
    address=forms.TextInput()

class UserRegForm(UserCreationForm):
    user_type=forms.ChoiceField(choices=(('admin','Admin Staff'),('superuser','Superuser')))
    is_active=forms.BooleanField(required=False)
    class Meta:
        model = User
        fields =['username','email','password1', 'password2', 'user_type', 'is_active']
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
            'password2':None,
        }
