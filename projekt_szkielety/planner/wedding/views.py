from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.template import loader
from django.views.generic import CreateView, TemplateView, ListView, FormView
from .models import AdditionalServices, Guest, Photographer, WeddingHall
# from django.views.generic.base import TemplateView, ListView
# Create your views here.

from wedding.models import Music,Invitations,CeremonyPlace,Photographer

from .forms import AdditionalServicesForm, CeremonyPlaceForm, GuestForm, InvitationsForm, MusicForm, PhotographerForm, WeddingHallForm


class MainCardsView(TemplateView):
    template_name = "wedding/main_page.html"


class MusicListView(ListView):
    model = Music

class InvitationsListView(ListView):
    model = Invitations

class PhotographerListView(ListView):
    model = Photographer

class CeremonyPlaceListView(ListView):
    model = CeremonyPlace

class AdditionalServicesListView(ListView):
    model = AdditionalServices

class WeddingHallListView(ListView):
    model = WeddingHall




def register(request):
    template = loader.get_template('wedding/register.html')
    context = {'elo':'elo'}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('wedding/login.html')
    context = {'elo':'elo'}
    return HttpResponse(template.render(context, request))    


class AddMusicView(CreateView):
    model = Music
    form_class = MusicForm
    template_name = 'wedding/music_add.html'

    def post(self, request):
        form = MusicForm(self.request.POST)
        print("\n\n\n ******************************** \n\n\n")
        print(form)
        print("\n\n\n ******************************** \n\n\n")
        print("\n\n\n ******************************** \n\n\n")
        print(form.data)
        print("\n\n\n ******************************** \n\n\n")
        if form.is_valid():
            form.save()
            print("ELOELO430")
        else:
            print("\n\n\n ******************************** \n\n\n")
            print(form.errors)
            print("\n\n\n ******************************** \n\n\n")
            print("FORMA JEST INWALIDA")
        return redirect('/music')

       


class AddInvitationsView(CreateView):
    model = Invitations
    form_class = InvitationsForm
    template_name = 'wedding/invitations_add.html'


class AddPhotographerView(CreateView):
    model = Photographer
    form_class = PhotographerForm
    template_name = 'wedding/photographer_add.html'    

class AddCeremonyPlaceView(CreateView):
    model = CeremonyPlace
    form_class = CeremonyPlaceForm
    template_name = 'wedding/ceremony_place_add.html'

class AddAdditionalServicesView(CreateView):
    model = AdditionalServices
    form_class = AdditionalServicesForm
    template_name = 'wedding/additionalservices_add.html'

class AddWeddingHallView(CreateView):
    model = WeddingHall
    form_class = WeddingHallForm
    template_name = 'wedding/wedding_hall_add.html'    

class AddGuestView(CreateView):
    model = Guest
    form_class = GuestForm
    template_name = 'wedding/guest_add.html'    


      


  
  


    

