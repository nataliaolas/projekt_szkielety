from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, TemplateView, ListView
from .models import Photographer
# from django.views.generic.base import TemplateView, ListView
# Create your views here.

from wedding.models import Music

from .forms import MusicForm


class MainCardsView(TemplateView):
    template_name = "wedding/main_page.html"


class PhotographerListView(ListView):
    model = Photographer


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

  


    

