# Generated by Django 3.0.4 on 2020-06-10 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footage_app', '0003_auto_20200609_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal',
            name='terminal_name',
            field=models.CharField(max_length=30),
        ),
    ]