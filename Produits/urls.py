from turtle import done
from django.urls import path
from .views import *
from Produits import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import delete_product



urlpatterns = [
   # path('',home,name='home')
   
   path('',Affichage.as_view(),name='home'),
   path('Ajout/',AjoutProduit.as_view(),name='Ajout'),
   path('Modification/<int:id>/',Modifier,name='Modifier'),
   #path('delete-product/<int:category_id>/', delete_product, name='delete_product'),
  

   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

