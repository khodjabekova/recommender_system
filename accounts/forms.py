from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        widgets = {
            'username': forms.TextInput(attrs = {'placeholder': 'Username'}),
            'email': forms.TextInput(attrs = {'placeholder': 'E-Mail address'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': "Password"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': "Confirm password"})