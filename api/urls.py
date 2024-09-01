
from django.urls import path,include
from . import views

urlpatterns = [
   path('', views.hello),
   path('upload/', views.upload),
   path('detect/', views.detect),
]
