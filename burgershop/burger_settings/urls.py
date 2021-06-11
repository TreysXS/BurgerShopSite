from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('Бургеры/', include('list_product.urls')),
    path('Корзина/', include('cart.urls')),
    path('Профиль/', include('user_profile.urls')),
    path('Заказы/', include('orders.urls')),
    path('accounts/', include('allauth.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
