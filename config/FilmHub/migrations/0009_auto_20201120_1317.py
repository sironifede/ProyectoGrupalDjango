# Generated by Django 2.2 on 2020-11-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0008_auto_20201120_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(default='default.jpg', upload_to='portadas'),
        ),
    ]
