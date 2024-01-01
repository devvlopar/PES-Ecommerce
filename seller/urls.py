from django.urls import path
from seller.views import *

urlpatterns = [
    path('', index_view, name='seller_index'),
    path('register/', register_view, name="seller_register"),
    path('login/', login_view, name="seller_login"),
    path('otp/', otp_view, name="seller_otp"),
   
]