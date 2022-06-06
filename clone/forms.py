from django import forms
from .models import Profile, Image, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method= 'POST'
    helper.add_input(Submit('post','post',css_class='btn-primary'
    ))

    class Meta:
        model=Post
        fields = [
            'image',
            'caption',
        ]
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo']



