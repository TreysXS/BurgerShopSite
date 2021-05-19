from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import BurgerProduct


class BurgerListView(ListView):
    """"""
    model = BurgerProduct
