
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cinemas'

router = routers.DefaultRouter()
router.register('', views.CinemaViewSet, basename='cinemas')

urlpatterns = [
    path('', include(router.urls) )
]