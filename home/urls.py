from django.urls import path
from home.views.home import Index
from home.views.signup import Signup
from home.views.login import Login, Logout
from home.views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView

urlpatterns = [
    path('', Index.as_view(), name = "homepage"),
    path('signup', Signup.as_view(), name = "signup"),
    path('login', Login.as_view(), name = "login"),
    path('logout', Logout, name = "logout"),
    path('cart', Cart.as_view(), name = "cart"),
    path('check-out', CheckOut.as_view(), name = "checkout"),
    path('orders', OrderView.as_view(), name ="orders"),
]