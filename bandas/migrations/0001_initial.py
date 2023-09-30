# Generated by Django 4.2.5 on 2023-09-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
    ]
