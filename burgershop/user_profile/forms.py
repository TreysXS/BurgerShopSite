from django import forms
from .models import Profile, User


class UserForm(forms.ModelForm):
    pass

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    pass

    class Meta:
        model = Profile
        fields = ('description', 'img')