# Generated by Django 4.1.4 on 2022-12-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='passport',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='passport'),
        ),
    ]
