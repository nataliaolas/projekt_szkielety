from django import forms
from django.db.models import fields
from .models import StandardInfo, Music


# class StandardForm(Forms.ModelForm):
#     class Meta:
#         model:StandardInfo
#         fields='__all__'

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields='__all__'
        exclude = ('approved',)

        widgets = {
            'type' : forms.TextInput(attrs={'class' : 'form-control'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control'}),
        } 