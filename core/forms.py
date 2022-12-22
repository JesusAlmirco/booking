from django import forms

class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')
    tel = forms.CharField(max_length=30, label='Phone number')
    remarks = forms.CharField(label='Remarks', widget=forms.Textarea())