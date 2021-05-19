from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponse

# Create your views here.


class Pagar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Pagar')


class SalvarPedido(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('SalvarPedido')


class Detalhe(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Detalhe')
