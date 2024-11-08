from django.urls import path

from .views import HeartAttackPredictionView

# Define the URL pattern for Heart Attack Prediction API endpoint
urlpatterns = [
    path('', HeartAttackPredictionView.as_view(),
         name='heart-attack-predictions'),
    # Placeholder: Add more routes for additional endpoints like logging or health checks
]
