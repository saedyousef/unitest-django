# Generated by Django 3.0.5 on 2020-04-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight'),
        ),
    ]
