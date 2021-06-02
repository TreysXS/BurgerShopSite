from .models import Order


def get_order(id):
    return Order.objects.get(id=id)


def order_delete(order):
    order.cart_products.all().delete()
    order.delete()