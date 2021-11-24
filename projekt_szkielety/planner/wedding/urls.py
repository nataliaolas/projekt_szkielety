
from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_cards, name='main_cards'),
    path('register', views.register, name='register'),
    path('music', views.AddMusicView.as_view(), name='music-add'),
    path('invitations', views.AddInvitationsView.as_view(), name='invitations-add'),
    path('ceremony_place', views.AddCeremonyPlaceView.as_view(), name='ceremony_place-add'),
    path('photographer', views.AddPhotographerView.as_view(), name='photographer-add'),
]

