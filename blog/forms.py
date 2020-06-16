"""Module defining forms"""

from django import forms

class EmailPostForm(forms.Form):
    """Form to email link to blog post with comments"""
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
