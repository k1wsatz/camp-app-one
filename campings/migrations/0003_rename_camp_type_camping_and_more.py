# Generated by Django 4.0.3 on 2022-04-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campings', '0002_alter_camping_name_alter_camping_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='camp',
            new_name='camping',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='people_number',
            field=models.PositiveSmallIntegerField(verbose_name='number of people'),
        ),
    ]
