from django.urls import path
from  .views import connecter_compte,creer_utilisateur,Verification_mail,changement_code


urlpatterns = [
    
    path("connecter/",connecter_compte,name='login'),
    path('register/', creer_utilisateur, name='register'),
    path('verification/', Verification_mail, name='verification'),
    path('modifierCode/<str:email>/',changement_code, name='modifierCode'),
 
]


