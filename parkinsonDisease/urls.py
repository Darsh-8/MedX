from django.urls import path

from .views import ParkinsonPredictionView

# URL pattern for the Parkinson's Disease Prediction API endpoint
urlpatterns = [
    path('', ParkinsonPredictionView.as_view(), name='predict'),
    # Placeholder: Add more routes as needed (e.g., for logging or an admin panel)
]
