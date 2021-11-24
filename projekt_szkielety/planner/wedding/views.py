from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def main_cards(request):
    template = loader.get_template('wedding/main_page.html')
    context = {'elo':'elo'}
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('wedding/register.html')
    context = {'elo':'elo'}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('wedding/login.html')
    context = {'elo':'elo'}
    return HttpResponse(template.render(context, request))    


    

