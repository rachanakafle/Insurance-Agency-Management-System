# Generated by Django 2.1.3 on 2019-01-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0002_agent_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='Education_level',
            field=models.CharField(choices=[('see', 'SEE'), ('Bachelors', 'BACHELORS'), ('Master', 'MASTER')], default=None, max_length=200),
        ),
    ]
