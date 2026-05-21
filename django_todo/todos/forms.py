from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "What needs to be done?",
                    "autocomplete": "off",
                    "maxlength": 200,
                }
            ),
        }
