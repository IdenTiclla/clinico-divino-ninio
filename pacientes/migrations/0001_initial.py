# Generated by Django 4.1.7 on 2023-03-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('ci', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Paciente',
            },
        ),
    ]