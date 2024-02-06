from django import forms
from django.contrib.auth.models import User
from .models import Post

# class PostForm(forms.Form):
    #author = forms.CharField(max_length=50, label='Автор')
    # title = forms.CharField(max_length=200, label='Заголовок')
    # text = forms.CharField(widget=forms.Textarea, label='Текст поста')
    # image = forms.ImageField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

