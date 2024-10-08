# Generated by Django 5.0.8 on 2024-08-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['flat', 'checkin']},
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AddIndex(
            model_name='booking',
            index=models.Index(fields=['flat', 'checkin'], name='Booking_boo_flat_id_15d837_idx'),
        ),
    ]
