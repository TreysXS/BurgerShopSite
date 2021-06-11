from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .service import get_user_products, create_and_send_order, clear_cart


class CartView(LoginRequiredMixin, View):
    """"""

    def get(self, request):
        """Displays the cart page."""
        return render(request, 'cart/cart.html', context={'cart': request.user.cart})

    def post(self, request):
        """Creates an order or removes products from the cart."""
        value_cart = request.POST.get('cart')
        user_products = get_user_products(request)
        if value_cart == 'send':
            create_and_send_order(request, user_products)
        elif value_cart == 'delete':
            clear_cart(user_products)
        return redirect('product-list')
