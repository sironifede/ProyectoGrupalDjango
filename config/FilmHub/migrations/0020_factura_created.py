# Generated by Django 2.2 on 2020-12-04 02:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0019_remove_asiento_reservado'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
