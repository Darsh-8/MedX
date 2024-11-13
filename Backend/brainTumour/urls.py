from django.urls import path

from .views import BrainTumourPrediction

urlpatterns = [
    path('', BrainTumourPrediction.as_view(),
         name='brain-tumour-predict'),
]
