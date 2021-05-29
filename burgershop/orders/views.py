from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View

from .models import Order
from .permissions import AdminHasPermissionsMixin


class OrderListView(AdminHasPermissionsMixin, ListView):
    model = Order


class OrderDetailView(AdminHasPermissionsMixin, View):

    def get(self, request, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            raise Http404
        return render(request, 'orders/order_detail.html', context={'order': order})

    def post(self, request, id):
        id = request.POST.get('id')
        order = Order.objects.get(id=id)
        order.cart_products.all().delete()
        order.delete()
        return redirect('order-list')