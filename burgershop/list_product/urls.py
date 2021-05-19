from django.urls import path
from .views import BurgerListView


urlpatterns = [
    path('', BurgerListView.as_view(), name='product-list')
]