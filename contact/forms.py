from django import forms


departments = [
    ('sponsorluk','Sponsorluk'),
    ('organizasyon','Organizasyon'),
    ('marketing','Marketing'),
]


class contact_form(forms.Form):

    email = forms.EmailField(label="Email Adresiniz")
    name = forms.CharField(label="İsminiz")
    message = forms.CharField(label="Mesajınız",widget=forms.Textarea)

class new_member_form(forms.Form):

    name = forms.CharField(label="İsminiz")
    department = forms.CharField(label='Hangi Departman?', widget=forms.Select(choices=departments))
    email = forms.EmailField(label="Email Adresiniz")
    number = forms.CharField(label="Telefon Numaranız")

class mail_list_form(forms.Form):

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email adresin'}),label="")
