from django.template import Library
from utils import money
register = Library()


@register.filter
def formata_preco(val):
    return money.formata_preco(val)


@register.filter
def cart_total_qtd(carrinho):
    return money.cart_total_qtd(carrinho)


@register.filter
def cart_totals(carrinho):
    return money.cart_totals(carrinho)
