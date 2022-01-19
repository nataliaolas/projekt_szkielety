from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.template import loader
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView
from .models import AdditionalServices, Guest, Photographer, WeddingHall
# from django.views.generic.base import TemplateView, ListView
# Create your views here.
from django.contrib.auth.models import User
from wedding.models import Music,Invitations,CeremonyPlace,Photographer
from django.contrib.auth import authenticate, login
from .forms import AdditionalServicesForm, CeremonyPlaceForm, GuestForm, InvitationsForm, LogInForm, MusicForm, PhotographerForm, SignUpForm, WeddingHallForm


class MainCardsView(TemplateView):
    template_name = "wedding/main_page.html"

class InProgressView(TemplateView):
    template_name = "wedding/in_progress.html"

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

class InvitationListView(ListView):
    model = Invitations



def sign_up(request):
    created_user = False

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            created_user = True
    else:
        form = SignUpForm()
    context = {
        'form': form,
        'created_user': created_user
    }
    return render(request, 'wedding/register2.html', context)

def customLogin(request):
    template = loader.get_template('wedding/login2.html')
    context = {'elo':'elo'}
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LogInForm()
    context = {
        'form': form
    }
    return render(request, 'wedding/login2.html', context)


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

    def post(self, request):
        form = InvitationsForm(self.request.POST)
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
            print(InvitationsForm.errors)
            print("\n\n\n ******************************** \n\n\n")
            print("FORMA JEST INWALIDA")
        return redirect('/invitations')

    def get_success_url(self):
        return redirect('/invitations')


class AddPhotographerView(CreateView):
    model = Photographer
    form_class = PhotographerForm
    template_name = 'wedding/photographer_add.html'

    def post(self, request):
        form = PhotographerForm(self.request.POST)
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
            print(PhotographerForm.errors)
            print("\n\n\n ******************************** \n\n\n")
            print("FORMA JEST INWALIDA")
        return redirect('/photographers')


class AddCeremonyPlaceView(CreateView):
    model = CeremonyPlace
    form_class = CeremonyPlaceForm
    template_name = 'wedding/ceremony_place_add.html'

    def post(self, request):
        form = CeremonyPlaceForm(self.request.POST)
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
            print(CeremonyPlaceForm.errors)
            print("\n\n\n ******************************** \n\n\n")
            print("FORMA JEST INWALIDA")
        return redirect('/ceremony_places')


class AddAdditionalServicesView(CreateView):
    model = AdditionalServices
    form_class = AdditionalServicesForm
    template_name = 'wedding/additionalservices_add.html'

    def post(self, request):
        form = AdditionalServicesForm(self.request.POST)
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
            print(AdditionalServicesForm.errors)
            print("\n\n\n ******************************** \n\n\n")
            print("FORMA JEST INWALIDA")
        return redirect('/additional_services')

class AddWeddingHallView(CreateView):
    model = WeddingHall
    form_class = WeddingHallForm
    template_name = 'wedding/wedding_hall_add.html'

    def post(self, request):
        form = WeddingHallForm(self.request.POST)
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
            print(WeddingHallForm.errors)
            print("\n\n\n ******************************** \n\n\n")
            print("FORMA JEST INWALIDA")
        return redirect('/wedding_halls')


class AddGuestView(CreateView):
    model = Guest
    form_class = GuestForm
    template_name = 'wedding/guest_add.html'    


class MusicDetailView(DetailView):
    model=Music
      

class PhotographerDetailView(DetailView):
    model=Photographer


class InvitationsDetailView(DetailView):
    model=Invitations


class CeremonyPlaceDetailView(DetailView):
    model=CeremonyPlace

class GuestDetailView(DetailView):
    model=Guest

class AdditionalServicesDetailView(DetailView):
    model=AdditionalServices


class WeddingHallDetailView(DetailView):
    model=WeddingHall
  

class MusicUpdateView(UpdateView):
    model=Music
    form_class = MusicForm
    template_name = 'wedding/music_add.html'

    def get_success_url(self):
        return redirect('music-detail', args=(self.object.id,))

class PhotographerUpdateView(UpdateView):
    model=Photographer
    form_class = PhotographerForm
    template_name = 'wedding/photographer_add.html'

    def get_success_url(self):
        return redirect('photographer-detail', args=(self.object.id,))

class InvitationsUpdateView(UpdateView):
    model=Invitations
    form_class = InvitationsForm
    template_name = 'wedding/invitations_add.html'

    def get_success_url(self):
        return redirect('invitation-detail', args=(self.object.id,))


class CeremonyPlaceUpdateView(UpdateView):
    model=CeremonyPlace
    form_class = CeremonyPlaceForm
    template_name = 'wedding/ceremony_place_add.html'

    def get_success_url(self):
        return redirect('ceremony_place-detail', args=(self.object.id,))

class GuestUpdateView(UpdateView):
    model=Guest
    form_class = GuestForm
    template_name = 'wedding/guest_add.html'

    def get_success_url(self):
        return redirect('music-detail', args=(self.object.id,))

class AdditionalServicesUpdateView(UpdateView):
    model=AdditionalServices
    form_class = AdditionalServicesForm
    template_name = 'wedding/additionalservices_add.html'

    def get_success_url(self):
        return redirect('additional_service-detail', args=(self.object.id,))


class WeddingHallUpdateView(UpdateView):
    model=WeddingHall
    form_class = WeddingHallForm
    template_name = 'wedding/wedding_hall_add.html'

    def get_success_url(self):
        return redirect('wedding_hall-detail', args=(self.object.id,))


  






    

