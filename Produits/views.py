from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Produit
from django.views.generic import ListView, CreateView, UpdateView,DetailView
from .forms import AjoutProduit  # Nom corrigé

class Affichage(ListView):
    model = Produit
    template_name = 'home.html'
    queryset = Produit.objects.all()

class AjoutProduit(CreateView):
    model = Produit
    form_class = AjoutProduit
    template_name = 'Ajout-donnee.html'
    success_url = reverse_lazy('home')

class Update_donnees(UpdateView):
    model = Produit
    form_class = AjoutProduit
    template_name = 'modification.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Optionnel : Logique supplémentaire avant la sauvegarde
        return super().form_valid(form)
    
# class DetailProduit(DetailView):
#     model = Produit
#     template_name = 'detailproduit.html'  # à créer
#     context_object_name = 'produit'
#     success_url = reverse_lazy('home')