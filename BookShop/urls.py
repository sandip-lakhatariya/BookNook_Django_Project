from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("productview/<int:myid>", views.productview, name="productview"),
    path("shop/", views.shopview, name="shopview"),
    path("shop/<slug:data>", views.shopview, name="shopview"),
    path("Signup/", views.handle_signup, name="handlesignup"),
    path("Signin/", views.handle_signin, name="handlesignin"),
    path("Logout/", views.handle_logout, name="handlelogout"),
    path("Contact/", views.contactUs, name="contactUs"),
    path("About/", views.aboutUs, name="aboutUs"),
    path("Shoppingcart/", views.shoppingCart, name="shoppingCart"),
    path("Shipping/", views.shipping, name="shipping"),
    path("ship_order/", views.ship_order, name="shipOrder"),
    path("payment_test/", views.payment_test, name="payment_test"),
    path("success/", views.success, name="success"),
]
