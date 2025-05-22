from django.urls import path
from django.urls import reverse_lazy
from .views import (
    Affichage, AjoutProduitView, UpdateDonneesView, ProduitDetailView,
    ProduitSearchView, connecter_compte, home, deconnexion, Acceuille
)
from django.views.generic import DeleteView, UpdateView
from .models import Produit, Category 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Acceuille.as_view(), name='Acceuille'),  # page d'accueil
    # path('', Acc.as_view(), name='home'),
    path('logout/', deconnexion, name='logout'),
    path('login/', connecter_compte, name='login'),
    path('acceuille/', Acceuille.as_view(), name='Acceuille'),  # tu peux garder une seule ligne pour Acceuille si tu veux
    path('home/', Affichage.as_view(), name='home'),
    path('ajout/', AjoutProduitView.as_view(), name='ajout'),
    path('modifier/<int:pk>/', UpdateDonneesView.as_view(), name='modifier'),

    # Suppression produit : redirection vers acceuille après suppression
    path(
        "produit/<int:pk>/supprimer/", 
        DeleteView.as_view(
            model=Produit, 
            template_name='confirm_delete.html', 
            success_url=reverse_lazy('home')
        ), 
        name="produit_supprimer"
    ),
    # Suppression catégorie : redirection vers acceuille
    path(
        "categorie/<int:pk>/supprimer/", 
        DeleteView.as_view(
            model=Category, 
            template_name='categorie_confirm_delete.html', 
            success_url=reverse_lazy('home')
        ), 
        name="categorie_supprimer"
    ),
    # Modification produit (inline)
    path(
        "produit/<int:pk>/modifier/",
        UpdateView.as_view(
            model=Produit,
            fields=['name', 'category', 'price', 'quantite', 'date_expiration', 'image', 'description'],
            template_name='produit_form.html',
            success_url=reverse_lazy('Acceuille')
        ),
        name="produit_modifier"
    ),
    path('produit/<int:pk>/', ProduitDetailView.as_view(), name='produit_detail'),
    path("recherche/", ProduitSearchView.as_view(), name="produit_search_results"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)