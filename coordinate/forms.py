from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"type": "username"})
        self.fields["email"].widget.attrs.update({"type": "email"})
        self.fields["password1"].widget.attrs.update({"type": "password1"})
        self.fields["password2"].widget.attrs.update({"type": "password2"})


    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.email = self.cleaned_data['password1']
        user.email = self.cleaned_data['password2']
        if commit:
            user.save()
        return user

