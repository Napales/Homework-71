from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class MyUserCreationForm(UserCreationForm):
    avatar = forms.ImageField()
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  'first_name',
                  'description',
                  'gender',
                  'avatar']
