from django.urls import path
from .views import BurgerListView, BurgerDetailView


urlpatterns = [
    path('', BurgerListView.as_view(), name='product-list'),
    path('<slug:slug>', BurgerDetailView.as_view(), name='product-detail'),
]