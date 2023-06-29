from django import forms
from .models import Post

class UploadFileForm(forms.ModelForm):
    filec = forms.FileField(required=False)  # Make the filec field optional

    class Meta:
        model = Post
        fields = ['filec']