from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
# Create your views here.

from wedding.models import Music,Invitations,CeremonyPlace,Photographer

from .forms import CeremonyPlaceForm, InvitationsForm, MusicForm, PhotographerForm

def main_cards(request):
    template = loader.get_template('wedding/main_page.html')
    context = {'elo':'elo'}
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('wedding/register.html')
    context = {'elo':'elo'}
    return HttpResponse(template.render(context, request))


class AddMusicView(CreateView):
    model = Music
    form_class = MusicForm
    template_name = 'wedding/music_add.html'

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


  
  


    

