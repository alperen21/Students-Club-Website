from django import forms
from .models import Article

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","image"]