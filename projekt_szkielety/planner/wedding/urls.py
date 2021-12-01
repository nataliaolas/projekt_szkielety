
from django.urls import path
from . import views
urlpatterns = [
    path('', views.MainCardsView.as_view(), name='main_cards'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('music', views.AddMusicView.as_view(), name='music-add'),
    path('photographers', views.PhotographerListView.as_view(), name='photographers_list'),
    path('photographer/<int:pk>', views.PhotographerListView.as_view(), name='photographer-detail'),
]

