from rest_framework import routers
from django.urls import path, include
from . import views
    
router = routers.DefaultRouter()
router.register('', views.BlogView)
    
urlpatterns = [
    path('', views.index),
    path('api/', include(router.urls)),
] 
