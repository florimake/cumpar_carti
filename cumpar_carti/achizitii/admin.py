from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Paragraf)
class ParagrafAdmin(admin.ModelAdmin):
    list_display = ("titlu", "paragraf")
    prepopulated_fields = {"slug": ("paragraf",)}
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("nume", "tel", "email")
    prepopulated_fields = {"slug": ("nume", "tel")}
    
# @admin.register(Produs)
# class ProdusAdmin(admin.ModelAdmin):
#     list_display = ("nume", "categorie", "status", "cod_produs", "pret", "garantie")
#     list_filter = ("status", "categorie",)
#     prepopulated_fields = {"slug": ("nume","cod_produs",)}
#     search_fields = ("nume", "cod_produs", "status")