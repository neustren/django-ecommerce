from django.contrib import admin
from .models import Produto, Variacao
# Register your models here.

# @admin.register(Produto)
# class ProdutoAdmin(admin.ModelAdmin):


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]


# admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
