from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Produit, Category
from django.contrib import messages
from datetime import datetime
from django.core.files.storage import FileSystemStorage


from django.views.generic import ListView, CreateView
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
    


#fonction pour modifier les données
def get_category_instance():
    instance = Category.objects.first()

def Modifier(request, id):
    produit = get_object_or_404(Produit, id=id) 
    catgories = Category.objects.all()
    errors = {}
    
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get("category")
        price = request.POST.get('price')
        quantite = request.POST.get('quantite')
        description = request.POST.get('description')
        date_expiration = request.POST.get('date_expiration')
        image = request.FILES.get('image')
        
        
        #validation des champs
        if not name:
            errors['name'] = "Le champ Nom est obligatoire."
        if not category_id:
            errors['category'] = "Le champ Catégorie est obligatoire."
        if not price:
            errors['price'] = "Le champ Prix est obligatoire."
        if not quantite:
            errors['quantite'] = "Le champ Quantité est obligatoire."
        if not description:
            errors['description'] = "Le champ Description est obligatoire."
        
        # Validation de la date d'expiration
        if date_expiration:
            try:
                datetime.strptime(date_expiration, '%Y-%m-%d')
            except ValueError:
                errors['date_expiration'] = "Le format de la date est invalide. Utilisez YYYY-MM-DD."
        if not errors:
            
            Category = get_object_or_404(catgories,id=category_id)
            produit.name = name
            produit.price = price
            produit.quantite = quantite
            produit.date_expiration = date_expiration
            produit.description = description
            
            if image:
                fs = FileSystemStorage()
                filname = fs.save(name.name,image)
                produit.image =  fs.url(filname)
                
                
        produit.save()
        messages.success(request, "Le produit a été modifié avec succès.")
        return redirect("home")  
    
    else:
        # Afficher les erreurs s'il y en a
        for key, errror in errors.items():
            messages.error(request, errror)
            
    return render(request, "modification.html",{'Produit':produit, 'Categories':Category, 'errors':errors })  

#suppression des donées
@require_http_methods(["DELETE"])
def delete_product(request, product_id):
    try:
        produit = Produit.objects.get(id=product_id)
        produit.delete()
        return JsonResponse({"success": True})
    except Produit.DoesNotExist:
        return JsonResponse({"success": False, "message": "Produit non trouvé"})
 
        
        
    


#fonction d'ajout des données
"""

def ajout_donne(request):
    
    #vreation de variable pour la gestion des erreurs
    errors = {}
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']
        quantite = request.POST['quantite']
        description = request.POST['description']
        date_ajout = request.POST['date_ajout']
        date_expiration = request.POST['date_expiration']
        image = request.FILES['image']
        
        #validation de la date 
        try:
            date_expiration = datetime.strptime(date_expiration, '%Y-%m-%d')
        except ValueError:
            errors['date_expiration'] = "le format est incorrecte"
            
        #validation du prix    
        try:
            price = float(price)
            
            if price < 0 :
                 errors['price'] = "Montant saisi incorrecte"
                 
        except ValueError:
            errors['price'] = "Saisissez un montant correcte"
        
        #si aucune erreur n'est constaté
        if not errors:
            try:         
            
               
                
              
                 #Recuperation des categories en fonction de la clé primaire
        
        
                category = get_object_or_404(Category, pk=request.POST['category'])
                savedonnees = Produit(name=name, category=category, price=price, quantite=quantite, description=description, date_ajout=date_ajout, date_expiration=date_expiration, image=image)
                savedonnees.save()
                messages.success(request,"le produit est enregistré")
            except Category.DoesNotExist:
                errors['category'] = f'la categorie specifié est introuvable.'
            except KeyError as e:
                errors[str(e)] =  f'le champ{e} est manquant dans la requete.'
            except Exception as e:
                messages.errors(request,f'une erreur est survenue:{e}')
                
        return redirect('home')
    else:
        category = Category.objects.all()
    return render(request, 'ajout-donnee.html', {'category':category,"errors": errors })

"""      