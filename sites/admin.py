from typing import Any
from django.contrib import admin
from .models import auteur,categorie,articles,Commentaire
from django.utils.html import format_html

# Register your models here.  
class auteurAdmin(admin.ModelAdmin):  
    list_display = ('nom','profil')
    search_fields = ('nom','profil')
    ordering = ('nom',)
     
admin.site.register(auteur)

class articlesAdmin(admin.ModelAdmin):
    list_display = ('titre','contenu','auteur','date_publication','categorie','imagealaune','image')
    
    def image_preview(self,obj):
        if obj.image:
            return format_html('<img src="{}" style="ma-width: 200px; height:auto;"/>',obj.image.url)
        return ""
    image_preview.short_description = 'Aperçu Image'
    
    search_fields = ('titre','contenu')
    fields = ('titre','contenu','auteur','date_publication','categorie','imagealaune','image')
    readonly_fields = ('date_publication','image_preview')
    list_filter = ('date_publication', 'auteur')
    ordering = ('-date_publication',)
    
    def save_model(self, request, obj, form, change): 
        if not obj.id:
            obj.author =request.user
        super().save_model(request,obj,form,change)
            
admin.site.register(articles,articlesAdmin)

class categoriesAdmin(admin.ModelAdmin):
    list_display = ('nom','description')
    search_fields = ('nom','description')
    list_filter = ('nom', 'description')
    ordering = ('-nom',)

admin.site.register(categorie)

class CommentaireInline(admin.TabularInline): 
    model = Commentaire
    extra = 0 
    
class ArticleAdmin (admin.ModelAdmin): 
    inlines = [CommentaireInline]

