# Generated by Django 4.2 on 2023-04-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurring',
            name='until',
            field=models.DateField(blank=True, null=True),
        ),
    ]