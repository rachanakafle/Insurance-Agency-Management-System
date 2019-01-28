# Generated by Django 2.1.3 on 2019-01-25 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CMS', '0002_agent_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applied_Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_assured', models.BigIntegerField()),
                ('premium_amount', models.BigIntegerField()),
                ('payment_method', models.CharField(choices=[('monthly', 'MONTHLY'), ('semiannual', 'SEMIANNUAL'), ('yearly', 'YEARLY')], default=None, max_length=20)),
                ('next_payment_date', models.DateTimeField()),
                ('client_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Client', to='CMS.Client')),
            ],
            options={
                'verbose_name_plural': 'Applied_policies',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_id', models.IntegerField(unique=True)),
                ('policy_name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('policy_type', models.CharField(max_length=200)),
                ('policy_period', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Policies',
            },
        ),
        migrations.AddField(
            model_name='applied_policy',
            name='policy_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='appliedname', to='policy.Policy'),
        ),
        migrations.AddField(
            model_name='applied_policy',
            name='policy_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Policy', to='policy.Policy'),
        ),
    ]
