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
            'type' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Typ'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nr Telefonu'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Email'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Price'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Adres'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Kaucja'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control',  'placeholder': 'Notatki'}),
        } 
        labels = {'type' : 'Typ', 'name' : 'Nazwa', 'phone_number' : 'Nr telefonu',
         'email_address' : 'Adres email' ,'price' : 'Cena' ,'address' : 'Adres' ,'caution' : 'Kaucja', 'notes' : 'Notatki' }