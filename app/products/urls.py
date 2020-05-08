from django.urls import path
from .views import ProductView

app_name = 'product'

urlpatterns = [
    path('product', ProductView.as_view({
        'get': 'list',
        'post': 'create'}), name='product'),
    path('product/<int:pk>', ProductView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'}), name='product-detail'),
]
