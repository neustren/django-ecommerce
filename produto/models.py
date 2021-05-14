from django.conf import settings
import os
from PIL import Image
from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(('V', 'Variação'), ('S', 'Simples'))
    )

    @staticmethod
    def resize_image(img, new_width=800):
        print(img.name)
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        print(img_full_path)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        print(original_width, original_height)
        new_height = round((new_width * original_height) / original_width)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome
