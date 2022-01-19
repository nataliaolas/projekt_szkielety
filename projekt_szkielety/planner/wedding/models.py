from django.db import models
from django.db.models.fields import CharField, PositiveIntegerField
from django.urls import reverse

class StandardInfo(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9)
    email_address = models.CharField(max_length=30, null=True,blank=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    address = models.CharField(max_length = 100,null=True, blank=True)
    caution = models.DecimalField(max_digits=8, decimal_places=2)
    approved = models.BooleanField(blank = True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class Music(StandardInfo):
    type = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('music-detail', kwargs={'pk' : self.pk})

    def get_add_url(self):
        return reverse('music-add')


class Invitations(StandardInfo):
    quantity = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('invitations-detail', kwargs={'pk' : self.pk})

    def get_add_url(self):
        return reverse('invitations-add')


class Photographer(StandardInfo):
    services = models.TextField()
    def get_absolute_url(self):
        return reverse('photographer-detail', kwargs={'pk' : self.pk})
    
    def get_add_url(self):
        return reverse('photographer-add')

class CeremonyPlace(StandardInfo):
    guest_capacity = models.PositiveIntegerField()
    def get_absolute_url(self):
        return reverse('ceremony-place-detail', kwargs={'pk' : self.pk})
    
    def get_add_url(self):
        return reverse('ceremony_place-add')


class AdditionalServices(StandardInfo):
    importance = models.IntegerField(max_length = 10,null=True, blank=True)
    def get_absolute_url(self):
        return reverse('additional-service-detail', kwargs={'pk' : self.pk})
    
    def get_add_url(self):
        return reverse('additional_services-add')


class WeddingHall(StandardInfo):
    accomodation = models.BooleanField()
    guest_capacity = models.PositiveIntegerField()
    def get_absolute_url(self):
        return reverse('wedding-hall-detail', kwargs={'pk' : self.pk})
    
    def get_add_url(self):
        return reverse('wedding_hall-add')


class Guest(models.Model):
    DIET_TYPES= [
    ('S', 'Standard'),
    ('LF', 'Lactose Free'),
    ('VT', 'Vegetarian'),
    ('V', 'Vegan'),
    ('GF', 'Gluten Free'),
    ('F','Frutarian')
    ]

    diet_type = models.CharField(max_length = 2, choices = DIET_TYPES)
    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 9,null=True,blank=True)
    email_address = models.CharField(max_length = 50, null=True,blank=True)
    accomodation = models.BooleanField()
    age = models.IntegerField(max_length = 3, null=True,blank=True)
    invited = models.BooleanField(default = False)
    attendance = models.BooleanField(default = False)
    def get_absolute_url(self):
        return reverse('guest-detail', kwargs={'pk' : self.pk})
    
    def get_add_url(self):
        return reverse('guest-add')


class Timetable(models.Model):
    name = models.TextField(max_length = 50)
    time = models.DateField()
    done = models.BooleanField(default = False)
    def get_absolute_url(self):
        return reverse('timetable-detail', kwargs={'pk' : self.pk})

class Documents(models.Model):
    name = models.CharField(max_length = 50)
    def get_absolute_url(self):
        return reverse('documents-detail', kwargs={'pk' : self.pk})

class Budget(models.Model):
    total = models.DecimalField(max_digits=8,decimal_places=2)
    spent = models.DecimalField(max_digits=8,decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=8,decimal_places=2)
    def get_absolute_url(self):
        return reverse('budget-detail', kwargs={'pk' : self.pk})

class Callendar(models.Model):
    date = models.DateField()
    notes = models.TextField()
    def get_absolute_url(self):
        return reverse('calendar-detail', kwargs={'pk' : self.pk})
    
