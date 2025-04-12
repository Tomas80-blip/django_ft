# Generated by Django 5.1.7 on 2025-03-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registracija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vardas', models.CharField(max_length=100)),
                ('el_pastas', models.EmailField(max_length=254, unique=True)),
                ('skurta', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
