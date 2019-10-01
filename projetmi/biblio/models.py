from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Niveau(models.Model):
    titre = models.CharField(max_length=255)
    #logo = models.ImageField(upload_to='niveau')

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Parcours(models.Model):
    titre = models.CharField(max_length=255)
    neveau = models.ForeignKey(Niveau, on_delete=models.CASCADE , related_name = 'parcoursniveau')
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Categorie(models.Model):
    titre = models.CharField(max_length=255)
    neveau = models.ForeignKey(Niveau, on_delete=models.CASCADE , related_name = 'catgniveau')
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Cours(models.Model):
    nom = models.CharField(max_length=255)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE , related_name = 'coursniveau')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE , related_name = 'courscateg')

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Fichier(models.Model):
    nom = models.CharField(max_length=255, blank=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE , related_name = 'fichierniveau')
    parcours = models.ForeignKey(Parcours, on_delete=models.CASCADE , related_name = 'fichierparcours')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='fichiercateg')
    ajouter_par = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'fichieruser')

    description = models.TextField(blank=True)
    formats = models.CharField(max_length=200)
    #fichier = models.FileField(upload_to='fichier')
    
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)


class Appreciation(models.Model):
    note = models.PositiveIntegerField()
    commentaire = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'appruser')
    fichier = models.ForeignKey(Fichier, on_delete=models.CASCADE, related_name = 'apprfichier')

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)