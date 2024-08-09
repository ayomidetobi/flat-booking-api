from django.db import models

class Flat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    flat = models.ForeignKey(Flat, related_name='bookings', on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"Booking {self.id} for {self.flat.name}"
