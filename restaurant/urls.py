from django.urls import path 
from restaurant.views import index
from restaurant.views import menu
from restaurant.views import about
from restaurant.views import book
from restaurant.views import display_menu_item
from restaurant.views import SuccessView


app_name='restaurant'
urlpatterns = [ 
    path('', index, name="index"), 
    path('about/', about, name="about"),
    path('menu/',menu, name="menu"),
    path('menu_item/<int:pk>/', display_menu_item, name="menu_item"),
    path('book/', book, name="book"),
    path("success/", SuccessView.as_view(), name="success"),
] 