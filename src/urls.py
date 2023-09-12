from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views.category import CategoryViewSet


router = DefaultRouter()
router.register('category',CategoryViewSet)
urlpatterns = [
    path('api/',include(router.urls)),
]