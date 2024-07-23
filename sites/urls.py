# myapp/urls.py

from django.urls import path
from .views import accueil_view, objectifs_view, presentation_view

urlpatterns = [
    path('', accueil_view, name='accueil'),
    path('objectifs/', objectifs_view, name='objectifs'),
    path('presentation/', presentation_view, name='presentation'),
]
