from django.urls import path
from .views import MenuView, index,  MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),
    path("menu_items/", MenuItemsView.as_view()),
    path("menu_items/<int:pk>", SingleMenuItemView.as_view()),
    path("menu/", MenuView.as_view(), name="menu"),
    path("api-token-auth/", obtain_auth_token)
]
