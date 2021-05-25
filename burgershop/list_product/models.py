from django.db import models
from django.urls import reverse


class BurgerProduct(models.Model):
    """"""
    title = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(max_length=1000, verbose_name='Описание продукта')
    grammar = models.IntegerField(verbose_name='Граммовки', default='0')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(blank=True, null=True, verbose_name='Фото продукта')

    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Бургеры'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """"""
        return reverse('product-detail', args=[str(self.slug)])
