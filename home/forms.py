from .models import Questions
from django import forms

class HomeForm(forms.ModelForm):
    question=forms.CharField()

    class Meta:
        model=Questions
        fields=('question',)