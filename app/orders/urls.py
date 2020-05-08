from django.urls import path
from .views import OrderView


app_name = 'order'


urlpatterns = [
    path('order', OrderView.as_view({
        'post': 'create',
        'get': 'list'}), name='order'),
    path('order/<int:pk>', OrderView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'}), name='order-detail'),
]
