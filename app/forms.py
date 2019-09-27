from django import forms

class ContactForm(forms.Form):
    Email = forms.EmailField(required=True)

class CreateAccountForm(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput(attrs={'required':True, 'type':'email'}))
    FirstName = forms.CharField(required=True)
    LastName = forms.CharField(required=True)
    Phone = forms.IntegerField(widget=forms.TextInput(attrs={'required':True, 'type':'tel'}))
    Make = forms.CharField(widget=forms.TextInput(attrs={'required':True, 'type':'text', 'placeholder':'Toyota'}))
    Model = forms.CharField(widget=forms.TextInput(attrs={'required':True, 'type':'text', 'placeholder':'Tacoma'}))
    Year = forms.IntegerField(widget=forms.TextInput(attrs={'required':True, 'type':'number', 'placeholder':2019}))
    Date = forms.DateField(widget=forms.TextInput(attrs={'required':True, 'type':'date'}))
    Time = forms.TimeField(widget=forms.TextInput(attrs={'required':True, 'type':'time'}))
    Service = forms.CharField(required=True)
