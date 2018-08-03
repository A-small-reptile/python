from django import forms

class CommentFrom(forms.Form):
    name=forms.CharField(required=True,max_length=20)
    email=forms.EmailField(required=True)
    comment=forms.CharField(required=True,max_length=300)