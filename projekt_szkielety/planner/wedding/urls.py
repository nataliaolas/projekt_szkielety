
from django.urls import path
from . import views
urlpatterns = [
    path('', views.MainCardsView.as_view(), name='main_cards'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    #LIST VIEWS
    path('music', views.MusicListView.as_view(), name='music_list'),
    path('invitations', views.InvitationsListView.as_view(), name='invitations_list'),
    path('photographers', views.PhotographerListView.as_view(), name='photographers_list'),
    path('ceremony_places', views.CeremonyPlaceListView.as_view(), name='ceremony_places_list'),
    path('additional_services', views.AdditionalServicesListView.as_view(), name='additional_services_list'),
    path('wedding_halls', views.WeddingHallListView.as_view(), name='wedding_halls_list'),
    #Detail VIEWS
    path('music/<int:pk>', views.PhotographerListView.as_view(), name='music-detail'),
    path('invitation/<int:pk>', views.PhotographerListView.as_view(), name='invitation-detail'),
    path('photographer/<int:pk>', views.PhotographerListView.as_view(), name='photographer-detail'),
    path('ceremeony_place/<int:pk>', views.PhotographerListView.as_view(), name='ceremeony_place-detail'),
    path('additional_service/<int:pk>', views.PhotographerListView.as_view(), name='additional_service-detail'),
    path('wedding_hall/<int:pk>', views.PhotographerListView.as_view(), name='wedding_hall-detail'),

    #CREATE VIEWS
    path('music_add', views.AddMusicView.as_view(), name='music-add'),
    path('invitations_add', views.AddInvitationsView.as_view(), name='invitations-add'),
    path('ceremony_place_add', views.AddCeremonyPlaceView.as_view(), name='ceremony_place-add'),
    path('photographer_add', views.AddPhotographerView.as_view(), name='photographer-add'),
]

