from django import forms
from .models import CommentModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['blog', 'created_at']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'phone'}),
            'comment': forms.Textarea(attrs={'placeholder': 'comment'}),
        }
