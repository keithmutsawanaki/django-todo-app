from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title'] # Keeping it minimal like the image
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'orei-input',
                'placeholder': 'What needs to be done?'
            }),
        }