from django.urls import path
from portfolio import views

app_name='portfolio'

urlpatterns=[
    path('city/', views.city, name='city'),
    path('nature/', views.nature, name='nature'),
    path('panorama/', views.panorama, name='panorama'),
    path('long_exposure/', views.long_exposure, name='long_exposure'),
] 