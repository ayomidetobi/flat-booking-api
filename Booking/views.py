from rest_framework import viewsets
from .models import Flat, Booking
from .serializers import FlatSerializer, BookingSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django.db.models import OuterRef, Subquery


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 50


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all().order_by("id")
    serializer_class = FlatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    # queryset = Booking.objects.select_related('flat').all()
    serializer_class = BookingSerializer
    filter_backends = [OrderingFilter]
    filterset_fields = ["flat", "checkin"]
    ordering_fields = ["checkin", "flat"]
    ordering = ["flat","checkin"]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        latest_booking_subquery = Booking.objects.filter(
            flat=OuterRef('flat_id'),
            checkin__lt=OuterRef('checkin')
        ).order_by('-checkin').values('id')[:1]

        return Booking.objects.select_related('flat').annotate(
            previous_booking_id=Subquery(latest_booking_subquery)
        )