from orders.models import Order


def get_user_products(request):
    """Return a user products from the model cart."""
    return request.user.cart.cart_product


def create_and_send_order(request, user_products):
    """Creates an order model and then adds products from the cart to it."""
    order = Order.objects.create(customer=request.user)
    order.cart_products.set(user_products.all())
    user_products.clear()


def clear_cart(user_products):
    """Removes products from the cart."""
    user_products.all().delete()