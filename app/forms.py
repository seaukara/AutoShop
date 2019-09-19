from django import forms

class ContactForm(forms.Form):
    Email = forms.EmailField(required=True)

class CreateAccountForm(forms.Form):
    Email = forms.EmailField(required=True)
    FirstName = forms.CharField(required=True)
    LastName = forms.CharField(required=True)
    Phone = forms.IntegerField(required=True)
    Make = forms.CharField(required=True)
    Model = forms.CharField(required=True)
    Year = forms.IntegerField(required=True)
    Date = forms.DateField(required=True)
    Time = forms.TimeField(required=True)
    Service = forms.CharField(required=True)
