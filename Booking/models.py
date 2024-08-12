from django.db import models

class Flat(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    flat = models.ForeignKey(Flat, related_name='bookings', on_delete=models.CASCADE,db_index=True)
    checkin = models.DateField(db_index=True)
    checkout = models.DateField()
    class Meta:
        indexes = [
            models.Index(fields=['flat', 'checkin']),
        ]
        ordering = ['flat', 'checkin']
    def __str__(self):
        return f"Booking {self.id} for {self.flat.name}"
