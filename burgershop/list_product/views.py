from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .models import BurgerProduct
from .service import get_product, create_products


class BurgerListView(ListView):

    model = BurgerProduct

    def post(self, request):
        """If user is authenticated create a cart_product ELSE redirect to the login page."""
        if request.user.is_authenticated:
            slug = request.POST.get('slug')
            new_product = get_product(slug)
            create_products(request, new_product)
            return redirect('product-list')
        else:
            return redirect('account_login')


class BurgerDetailView(View):

    def get(self, request, slug):
        """Displays the BurgerProduct page"""
        try:
            burger_product = get_product(slug)
        except BurgerProduct.DoesNotExist:
            raise Http404()
        return render(request, 'list_product/burgerproduct_detail.html', context={'burger': burger_product})

    def post(self, request, slug):
        """If user is authenticated create a cart_product's ELSE redirect to the login page"""
        if request.user.is_authenticated:
            count_product = int(request.POST.get('count'))
            new_product = get_product(slug)

            for _ in range(count_product):
                create_products(request, new_product)

            return redirect('user-cart')
        else:
            return redirect('account_login')
