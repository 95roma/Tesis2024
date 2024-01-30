# Generated by Django 3.0.6 on 2022-10-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ocupacion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'ocupacion',
                'verbose_name_plural': 'ocupacions',
                'db_table': 'ocupacion',
            },
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salariomaximo', models.FloatField(max_length=8)),
                ('salariominimo', models.FloatField(max_length=8)),
            ],
            options={
                'verbose_name': 'salario',
                'verbose_name_plural': 'salarios',
                'db_table': 'salario',
            },
        ),
    ]