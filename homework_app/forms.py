from django import forms
from django.forms import ModelForm, PasswordInput

from homework_app.models import Category, Product



class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']


class EditCategoryForm(ModelForm): #czy tutaj należy tworzyć nowy formularz czy lepiej wykorzystać formularz dodawania?
    class Meta:
        model = Category
        fields = ['category_name']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=64)


class LoginForm(forms.Form):
    login = forms.CharField(label='login', max_length=64)
    password = forms.CharField(label='password', max_length=64, widget=PasswordInput)
