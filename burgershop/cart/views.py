from django.shortcuts import render, redirect
from django.views import View
from .models import Order


class CartView(View):

    def get(self, request):
        return render(request, 'cart/cart.html', context={'cart': request.user.cart})

    def post(self, request):
        user_products = request.user.cart.cart_product
        order = Order.objects.create(customer=request.user)
        order.cart_products.set(request.user.cart.cart_product.all())
        user_products.clear()
        return redirect('product-list')
