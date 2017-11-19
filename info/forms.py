from .models import info
from django import forms


class information(forms.ModelForm):
    class Meta:
        model=info
        fields={
            'Name',
            'Email',
            'Subject',
            'Message',
        }




