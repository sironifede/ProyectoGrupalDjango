# Generated by Django 2.2 on 2020-11-19 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0004_auto_20201119_2154'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paquete',
            new_name='Factura',
        ),
        migrations.RemoveField(
            model_name='combo_comida',
            name='monto_total',
        ),
    ]