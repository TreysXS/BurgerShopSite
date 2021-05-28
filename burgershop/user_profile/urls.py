from django.urls import path
from .views import UserProfileDetail, UserProfileUpdate


urlpatterns = [
    path('', UserProfileDetail.as_view(), name='user-profile'),
    path('Обновить/', UserProfileUpdate.as_view(), name='user-update'),
]