# Generated by Django 2.1.3 on 2019-02-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_myuser_is_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='agent',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='client',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]