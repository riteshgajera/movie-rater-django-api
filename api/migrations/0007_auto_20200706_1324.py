# Generated by Django 3.0.7 on 2020-07-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200703_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='api/images/'),
        ),
    ]
