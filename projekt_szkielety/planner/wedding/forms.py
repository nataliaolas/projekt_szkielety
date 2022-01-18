from django import forms
from django.db.models import fields
from .models import AdditionalServices, CeremonyPlace, Invitations, Photographer, StandardInfo, Music, WeddingHall, Guest
from crispy_forms.helper import FormHelper

# class StandardForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         print("ELOLOLO")
#         print("\n\n ********* Standard FORM ***********")
#         print(f'ARGS: {args}')
#         print(f'KWARGS: {kwargs}')
#         super(StandardForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'POST'

#     class Meta:
#         model=StandardInfo
#         fields='__all__'
#         exclude = ('approved',)

#         # def save(self, *args, **kwargs):
#         #     #Calling the parent model form save method
#         #     print("\n\n ********* Standard FORM ***********")
#         #     print(f'ARGS: {args}')
#         #     print(f'KWARGS: {kwargs}')
#         #     print("********************************\n\n")
#         #     super(StandardForm, self).save(*args, **kwargs)
#         widgets = {
#             'name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa'}),
#             'phone_number' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nr Telefonu'}),
#             'email_address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Email'}),
#             'price' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Cena'}),
#             'address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Adres'}),
#             'caution' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Kaucja'}),
#             'notes' : forms.Textarea(attrs={'class' : 'form-control',  'placeholder': 'Notatki'}),
#         } 
#         labels = {'type' : 'Typ', 'name' : 'Nazwa', 'phone_number' : 'Nr telefonu',
#          'email_address' : 'Adres email' ,'price' : 'Cena' ,'address' : 'Adres' ,'caution' : 'Kaucja', 'notes' : 'Notatki' }



class MusicForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(MusicForm, self).__init__(*args,**kwargs)

    class Meta:
        model = Music
        fields='__all__'
        exclude = ('approved',)

        widgets = {
            'type' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Typ'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa'}),
            'phone_number' : forms.NumberInput(attrs={'class' : 'form-control',  'placeholder': 'Nr Telefonu'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Email'}),
            'price' : forms.NumberInput(attrs={'class' : 'form-control',  'placeholder': 'Cena'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Adres'}),
            'caution' : forms.NumberInput(attrs={'class' : 'form-control',  'placeholder': 'Kaucja'}),
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
            'quantity' : forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Ilosc'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nr Telefonu'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Email'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Cena'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Adres'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Kaucja'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control',  'placeholder': 'Notatki'}),
        } 
        labels = {'quantity' : 'Ilosc', 'name' : 'Nazwa', 'phone_number' : 'Nr telefonu',
         'email_address' : 'Adres email' ,'price' : 'Cena' ,'address' : 'Adres' ,'caution' : 'Kaucja', 'notes' : 'Notatki' }

class PhotographerForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields='__all__'
        exclude = ('approved',)

        widgets = {
            'services' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Uslugi'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nr Telefonu'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Email'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Cena'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Adres'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Kaucja'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control',  'placeholder': 'Notatki'}),
        }     
        labels = {'services' : 'Uslugi', 'name' : 'Nazwa', 'phone_number' : 'Nr telefonu',
         'email_address' : 'Adres email' ,'price' : 'Cena' ,'address' : 'Adres' ,'caution' : 'Kaucja', 'notes' : 'Notatki' }    

class CeremonyPlaceForm(forms.ModelForm):
    class Meta:
        model = CeremonyPlace
        fields='__all__'
        exclude = ('approved',)

        widgets = {
            'guest_capacity' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number',  'placeholder': 'Ilosc Gosci'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nr Telefonu'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Email'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Cena'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Adres'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Kaucja'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control',  'placeholder': 'Notatki'}),
        }
        labels = {'guest_capacity' : 'Ilosc Gosci', 'name' : 'Nazwa', 'phone_number' : 'Nr telefonu',
         'email_address' : 'Adres email' ,'price' : 'Cena' ,'address' : 'Adres' ,'caution' : 'Kaucja', 'notes' : 'Notatki' } 

class AdditionalServicesForm(forms.ModelForm):
    class Meta:
        model = AdditionalServices
        fields='__all__'
        exclude = ('approved',)

        widgets = {
            'importance' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number',  'placeholder': 'Poziom Istotnosci'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nr Telefonu'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Email'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Cena'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Adres'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Kaucja'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control',  'placeholder': 'Notatki'}),
        }
        labels = {'importance' : 'Poziom Istotnosci', 'name' : 'Nazwa', 'phone_number' : 'Nr telefonu',
         'email_address' : 'Adres email' ,'price' : 'Cena' ,'address' : 'Adres' ,'caution' : 'Kaucja', 'notes' : 'Notatki' }   


class WeddingHallForm(forms.ModelForm):
    class Meta:
        model = WeddingHall
        fields='__all__'
        exclude = ('approved',)

        widgets = {
            'accomodation' : forms.CheckboxInput(attrs={'class' : 'form-check'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nr Telefonu'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Email'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Cena'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Adres'}),
            'caution' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Kaucja'}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control',  'placeholder': 'Notatki'}),
        }
        labels = {'accomodation' : 'Nocleg', 'name' : 'Nazwa', 'phone_number' : 'Nr telefonu',
         'email_address' : 'Adres email' ,'price' : 'Cena' ,'address' : 'Adres' ,'caution' : 'Kaucja', 'notes' : 'Notatki' } 


DIET_TYPES = [
    ('S', 'Standard'),
    ('LF', 'Lactose Free'),
    ('VT', 'Vegetarian'),
    ('V', 'Vegan'),
    ('GF', 'Gluten Free'),
    ('F','Frutarian')
]

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields='__all__'
        #exclude = ('approved',)

        widgets = {
            'diet_type' : forms.Select(choices = DIET_TYPES,attrs={'class':'form-group'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Imie'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwisko'}),
            'phone_number' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nr Telefonu'}),
            'email_address' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Email'}),
            'accomodation' : forms.CheckboxInput(attrs={'class' : 'form-check'}),
            'age' : forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Wiek'}),
            'invited' : forms.CheckboxInput(attrs={'class' : 'form-check'}),
            'attendance' : forms.CheckboxInput(attrs={'class' : 'form-check'}),
        }
        labels = {'diet_type': 'Rodzaj Diety', 'first_name' : 'Imie', 'last_name' : 'Nazwisko', 'phone_number' : 'Nr telefonu',
         'email_address' : 'Adres email' ,'accomodation' : 'Nocleg' ,'age' : 'Wiek' ,'invited' : 'Zaproszony/a', 'attendance' : 'Zjawi Się' } 