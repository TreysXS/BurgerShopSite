from .models import BurgerProduct


def get_product(slug):
    return BurgerProduct.objects.get(slug=slug)


def create_products(request, product):
    cart_product = request.user.cart.cart_product.create(product=product)
    cart_product.save()