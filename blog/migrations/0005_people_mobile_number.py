# Generated by Django 4.1.4 on 2022-12-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_city_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='mobile number'),
        ),
    ]
