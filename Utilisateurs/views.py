from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


#fonction pour creer un utilisateur

def creer_utilisateur(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password != password_confirm:
            messages.error(request, "Les mots de passe ne correspondent pas.")
        elif len(password) < 8 or not re.search(r'[A-Za-z]',password) or not re.search(r'\d',password)or not re.search(r'[A-Za-z]',password) :
            messages.error(request, "Le mot de passe doit contenir au moins 8 caractères.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Cet email existe déjà.")
        else:
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
