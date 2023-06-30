from .models import Listing, Contact
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

