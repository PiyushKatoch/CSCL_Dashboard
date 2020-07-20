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
    ('BIO-TECH', 'BioTech Engineering')
)

SPECIALIZATION = (
    ('','Choose...'),
    ('Data Science', 'Data Science'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Cyber Security', 'Cyber Security'),
    ('ECE-1','ECE Specialization')
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
        fields = ['username','email','stream','specialization','password1','password2']

class SeniorRegisterForm(UserCreationForm):
    email = forms.EmailField()
    specialization = forms.ChoiceField(
         label='Select your Specialization you are in ?',
         choices=SPECIALIZATION,)
    courses=forms.CharField(label='Top 5 Courses you want to Recommend | Format - course1-udemy,course2-courera,course3-platform_name')
    articles=forms.CharField(label='Top 5 Articles you want to Recommend | Format - article1-google,article2-wikipedia,article3-platform_name')
    projects=forms.CharField(label='Top 5 Projects you want to Collaborate on | Format - Project1-discription,Project2-discription')
    class Meta:
        model = User
        fields = ['username' , 'email','specialization','courses','articles','projects','password1' , 'password2']

class TeacherRegisterForm(UserCreationForm):
    email = forms.EmailField()
    teacherID = forms.CharField()
    class Meta:
        model = User
        fields = ['username' , 'email','teacherID','password1' , 'password2']


    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


