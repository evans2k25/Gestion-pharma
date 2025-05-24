from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.urls import reverse


#fonction pour creer un utilisateur

def creer_utilisateur(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Vérification des champs requis
        if not username or not email or not password or not password_confirm:
            messages.error(request, "Tous les champs sont obligatoires.")
            return redirect("creation")
        
        # Validation du format de l'email (optionnel, basique)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, "Email invalide.")
            return redirect("creation")

        if password != password_confirm:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect("creation")

        if len(password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password) or not re.search(r'[!@#$%(),.?":{}²|<>§\/&=*]', password):
            messages.error(request, "Le mot de passe doit contenir au moins 8 caractères, une lettre, un chiffre et un caractère spécial.")
            return redirect("creation")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà.")
            return redirect("creation")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email existe déjà.")
            return redirect("creation")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Utilisateur créé avec succès. Vous pouvez vous connecter.")
        return redirect("login")
    return render(request, "creation.html")

# fonction pour se connecter.
def connecter_compte(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect("home")  # Accueil ou autre page
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, "login.html")

def Verification_mail(request):
    if request.method == "POST":
        email = request.POST.get('email') or request.GET.get('email')
        # Vérification si l'email est fourni
        if not email:
            messages.error(request, "Veuillez entrer votre adresse e-mail.")
            return render(request, "verificationMail.html")
        # Validation de l'email
        user = User.objects.filter(email=email).first()
        if user:
            # Attention : ton URL "modifierCode" doit gérer ?email=... en GET
            return redirect(reverse('modifierCode', kwargs={'email': email}))
        else:
            messages.error(request, "Aucun utilisateur trouvé avec cet e-mail.")
            return redirect("verification")
    return render(request, "verificationMail.html")

# fonction pour changer de mot de passe apres verification

def changement_code(request, email):
    # Utilise l'argument email fourni dans l'URL !
    if not email:
        messages.error(request, "Lien invalide ou email manquant.")
        return redirect("login")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, "Aucun utilisateur trouvé avec cet e-mail.")
        return redirect("login")

    if request.method == "POST":
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password != password_confirm:
            messages.error(request, "Les mots de passe ne correspondent pas.")
        elif len(password) < 8:
            messages.error(request, "Le mot de passe doit contenir au moins 8 caractères.")
        elif not any(char.isdigit() for char in password):
            messages.error(request, "Le mot de passe doit contenir au moins un chiffre.")
        elif not any(char.isalpha() for char in password):
            messages.error(request, "Le mot de passe doit contenir au moins une lettre.")
        elif not any(char in "!@#$%(),.?\":{}²|<>§/\\&=*-" for char in password):
            messages.error(request, "Le mot de passe doit contenir au moins un caractère spécial.")
        else:
            user.set_password(password)
            user.save()
            messages.success(request, "Mot de passe modifié avec succès.")
            return redirect("login")

    context = {
        'email': email,
    }
    return render(request, "nouveauMDP.html", context)


def deconnexion(request):
    logout(request)
    request.session.flush()  # vide TOUTE la session
    return redirect('login')