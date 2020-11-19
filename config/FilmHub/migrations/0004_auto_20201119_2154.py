# Generated by Django 2.2 on 2020-11-19 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0003_auto_20201119_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boleto',
            name='monto_total',
        ),
        migrations.RemoveField(
            model_name='boleto',
            name='pelicula',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='funcion',
        ),
        migrations.AddField(
            model_name='boleto',
            name='funcion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Funcion'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='pelicula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Pelicula'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='sala',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Sala'),
        ),
        migrations.AlterField(
            model_name='boleto',
            name='asiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Asiento'),
        ),
        migrations.AlterField(
            model_name='boleto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='funcion',
            name='horario',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.TimeField(null=True),
        ),
    ]
