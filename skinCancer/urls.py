from django.urls import path

from .views import SkinCancer

# URL configuration for the skin cancer prediction API
urlpatterns = [
    path('', SkinCancer.as_view(), name='skin-cancer-prediction'),
]
