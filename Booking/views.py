from rest_framework import viewsets
from .models import Flat, Booking
from .serializers import FlatSerializer, BookingSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 50


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all().order_by("id")
    serializer_class = FlatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [OrderingFilter]
    filterset_fields = ["flat", "checkin"]
    ordering_fields = ["checkin", "checkout"]
    ordering = ["checkin"]
    pagination_class = CustomPageNumberPagination
