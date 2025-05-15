from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Produit)
admin.site.register(Vente)
admin.site.register(FactureClient)
admin.site.register(Customer)
