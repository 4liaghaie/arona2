from django.urls import path

from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.home, name='Home' ),
    path('lalila', views.lalila, name='laila'),
    path('amarila', views.amarila, name='amarila'),
    path('palaya', views.palaya, name='palaya'),
    path('thegrand', views.thegrand, name='thegrand'),
    path('larensignature', views.larensignature, name='larensignature'),
    path('food', views.food, name='foods'),
    path('activity', views.activity, name='act'),
    path('spa', views.spa, name='spa'),
    path('meeting', views.meeting, name='meeting'),


]
