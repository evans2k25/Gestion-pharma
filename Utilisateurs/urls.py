from django.urls import path
from  .views import connecter_compte,creer_utilisateur


urlpatterns = [
    
    path("connecter/",connecter_compte,name='login'),
    path('register/', creer_utilisateur, name='register'),
    
]


