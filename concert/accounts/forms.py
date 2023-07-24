from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import ProfileModel



class ProfileForm(UserChangeForm):
    Gender = forms.ChoiceField(choices=ProfileModel.status_choices)

    class Meta:
        model = ProfileModel
        fields = ['user', 'Gender', 'Credit', 'ProfileImage']



class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ProfileModel
        fields = ['ProfileImage', 'Credit', 'Gender']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['ProfileImage', 'Credit', 'Gender']

class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', 'last_name', 'email']
    password = None
        