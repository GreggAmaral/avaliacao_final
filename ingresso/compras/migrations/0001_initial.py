# Generated by Django 4.2.7 on 2024-04-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254)),
                ('valor', models.IntegerField()),
                ('lugar', models.CharField(max_length=3)),
                ('comprado', models.BooleanField(default=False)),
            ],
        ),
    ]
