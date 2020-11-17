# Generated by Django 2.2 on 2020-11-17 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fila', models.CharField(max_length=1)),
                ('butaca', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('contenido_neto', models.IntegerField(blank=True, default=0, null=True)),
                ('precio_unidad', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('contenido_neto', models.IntegerField(blank=True, default=0, null=True)),
                ('precio_unidad', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('horario', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=100)),
                ('duracion', models.IntegerField(blank=True, default=0, null=True)),
                ('funcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Funcion')),
            ],
        ),
        migrations.CreateModel(
            name='Combo_Comida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cant_comida', models.IntegerField(blank=True, default=0, null=True)),
                ('cant_bebida', models.IntegerField(blank=True, default=0, null=True)),
                ('monto_total', models.IntegerField(blank=True, default=0, null=True)),
                ('bebida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Bebida')),
                ('comida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Comida')),
            ],
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(blank=True, default=0, null=True)),
                ('asiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Asiento')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Pelicula')),
            ],
        ),
    ]
