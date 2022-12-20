from django import forms
from allauth.account.forms import SignupForm


class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='first name')
    last_name = forms.CharField(max_length=30, label='last name')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='first name')
    last_name = forms.CharField(max_length=30, label='last name')
    description = forms.CharField(label='description', widget=forms.Textarea(), required=False)
    image = forms.ImageField(required=False, )