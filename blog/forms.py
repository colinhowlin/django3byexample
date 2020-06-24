"""Module defining forms"""

from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    """Form to email link to blog post with comments"""
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Form to post comments to a blog post. Inherits from ModelForm
       which allows us to define form fields from model attributes"""
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
