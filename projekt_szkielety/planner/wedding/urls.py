
from django.urls import path
from . import views
urlpatterns = [
    path('', views.MainCardsView.as_view(), name='main_cards'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('photographers', views.PhotographerListView.as_view(), name='photographers_list'),
    path('photographer/<int:pk>', views.PhotographerListView.as_view(), name='photographer-detail'),
    path('music_add', views.AddMusicView.as_view(), name='music-add'),
    path('invitations_add', views.AddInvitationsView.as_view(), name='invitations-add'),
    path('ceremony_place_add', views.AddCeremonyPlaceView.as_view(), name='ceremony_place-add'),
    path('photographer_add', views.AddPhotographerView.as_view(), name='photographer-add'),
]

