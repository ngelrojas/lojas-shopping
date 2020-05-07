from django.urls import path
from .views.profileBuyer import ProfileBuyerView
from .views.profileSeller import ProfileSellerView

app_name = 'profile'

urlpatterns = [
    path('profile-buyer/<int:pk>', ProfileBuyerView.as_view({
        'get': 'retrieve',
        'put': 'update'}), name='profile-buyer'),
    path('profile-seller', ProfileSellerView.as_view({
        'post': 'create'}), name='profile-seller'),
    path('profile-seller/<int:pk>', ProfileSellerView.as_view({
        'get': 'retrieve',
        'put': 'update'}), name='profile-seller-detail')
]
