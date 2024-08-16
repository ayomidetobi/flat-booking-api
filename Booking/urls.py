from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlatViewSet, BookingViewSet

router = DefaultRouter()
router.register('flats', FlatViewSet)
router.register('bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]
