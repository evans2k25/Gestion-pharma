from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Produit
from .forms import AjoutProduit as AjoutProduitForm  # Renommage pour éviter conflit

class Affichage(ListView):
    model = Produit
    template_name = 'home.html'
    queryset = Produit.objects.all()
    context_object_name = 'produits'  # bon pour éviter le nom par défaut "object_list"

class AjoutProduitView(CreateView):
    model = Produit
    form_class = AjoutProduitForm
    template_name = 'Ajout-donnee.html'
    success_url = reverse_lazy('home')

class UpdateDonneesView(UpdateView):
    model = Produit
    form_class = AjoutProduitForm
    template_name = 'modification.html'
    success_url = reverse_lazy('home')


from django.views.generic import DeleteView
from django.urls import reverse_lazy

class GenericDeleteView(DeleteView):
    model = None  # À surcharger dynamiquement
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("home")

    def get_queryset(self):
        # Permet de définir dynamiquement le modèle à supprimer
        assert self.model is not None, "Vous devez définir self.model dans la vue."
        return self.model.objects.all()
    
# class GenericUpdateView(UpdateView):
#     model = None  # À surcharger dynamiquement (ex : Produit)
#     fields = "__all__"  # ou une liste comme ['name', 'category', ...]
#     template_name = "modification.html"
#     success_url = reverse_lazy("home")

#     def get_queryset(self):
#         assert self.model is not None, "Vous devez définir self.model dans la vue."
#         return self.model.objects.all()
from django.views.generic import DetailView
from .models import Produit

from django.views.generic import DetailView
from .models import Produit

class ProduitDetailView(DetailView):
    model = Produit
    template_name = 'produit_detail.html'  # à créer
    context_object_name = "produit"