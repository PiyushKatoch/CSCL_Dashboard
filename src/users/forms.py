from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Profile

STREAM = (
    ('','Choose...'),
    ('CSE', 'Computer Science Engineering'),
    ('ECE', 'Electrical and Computer Engineering '),
    ('BIO', 'BioTech Engineering')
)

SPECIALIZATION = (
    ('','Choose...'),
    ('DS', 'Data Science'),
    ('AI', 'Artificila Intelligence'),
    ('CYS', 'Cyber Security')
)


class ChoicesForm(forms.ModelForm):
    register_as = forms.ChoiceField(
        label = "Choose as who you want to get registered ?",
        choices = ((0, "First Year Student"), (1, "Second / Third Year Student"), (2, "Teacher")),
        widget = forms.RadioSelect,
        initial = '1',
    )

    class Meta:
        model = User
        fields = ['register_as']

class JuniorRegisterForm(UserCreationForm):
     email = forms.EmailField()
     stream = forms.ChoiceField(
         label='Select your Stream ?',
         choices=STREAM,)
     specialization = forms.ChoiceField(
         label='Select your Specialization you aspire to be in ?',
         choices=SPECIALIZATION,)

     class Meta:
        model = User
        fields = ['username' , 'email','stream','specialization','password1' , 'password2']

class SeniorRegisterForm(UserCreationForm):
    email = forms.EmailField()

  

    class Meta:
        model = User
        fields = ['username' , 'email','password1' , 'password2']

class TeacherRegisterForm(UserCreationForm):
    email = forms.EmailField()

  

    class Meta:
        model = User
        fields = ['username' , 'email','password1' , 'password2']


    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


