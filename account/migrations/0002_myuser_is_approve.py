# Generated by Django 2.1.3 on 2019-02-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_approve',
            field=models.BooleanField(default=False),
        ),
    ]
