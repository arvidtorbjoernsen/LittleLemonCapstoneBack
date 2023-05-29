from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.views.generic.base import RedirectView

from restaurant import views

router = DefaultRouter()

router.register(r"tables", views.BookingViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurant/", include("restaurant.urls")),
    path("restaurant/booking/", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    re_path("", RedirectView.as_view(url="restaurant/", permanent=True))
]
