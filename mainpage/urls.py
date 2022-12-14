from django.urls import path
from mainpage import views

app_name='mainpage'

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('my_gear/', views.my_gear, name='my_gear'),
    path('techniques/', views.techniques, name='techniques'),
    path('contact/', views.contact, name='contact'),
    path('panorama/',views.panorama,name='panorama'),
    path('long_exposure',views.long_exposure, name='long_exposure'),
    path('post_processing',views.post_processing, name='post_processing'),
]