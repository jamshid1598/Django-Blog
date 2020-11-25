from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email      = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email-input', 'placeholder':'email@example.com'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'f_name-input', 'placeholder':'James'}))
    last_name  = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'s_name-input', 'placeholder':'Bond'}))

    class Meta:
        model  = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs={'class':'user-username', 'placeholder':'username'}
        self.fields['password1'].widget.attrs={'class':'user-password1', 'placeholder':'password'}
        self.fields['password2'].widget.attrs={'class':'user-password2', 'placeholder':'confirm password'}

    def save(self, commit=True):
        user            = super(SignUpForm, self).save(commit=False)
        user.email      = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user