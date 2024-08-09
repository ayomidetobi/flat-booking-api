from django.contrib import admin
from .models import Flat, Booking

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    fields = ('id', 'checkin', 'checkout')

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [BookingInline]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'flat', 'checkin', 'checkout')
    list_filter = ('flat', 'checkin', 'checkout')
    search_fields = ('flat__name',)
