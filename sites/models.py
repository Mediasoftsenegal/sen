from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.files.storage import FileSystemStorage
from ckeditor_uploader.fields import RichTextUploadingField


fs = FileSystemStorage(location='sites/static/')

	# Create your models here.    
class auteur(models.Model):
    nom = models.CharField(max_length=155)
    biographie = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/auteurs/')
    profil = models.CharField(max_length=255)
    
    def __str__(self):
       return f"{self.nom} {self.biographie}"
   
class categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
       return f"{self.nom} "
class articles(models.Model):
   titre = models.CharField(max_length=255)
   contenu = RichTextUploadingField() 
   auteur = models.ForeignKey('Auteur', on_delete=models.SET_NULL,null=True)
   date_publication = models.DateTimeField(auto_now_add=True)
   categorie = models.ForeignKey('Categorie',on_delete=models.SET_NULL,null=True)
   imagealaune = models.ImageField(upload_to='images/articles/',storage=fs)
   
            
   def __str__(self):
       return self.titre        
class Meta:
        ordering = ['-date_publication']
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        
class Commentaire(models.Model):
    articles = models.ForeignKey(articles, on_delete=models.CASCADE)
    

    

