from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produit
from .forms import AjoutProduit as AjoutProduitForm  # Renommage pour éviter conflit

@never_cache
@login_required(login_url='login')
def home(request):
    return render(request, "home.html")



class produit_list(LoginRequiredMixin, ListView):
    model = Produit
    template_name = 'produit.html'
    context_object_name = 'produits'

class Acceuille(TemplateView):
    template_name = "Acc.html"

@method_decorator(never_cache, name='dispatch')
class Affichage(LoginRequiredMixin, ListView):
    model = Produit
    template_name = 'home.html'
    context_object_name = 'produits'

@method_decorator(never_cache, name='dispatch')
class AjoutProduitView(LoginRequiredMixin, CreateView):
    model = Produit
    form_class = AjoutProduitForm
    template_name = 'Ajout-donnee.html'
    success_url = reverse_lazy('produit')

class UpdateDonneesView(LoginRequiredMixin, UpdateView):
    model = Produit
    form_class = AjoutProduitForm
    template_name = 'modification.html'
    success_url = reverse_lazy('produit')

class GenericDeleteView(LoginRequiredMixin, DeleteView):
    model = Produit
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("produit")

class ProduitDetailView(LoginRequiredMixin, DetailView):
    model = Produit
    template_name = 'produit_detail.html'
    context_object_name = "produit"

class ProduitSearchView(LoginRequiredMixin, ListView):
    model = Produit
    context_object_name = "produits"
    template_name = 'produit_search_results.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string(self.template_name, context, request=self.request)
            return JsonResponse({'html': html})
        else:
            return super().render_to_response(context, **response_kwargs)

@never_cache
def connecter_compte(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['start'] = True
            messages.success(request, "Connexion réussie !")
            return redirect("Affichage")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, "login.html")