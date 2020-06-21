from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text',]  # tuple 도 괜찮고, list도 괜찮다

