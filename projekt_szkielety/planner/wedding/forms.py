from django import forms
from django.db.models import fields
from .models import AdditionalServices, CeremonyPlace, Invitations, Photographer, StandardInfo, Music, WeddingHall, Guest
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class MusicForm(forms.ModelForm):

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



def validate_strong_password(value):
    
    if len(set(value)) < 5:
        raise ValidationError(
            '%(value)s nie zawiera 5 unikalnych znaków, a powinno',
            params={'value': value}
        )
    elif not any(map(str.isdigit, value)):
        raise ValidationError(
            '%(value)s nie zawiera zadnej cyfry a powinno',
            params={'value': value}
        )
    elif not any(map(str.isupper, value)):
        raise ValidationError(
            '%(value)s nie posiada duzej litery!',
            params={'value': value}
        )
    elif not any(map(str.islower, value)):
        raise ValidationError(
            '%(value)s nie posiada malej litery!',
            params={'value': value}
        )


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa uzytkownika'}),
        label="Podaj nazwę użytkownika")
    password = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class' : 'form-control',  'placeholder': 'Haslo'}),
        label="Podaj Hasło",
        validators=[validate_strong_password]
    )
    password2 = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class' : 'form-control',  'placeholder': 'Powtorz Haslo'}),
        label="Powtórz Hasło"
    )
    

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if username:
            if User.objects.filter(username=username):
                self.add_error('username', 'Nazwa użytkownika jest już zajęta')

            if password and password2 and password != password2:
                self.add_error(None, 'Hasła nie są identyczne')

class LogInForm(forms.Form):
    username = forms.CharField(min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control',  'placeholder': 'Nazwa uzytkownika'}),
        label="Podaj nazwę użytkownika",
        required=True
    )
    password = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(attrs={'class' : 'form-control',  'placeholder': 'Haslo'}),
        label="Podaj Hasło",
        required=True
    )
    

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            print("USER IS NOT AUTHENTICATED!!!!")
            self.add_error(None,"Błędny login lub hasło")
