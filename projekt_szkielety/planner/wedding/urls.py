
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.MainCardsView.as_view(), name='main_cards'),
    # path('register', views.register, name='register'),
    path('register', views.sign_up, name='register'),
    path('login', views.customLogin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #LIST VIEWS
    path('music', views.MusicListView.as_view(), name='music_list'),
    path('invitations', views.InvitationsListView.as_view(), name='invitations_list'),
    path('photographers', views.PhotographerListView.as_view(), name='photographers_list'),
    path('ceremony_places', views.CeremonyPlaceListView.as_view(), name='ceremony_places_list'),
    path('additional_services', views.AdditionalServicesListView.as_view(), name='additional_services_list'),
    path('wedding_halls', views.WeddingHallListView.as_view(), name='wedding_halls_list'),
    #Detail VIEWS
    path('music/<int:pk>', views.MusicDetailView.as_view(), name='music-detail'),
    path('invitation/<int:pk>', views.InvitationsDetailView.as_view(), name='invitation-detail'),
    path('photographer/<int:pk>', views.PhotographerDetailView.as_view(), name='photographer-detail'),
    path('ceremeony_place/<int:pk>', views.CeremonyPlaceDetailView.as_view(), name='ceremeony_place-detail'),
    path('additional_service/<int:pk>', views.AdditionalServicesDetailView.as_view(), name='additional_service-detail'),
    path('wedding_hall/<int:pk>', views.WeddingHallDetailView.as_view(), name='wedding_hall-detail'),

    #CREATE VIEWS
    path('music_add', views.AddMusicView.as_view(), name='music-add'),
    path('invitations_add', views.AddInvitationsView.as_view(), name='invitations-add'),
    path('ceremony_place_add', views.AddCeremonyPlaceView.as_view(), name='ceremony_place-add'),
    path('photographer_add', views.AddPhotographerView.as_view(), name='photographer-add'),
    path('additional_services_add', views.AddAdditionalServicesView.as_view(), name='additional_services-add'),
    path('wedding_hall_add', views.AddWeddingHallView.as_view(), name='wedding_hall-add'), 
    path('guest_add', views.AddGuestView.as_view(), name='guest-add'), 

    #UPDATE VIEWS
    path('music/update/<int:pk>', views.MusicUpdateView.as_view(), name='music-update'),
    path('invitation/update/<int:pk>', views.InvitationsUpdateView.as_view(), name='invitation-update'),
    path('photographer/update/<int:pk>', views.PhotographerUpdateView.as_view(), name='photographer-update'),
    path('ceremeony_place/update/<int:pk>', views.CeremonyPlaceUpdateView.as_view(), name='ceremeony_place-update'),
    path('additional_service/update/<int:pk>', views.AdditionalServicesUpdateView.as_view(), name='additional_service-update'),
    path('wedding_hall/update/<int:pk>', views.WeddingHallUpdateView.as_view(), name='wedding_hall-update'),
]

