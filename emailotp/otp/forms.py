from django import forms


class RegisterEmailForm(forms.Form):
    email = forms.EmailField()
