from django.contrib.auth.models import User
from django.db import models
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class CartProduct(models.Model):
    """The model of the product in the cart."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey('list_product.BurgerProduct', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Продукты в корзинах'


class Cart(models.Model):
    """Cart model.Communication with the user OneToOneField."""
    customer = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    cart_product = models.ManyToManyField(CartProduct)

    class Meta:
        verbose_name_plural = 'Корзины'

    def get_absolute_url(self):
        return reverse('cart-user', args=[str(self.id)])

    @receiver(post_save, sender=User)
    def create_user_cart(sender, instance, created, **kwargs):
        """
        Creating a model cart when registering a user.
        """
        if created:
            Cart.objects.create(customer=instance)

    @receiver(post_save, sender=User)
    def save_user_cart(sender, instance, **kwargs):
        """
        Update user cart.
        """
        instance.cart.save()


