from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponse
from . import models
from . import forms


class BasePerfil(View):
    template_name = 'criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user
                ),
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None
                )
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None
                ),
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None
                )
            }

        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, request, *args, **kwargs):
        return self.renderizar


class Criar(BasePerfil):
    def post(self, request, *args, **kwargs):
        return self.renderizar


class Atualizar(BasePerfil):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Atualizar')


class Login(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Logout')
