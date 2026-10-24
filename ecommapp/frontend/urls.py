from django.urls import path
from . views import main,ProductsSerial,contact,productview
from users.views import signin,logout_user,register
from account.views import dashboard
from cart.views import cart,cart_add,cart_remove,cart_update
urlpatterns = [
    path("",main,name="mainpage"),
    path("products",productview,name="products"),
    path("products/api",ProductsSerial.as_view(),name="productsapi"),
    path("login",signin,name="login"),
    path("register",register,name="register"),
    path("logout",logout_user,name="logout"),
    path("contact",contact,name="contact"),
    path("profile",dashboard,name="profile"),
    path("cart",cart,name="cart"),
    path("cart/addtocart",cart_add,name="addcart"),
    path("cart/removefromcart",cart_remove,name="removefromcart"),
    path("cart/updatecart",cart_update,name="updatecart"),
    
]