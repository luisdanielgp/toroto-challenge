# Generated by Django 2.2 on 2020-04-30 08:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('monthly_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('co2_tons_per_month', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
