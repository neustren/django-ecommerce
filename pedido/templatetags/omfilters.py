from django.template import Library
from utils import money
register = Library()


@register.filter
def formata_preco(val):
    return money.formata_preco(val)
