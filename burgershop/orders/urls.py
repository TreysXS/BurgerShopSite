from django.urls import path

from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('<uuid:id>', OrderDetailView.as_view(), name='order-detail'),
]