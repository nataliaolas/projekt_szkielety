from django import forms
from django.db.models import fields
from .models import CeremonyPlace, Invitations, Photographer, StandardInfo, Music


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



class InvitationsForm(forms.ModelForm):
    class Meta:
        model = Invitations
        fields='__all__'
        exclude = ('approved',)

        widgets = {
            'quantity' : forms.TextInput(attrs={'class' : 'form-control'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control'}),
        } 

class PhotographerForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields='__all__'
        exclude = ('approved',)

        widgets = {
            'services' : forms.TextInput(attrs={'class' : 'form-control'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control'}),
        }         

class CeremonyPlaceForm(forms.ModelForm):
    class Meta:
        model = CeremonyPlace
        fields='__all__'
        exclude = ('approved',)

        widgets = {
            'guest_capacity' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control'}),
        } 