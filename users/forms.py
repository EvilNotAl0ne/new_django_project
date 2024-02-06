
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль', 
        widget=forms.PasswordInput, 
        error_messages={'required': 'Пожалуйста, заполните поле'})

    password2 = forms.CharField(
        label='Повторите пороль',
        widget=forms.PasswordInput)
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совподают')
        return cd['password2']


    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'email'
            )

        help_texts = {
            'username': "Только буквы, цифры и символы @.+-_"
            }

        verbose_name = {
            'username': 'login'
            }
        
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'email': 'Эл. почта'
        }
        widgets = {
            'username': forms.TextInput,
            'email': forms.EmailInput,
            'first_name': forms.TextInput
        }