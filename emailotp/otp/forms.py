from django import forms


class RegisterEmailForm(forms.Form):
    email = forms.EmailField()


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()

