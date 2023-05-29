from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import*
from django.db import transaction



class ManagerSignUpForm(UserCreationForm):
    attrs_first_name = {'class': 'form-control', 'placeholder': 'first name'}

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs=attrs_first_name)
    )
    attrs_last_name = {'class': 'form-control', 'placeholder': 'last name'}

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs=attrs_last_name)
    )
    attrs_username = {'class': 'form-control', 'placeholder': 'user name'}

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs_username)
    )

    attrs_email = {'class': 'form-control', 'placeholder': '000@ecx.sa'}
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs=attrs_email)
    )
    attrs_password1 = {'class': 'form-control', 'placeholder': 'password'}

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs_password1)

    )
    attrs_password2 = {'class': 'form-control', 'placeholder': 'password'}

    password2 = forms.CharField(
        label='Password Confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs_password2)

    )

    class Meta(UserCreationForm.Meta):
      model = Employee
      fields = ('first_name', 'last_name', 'username','email')






class HospitalSignUpForm(UserCreationForm):
    attrs_first_name = {'class': 'form-control', 'placeholder': 'first name'}

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs=attrs_first_name)
    )
    attrs_last_name = {'class': 'form-control', 'placeholder': 'last name'}

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs=attrs_last_name)
    )
    attrs_username = {'class': 'form-control', 'placeholder': 'user name'}

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs_username)
    )

    attrs_email = {'class': 'form-control', 'placeholder': '000@ecx.sa'}
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs=attrs_email)
    )
    attrs_password1 = {'class': 'form-control', 'placeholder': 'password'}

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs_password1)

    )
    attrs_password2 = {'class': 'form-control', 'placeholder': 'password'}

    password2 = forms.CharField(
        label='Password Confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs_password2)

    )

    class Meta(UserCreationForm.Meta):
      model = Hospital
      fields = ('first_name', 'last_name', 'username','email')

class EmployeeSignUpForm(UserCreationForm):
    attrs_first_name = {'class': 'form-control', 'placeholder': 'first name'}

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs=attrs_first_name)
    )
    attrs_last_name = {'class': 'form-control', 'placeholder': 'last name'}

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs=attrs_last_name)
    )
    attrs_username = {'class': 'form-control', 'placeholder': 'user name'}

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs_username)
    )

    attrs_email = {'class': 'form-control', 'placeholder': '000@ecx.sa'}
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs=attrs_email)
    )
    attrs_password1 = {'class': 'form-control', 'placeholder': 'password'}

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs_password1)

    )
    attrs_password2 = {'class': 'form-control', 'placeholder': 'password'}

    password2 = forms.CharField(
        label='Password Confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs_password2)

    )

    class Meta(UserCreationForm.Meta):
      model = Employee
      fields = ('first_name', 'last_name', 'username','email')
