from django.contrib import admin

from .models import AdditionalServices, Budget, Callendar, CeremonyPlace, Documents, Guest, Invitations, Music, Photographer, Timetable, WeddingHall

# Register your models here.
admin.site.register(Music)
admin.site.register(Invitations)
admin.site.register(Photographer)
admin.site.register(CeremonyPlace)
admin.site.register(AdditionalServices)
admin.site.register(WeddingHall)
admin.site.register(Guest)
admin.site.register(Timetable)
admin.site.register(Documents)
admin.site.register(Budget)
admin.site.register(Callendar)