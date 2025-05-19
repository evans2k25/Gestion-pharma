from django.urls import path
from .views import Affichage, AjoutProduit, Update_donnees 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Affichage.as_view(), name='home'),
    path('Ajout/', AjoutProduit.as_view(), name='Ajout'),
    path('modification/<int:pk>/', Update_donnees.as_view(), name='modification'),
   #  path('Detail/<int:pk>/', DetailProduit.as_view(), name='DetailProduit'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)