from orders.models import Order


def get_user_products(request):
    return request.user.cart.cart_product


def create_and_send_order(request, user_products):
    order = Order.objects.create(customer=request.user)
    order.cart_products.set(user_products.all())
    user_products.clear()


def clear_cart(user_products):
    user_products.all().delete()