from django import forms

class contact_form(forms.Form):

    email = forms.EmailField(label="Email Adresi")
    name = forms.CharField(label="İsminiz")
    message = forms.CharField(label="Mesajınız",widget=forms.Textarea)
