from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, TemplateView, ListView
from .models import AdditionalServices, Photographer, WeddingHall
# from django.views.generic.base import TemplateView, ListView
# Create your views here.

from wedding.models import Music,Invitations,CeremonyPlace,Photographer

from .forms import AdditionalServicesForm, CeremonyPlaceForm, InvitationsForm, MusicForm, PhotographerForm


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

    def form_invalid(self, form):
        print("\nFORM INVALID!!\n")
        print(f"\n SELF: {self}!!\n")
        print(f"\n Form: {form}!!\n")
        return super().form_invalid(form)

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


  
  


    

