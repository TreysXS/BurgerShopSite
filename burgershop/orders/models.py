import uuid
from django.db import models
from django.urls import reverse

from cart.models import CartProduct


class Order(models.Model):
    """Order model."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cart_products = models.ManyToManyField(CartProduct)

    class Meta:
        verbose_name_plural = 'Заказы'
        permissions = (("can_delete_order", "Delete order"),)

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])