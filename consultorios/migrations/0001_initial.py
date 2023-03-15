# Generated by Django 4.1.7 on 2023-03-15 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctores', '__first__'),
        ('especialidades', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctores.doctor')),
                ('especialidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='especialidades.especialidad')),
            ],
            options={
                'db_table': 'Consultorio',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.TimeField()),
                ('fin', models.TimeField()),
                ('turno', models.CharField(max_length=20)),
                ('consultorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultorios.consultorio')),
            ],
            options={
                'db_table': 'Horario',
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('consultorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultorios.consultorio')),
            ],
            options={
                'db_table': 'Equipo',
            },
        ),
    ]
