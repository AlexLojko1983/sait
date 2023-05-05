# Generated by Django 4.2 on 2023-05-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('prise', models.DecimalField(decimal_places=2, max_digits=7)),
                ('unit', models.CharField(max_length=2)),
            ],
        ),
    ]