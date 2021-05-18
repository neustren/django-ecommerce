from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from . import models
from django.contrib import messages
from django.urls import reverse
from pprint import pprint


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

        if self.request.session.get('carrinho'):
            del self.request.session['carrinho']
            self.request.session.save()

        http_referer = self.request.META.get(
            'HTTP_REFERER', reverse('produto:lista'))

        variacao_id = self.request.GET.get('vid')
        if not variacao_id:
            messages.error(self.request, 'Produto não existe')
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)
        if variacao.estoque < 1:
            messages.error(self.request, 'Estoque insuficiente')
            return redirect(http_referer)

        # return redirect(self.request.META['HTTP_REFERER'])

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']
        produto = variacao.produto

        imagem = produto.imagem.name if produto.imagem else ''

        if variacao_id in carrinho:
            quantidade_carrinho = carrinho[variacao_id]['quantidade']
            quantidade_carrinho += 1

            if variacao.estoque < quantidade_carrinho:
                messages.warning(self.request,
                                 f'Estoque insuficiente para {quantidade_carrinho}x no '
                                 f'produto "{produto.nome}". Adicionamos {variacao.estoque}x '
                                 f'no seu carrinho.')

                quantidade_carrinho = variacao.estoque

            carrinho[variacao_id]['quantidade'] = quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo'] = variacao.preco * \
                quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo_promocional'] = variacao.preco_promocional * \
                quantidade_carrinho

        else:
            carrinho[variacao_id] = {
                'produto_id': produto.id,
                'produto_nome': produto.nome,
                'variacao_nome': variacao.nome or '',
                'variacao_id': variacao.id,
                'preco_unitario': variacao.preco,
                'preco_unitario_promocional': variacao.preco_promocional,
                'preco_quantitativo': variacao.preco,
                'preco_quantitativo_promocional': variacao.preco_promocional,
                'quantidade': 1,
                'slug': produto.slug,
                'imagem': imagem
            }

        self.request.session.save()
        # pprint(carrinho)

        messages.success(self.request,
                         f"Produto {produto.nome} {variacao.nome} adicionado ao seu carrinho "
                         f"{carrinho[variacao_id]['quantidade']}x.")

        # retcrn HttpResponse(f'{variacao.produto} {variacao.nome}')

        return redirect(http_referer)


class RemoverDoCarrinho(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('RemoverDoCarrinho')


class Carrinho(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse('Carrinho')
        return render(self.request, 'produto/carrinho.html')


class Finalizar(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Finalizar')
