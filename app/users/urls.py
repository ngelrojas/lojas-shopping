from django.urls import path, re_path
from rest_framework_jwt.views import ObtainJSONWebToken
from users import views
from users.helper_views.activationUser import ActivationAccount
from users.helper_views.customUserLogin import CustomLoginUser
from users.helper_views.reactivateAccount import SendEmailReAccount
from users.helper_views.reactivateAccount import ReactivateAccount

app_name = 'user'

urlpatterns = [
    path('auth', ObtainJSONWebToken.as_view(serializer_class=CustomLoginUser)),
    path('user', views.CreateUserView.as_view(), name='create'),
    path('user/<int:pk>', views.UpdateUserView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'}), name='update'),
    re_path(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/'
            '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
            ActivationAccount.as_view(),
            name='activation'),
    path('recovery-password', views.RecoveryPasswordUser.as_view({
        'post': 'create'}), name='recovery-password'),
    path('recovery-confirm', views.RecoveryPwdConfirm.as_view({
        'put': 'update'}), name='recovery-confirm'),
    path('re-send-email', SendEmailReAccount.as_view(), name='re-send-email'),
    path('re-activate', ReactivateAccount.as_view({
        'put': 'update'}), name='re-activate-account'),
]
