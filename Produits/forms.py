from django.forms import ModelForm
from .models import Produit, Category,Vente
from django import forms


class AjoutProduit(ModelForm):
    
    class Meta:
        model = Produit
        fields = ['name', 'category', 'price', 'quantite', 'image', 'description', 'date_expiration']
        
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Le nom du produit',
                    'class': 'form-control-col-md-6'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control-col-md-6'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Le Prix Unitaire du produit',
                    'class': 'form-control-col-md-6'
                }
            ),
            'quantite': forms.NumberInput(
                attrs={
                    'placeholder': 'La quantité en stock',
                    'class': 'form-control-col-md-6'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'La description du produit',
                    'class': 'form-control',
                    'rows': 4
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            ),
            'date_expiration': forms.DateInput(
                attrs={
                    'placeholder': 'Date d\'expiration',
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AjoutProduit, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages = {
            'required': 'Le nom est obligatoire',
            'invalid': 'Remplissez le champ correctement',
        }
        self.fields['category'].error_messages = {
            'required': 'Le type est obligatoire',
            'invalid': 'Remplissez le champ correctement',
        }
        self.fields['price'].error_messages = {
            'required': 'Le prix est obligatoire',
            'invalid': 'Remplissez le champ correctement',
        }
        self.fields['quantite'].error_messages = {
            'required': 'La quantité est obligatoire',
            'invalid': 'Remplissez le champ correctement',
        }
        self.fields['description'].error_messages = {
            'required': 'La description est obligatoire',
            'invalid': 'Remplissez le champ correctement',
        }
        self.fields['date_expiration'].error_messages = {
            'required': 'La date d\'expiration est obligatoire',
            'invalid': 'Entrez une date valide',
        }


#formulaire de vente de produit
class AjoutVente(ModelForm):
    
    quantite = forms.IntegerField(
        help_text='Quantité à vendre',
        required=True,
    )
    
    customer = forms.CharField(
        max_length=100,
        help_text='Nom du client',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nom du client',
                'class': 'form-control'
            }
        )
        
        
    )
    class Meta:
        model = Vente
        fields = ['quantite', 'customer']
        
        widgets = {
            'quantite': forms.NumberInput(
                attrs={
                    'placeholder': 'Quantité à vendre',
                    'class': 'form-control'
                }
            ),
            'customer': forms.TextInput(
                attrs={
                    'placeholder': 'Nom du client',
                    'class': 'form-control'
                }
            ),
        }