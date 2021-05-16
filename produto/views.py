from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from . import models


class ListaProdutos(ListView):
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('ListaProdutos')
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10


class DetalheProduto(DetailView):
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('DetalheProduto')
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarAoCarrinho(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('AdicionarAoCarrinho')


class RemoverDoCarrinho(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('RemoverDoCarrinho')


class Carrinho(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Finalizar')
