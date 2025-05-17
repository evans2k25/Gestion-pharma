from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Produit, Category
from django.contrib import messages
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView ,UpdateView
from .forms import AjoutProduit
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Produit
from .models import Category
from .forms import AjoutProduit



# Create your views here.
#def home(request):
    
    # recuperation des données
 #   donnees = Produit.objects.all()
    
 #   context = {
  #      'donnees':donnees
   # }
    
    #return render(request, 'home.html',context)



class Affichage(ListView):
    
    
    model = Produit
    
    #affichage du template
    template_name = 'home.html'
    
    #recuperation des données
    queryset = Produit.objects.all()
    
#class d'ajout des données avec formulaire généré
class AjoutProduit(CreateView):
    
    #utlisitation du model 
    model = Produit
    #specification du formulaire
    form_class = AjoutProduit
    #affichage du template
    template_name ='Ajout-donnee.html'
    success_url = reverse_lazy('home')
    
#classe  pour modifier les données
class Update_donnees(UpdateView):
    #recuperation du model
    model = Produit
    #specipication du formulaire
    form_class = AjoutProduit
    #affichage du template
    template_name = 'modification.html'
    success_url = reverse_lazy('home')
    
    

