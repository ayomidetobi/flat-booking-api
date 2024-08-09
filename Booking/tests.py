from datetime import date

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Booking, Flat


class FlatAndBookingTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    # Unit tests
    def test_flat_creation(self):
        flat = Flat.objects.create(name="Flat-1")
        self.assertEqual(flat.name, "Flat-1")

    def test_flat_str_method(self):
        flat = Flat.objects.create(name="Flat-1")
        self.assertEqual(str(flat), "Flat-1")

    def test_booking_creation(self):
        flat = Flat.objects.create(name="Flat-1")
        booking = Booking.objects.create(flat=flat, checkin=date(2022, 1, 1), checkout=date(2022, 1, 13))
        self.assertEqual(booking.flat, flat)
        self.assertEqual(booking.checkin, date(2022, 1, 1))
        self.assertEqual(booking.checkout, date(2022, 1, 13))

    def test_booking_str_method(self):
        flat = Flat.objects.create(name="Flat-1")
        booking = Booking.objects.create(flat=flat, checkin=date(2022, 1, 1), checkout=date(2022, 1, 13))
        expected_str = f"Booking {booking.id} for {flat.name}"
        self.assertEqual(str(booking), expected_str)

    # End-to-end tests
    def test_flat_list_view(self):
        Flat.objects.create(name="Flat-1")
        Flat.objects.create(name="Flat-2")

        url = reverse('flat-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], "Flat-1")

    def test_flat_detail_view(self):
        flat = Flat.objects.create(name="Flat-1")
        
        url = reverse('flat-detail', kwargs={'pk': flat.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Flat-1")

    def test_booking_create_view(self):
        flat = Flat.objects.create(name="Flat-1")
        data = {
            'flat': flat.pk,
            'checkin': '2024-11-01',
            'checkout': '2024-11-10',
        }

        url = reverse('booking-list')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.get()
        self.assertEqual(booking.flat, flat)
        self.assertEqual(str(booking.checkin), '2024-11-01')
        self.assertEqual(str(booking.checkout), '2024-11-10')

    def test_booking_list_view(self):
        flat = Flat.objects.create(name="Flat-1")
        Booking.objects.create(flat=flat, checkin=date(2023, 1, 1), checkout=date(2023, 1, 10))

        url = reverse('booking-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['flat'], flat.pk)
        self.assertEqual(response.data['results'][0]['checkin'], '2023-01-01')
        self.assertEqual(response.data['results'][0]['checkout'], '2023-01-10')

    def test_booking_detail_view(self):
        flat = Flat.objects.create(name="Flat-1")
        booking = Booking.objects.create(flat=flat, checkin=date(2023, 1, 1), checkout=date(2023, 1, 10))

        url = reverse('booking-detail', kwargs={'pk': booking.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['flat'], flat.pk)
        self.assertEqual(response.data['checkin'], '2023-01-01')
        self.assertEqual(response.data['checkout'], '2023-01-10')

    def test_create_booking_with_invalid_flat_data(self):
        invalid_data = {
            'flat': 999,
            'checkin': '2023-01-01',
            'checkout': '2023-01-10',
        }
        create_booking_url = reverse('booking-list')
        response = self.client.post(create_booking_url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_booking_with_invalid_date(self):
        flat = Flat.objects.create(name="Flat-1")

        invalid_data = {
            'flat': flat.id,
            'checkin': '2023-01-01',
            'checkout': '2022-12-30',
        }
        create_booking_url = reverse('booking-list')
        response = self.client.post(create_booking_url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    def test_booking_list_view_sort_checkin_asc(self):
        flat = Flat.objects.create(name="Flat-1")
        Booking.objects.create(flat=flat, checkin=date(2023, 1, 1), checkout=date(2023, 1, 10))
        Booking.objects.create(flat=flat, checkin=date(2022, 12, 1), checkout=date(2022, 12, 10))

        url = reverse('booking-list') + '?ordering=checkin'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['checkin'], '2022-12-01')
        self.assertEqual(response.data['results'][1]['checkin'], '2023-01-01')

    def test_booking_list_view_sort_checkin_desc(self):
        flat = Flat.objects.create(name="Flat-1")
        Booking.objects.create(flat=flat, checkin=date(2023, 1, 1), checkout=date(2023, 1, 10))
        Booking.objects.create(flat=flat, checkin=date(2022, 12, 1), checkout=date(2022, 12, 10))

        url = reverse('booking-list') + '?ordering=-checkin'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['checkin'], '2023-01-01')
        self.assertEqual(response.data['results'][1]['checkin'], '2022-12-01')
    def test_booking_list_view_pagination(self):
        flat = Flat.objects.create(name="Flat-1")
        for i in range(15):  # Create 15 bookings
            Booking.objects.create(flat=flat, checkin=date(2023, 1, 1), checkout=date(2023, 1, 10))

        url = reverse('booking-list') + '?page=2&page_size=10'  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)  
        self.assertEqual(response.data['results'][0]['checkin'], '2023-01-01') 

    def test_booking_list_view_default_page_size(self):
        flat = Flat.objects.create(name="Flat-1")
        for i in range(15):  # Create 15 bookings
            Booking.objects.create(flat=flat, checkin=date(2023, 1, 1), checkout=date(2023, 1, 10))

        url = reverse('booking-list')  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)  

    def test_booking_list_view_max_page_size(self):
        flat = Flat.objects.create(name="Flat-1")
        for i in range(25):  
            Booking.objects.create(flat=flat, checkin=date(2023, 1, 1), checkout=date(2023, 1, 10))

        url = reverse('booking-list') + '?page_size=20'  
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 20) 

