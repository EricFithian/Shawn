from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photos/', views.photos, name='photos'),
    path('details/', views.details, name='details'),
    path('rsvp/', views.rsvp, name='rsvp'),
    path('registry/', views.registry, name='registry'),
]