from .models import Order


def get_order(id):
    """Returns the order model by id."""
    return Order.objects.get(id=id)


def order_delete(order):
    """Removes the order model."""
    order.cart_products.all().delete()
    order.delete()