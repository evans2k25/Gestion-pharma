from django.urls import path
from .views import Affichage, AjoutProduitView, UpdateDonneesView,ProduitDetailView,ProduitSearchView
from django.views.generic import DeleteView, UpdateView
from .models import Produit, Category 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Affichage.as_view(), name='home'),
    path('ajout/', AjoutProduitView.as_view(), name='ajout'),
    path('modifier/<int:pk>/', UpdateDonneesView.as_view(), name='modifier'),
    
    
    path(
        "produit/<int:pk>/supprimer/", 
        DeleteView.as_view(model=Produit, template_name='confirm_delete.html', success_url='/'), 
        name="produit_supprimer"
    ),
    
    path(
        "categorie/<int:pk>/supprimer/", 
        DeleteView.as_view(model=Category, template_name='categorie_confirm_delete.html', success_url='/'), 
        name="categorie_supprimer"
    ),
    
    path(
        "produit/<int:pk>/modifier/",
        UpdateView.as_view(
            model=Produit,
            fields=['name', 'category', 'price', 'quantite', 'date_expiration', 'image', 'description'],
            template_name='produit_form.html',
            success_url='/'
        ),
        name="produit_modifier"
    ),
    
    path('produit/<int:pk>/', ProduitDetailView.as_view(), name='produit_detail'),
    
    path("recherche/", ProduitSearchView.as_view(), name="produit_search_results"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 