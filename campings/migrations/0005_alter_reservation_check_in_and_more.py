# Generated by Django 4.0.3 on 2022-04-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campings', '0004_rename_end_date_reservation_check_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(),
        ),
    ]