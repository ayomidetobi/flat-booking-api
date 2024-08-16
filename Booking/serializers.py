from rest_framework import serializers
from .models import Flat, Booking
from datetime import date


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    previous_booking_id = serializers.ReadOnlyField()
    flat_name = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        checkin = data.get("checkin")
        checkout = data.get("checkout")

        if checkin < date.today():
            raise serializers.ValidationError(
                "Check-in date cannot be in the past."
            )

        if checkout <= checkin:
            raise serializers.ValidationError(
                "Check-out date must be after the check-in date."
            )

        return data

    # def get_previous_booking_id(self, obj):
    #     previous_booking = Booking.objects.filter(flat=obj.flat, checkin__lt=obj.checkin).order_by('-checkin').first()
    #     return previous_booking.id if previous_booking else None

    def get_flat_name(self, obj):
        return obj.flat.name if obj.flat else None
