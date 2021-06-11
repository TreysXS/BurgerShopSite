from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View

from .permissions import AdminHasPermissionsMixin
from .service import get_order, order_delete
from .models import Order


class OrderListView(AdminHasPermissionsMixin, ListView):

    model = Order


class OrderDetailView(AdminHasPermissionsMixin, View):

    def get(self, request, id):
        """Displays the order page."""
        try:
            order = get_order(id)
        except Order.DoesNotExist:
            raise Http404
        return render(request, 'orders/order_detail.html', context={'order': order})

    def post(self, request, id):
        """Completes the order.Removes the order model."""
        order = get_order(id)
        order_delete(order)
        return redirect('order-list')