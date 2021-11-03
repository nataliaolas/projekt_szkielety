from django.db import models
from django.db.models.fields import CharField, PositiveIntegerField


class StandardInfo(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9)
    email_address = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    address = models.CharField(max_length = 100)
    caution = models.DecimalField(max_digits=5, decimal_places=2)
    approved = models.BooleanField()
    notes = models.TextField()

    class Meta:
        abstract = True


class Music(StandardInfo):
    type = models.CharField(max_length=20)


class Invitations(StandardInfo):
    quantity = models.PositiveIntegerField()

class Photographer(StandardInfo):
    services = models.TextField()

class CeremonyPlace(StandardInfo):
    guest_capacity = models.PositiveIntegerField()

class AdditionalServices(StandardInfo):
    importance = models.IntegerField(max_length = 10)

class WeddingHall(StandardInfo):
    accomodation = models.BooleanField()
    guest_capacity = models.PositiveIntegerField()

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
    phone_number = models.CharField(max_length = 9)
    email_address = models.CharField(max_length = 50)
    accomodation = models.BooleanField()
    age = models.IntegerField(max_length = 3)
    invited = models.BooleanField(default = False)
    attendance = models.BooleanField(default = False)

class Timetable(models.Model):
    name = models.TextField(max_length = 50)
    time = models.DateField()
    done = models.BooleanField(default = False)

class Documents(models.Model):
    name = models.CharField(max_length = 50)

class Budget(models.Model):
    total = models.DecimalField(max_digits=8,decimal_places=2)
    spent = models.DecimalField(max_digits=8,decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=8,decimal_places=2)

class Callendar(models.Model):
    date = models.DateField()
    notes = models.TextField()
    
