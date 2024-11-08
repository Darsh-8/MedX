from django.urls import path
from .views import DiabetesPredictionView

# Define the URL pattern for the Diabetes Prediction API endpoint
urlpatterns = [
    path('', DiabetesPredictionView.as_view(), name='diabetes-prediction'),
    # Placeholder: Add more routes for additional endpoints, e.g., logging, configuration endpoints, etc.
]
