
from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_cards, name='main_cards'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('music', views.AddMusicView.as_view(), name='music-add'),
]

