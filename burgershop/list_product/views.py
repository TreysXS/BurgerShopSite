from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import BurgerProduct


class BurgerListView(ListView):
    """"""
    model = BurgerProduct


class BurgerDetailView(View):
    """"""

    def get(self, request, slug):
        try:
            burger_product = BurgerProduct.objects.get(slug=slug)
        except BurgerProduct.DoesNotExist:
            raise Http404()
        return render(request, 'list_product/burgerproduct_detail.html', context={'burger': burger_product})

    def post(self, request, slug):
        count_product = int(request.POST.get('count'))
        new_product = BurgerProduct.objects.get(slug=slug)
        for i in range(0, count_product):
            cart_product = request.user.cart.cart_product.create(product=new_product)
            cart_product.save()
        return redirect('user-cart')

