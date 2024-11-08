from django.urls import include, path

urlpatterns = [
    path('skin-cancer/', include('skinCancer.urls')),
    path('brain-tumour/', include('brainTumour.urls')),
    path('parkinson-disease/', include('parkinsonDisease.urls')),
    path('diabetes-prediction/', include('diabetes.urls')),
    path('heart-attack-prediction/', include('heartAttack.urls')),

]
