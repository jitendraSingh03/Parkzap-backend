# Generated by Django 3.2.7 on 2021-09-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_info',
            name='contact_dob',
            field=models.CharField(default='', max_length=20),
        ),
    ]