from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class Add_newnote_form(forms.ModelForm):
    user_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Content
        fields = ['title', 'text', 'user_id']
        # exclude = ['user_id']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'named'}),
            'text': forms.Textarea(attrs={'class': 'input-text'}),
        }


class Task_form(forms.ModelForm):
    user_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Tasks_model
        fields = ['text', 'user_id']
        widgets = {
            'text': forms.TextInput(attrs={'id': 'task-field'}),
        }





class Registration_form(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-field'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-field'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-field'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Login_form(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-field'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-field'}))


