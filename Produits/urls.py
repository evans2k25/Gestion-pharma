from turtle import done
from django.urls import path
from .views import *
from Produits import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path






urlpatterns = [
   # path('',home,name='home')
   
   path('',Affichage.as_view(),name='home'),
   path('Ajout/',AjoutProduit.as_view(),name='Ajout'),
   path('modification/<int:pk>/',Update_donnees.as_view(),name='modification'),
 
  

   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

