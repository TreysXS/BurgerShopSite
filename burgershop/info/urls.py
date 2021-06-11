from django.urls import path

from .views import GeneralView

urlpatterns = [
    path('', GeneralView.as_view(), name='home')
]