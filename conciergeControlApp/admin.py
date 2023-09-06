from django.contrib import admin
from .models import Produto, Condomino, Acervo_Portaria

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('local', 'produto', 'estoque')

class CondominoAdmin(admin.ModelAdmin):
    list_display = ('ap', 'name', 'fone', 'inquilino', 'fone_inquilino')

class Acervo_PortariaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'estoque')

# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Condomino, CondominoAdmin)
admin.site.register(Acervo_Portaria, Acervo_PortariaAdmin)
