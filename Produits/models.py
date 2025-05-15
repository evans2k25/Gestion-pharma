from django.db import models

# Classe pour les produits
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Produit(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantite = models.PositiveIntegerField()
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField()
    # Correction ici : changement de self.Produit à self.name
    image = models.ImageField(upload_to='produits/', null=True, blank=True)
    
    class Meta:
        ordering = ['-date_ajout']
        
    def statut_quantite(self):
        if self.quantite == 0:
            return 'red'
        elif self.quantite <= 10:
            return 'orange'
        else:
            return 'green'
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveIntegerField(null=True)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Vente de {self.produit.name} à {self.customer.name}"

class FactureClient(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(null=True)
    date_achat = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Facture de {self.customer.name}"
