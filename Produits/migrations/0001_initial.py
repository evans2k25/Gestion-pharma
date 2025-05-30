# Generated by Django 5.1.6 on 2025-02-23 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('quantite', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('date_expiration', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.category')),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='FactureClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(null=True)),
                ('date_achat', models.DateTimeField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.customer')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('quantite', models.PositiveIntegerField(null=True)),
                ('prix_unitaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.customer')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.produit')),
            ],
        ),
    ]
