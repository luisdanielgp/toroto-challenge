# Generated by Django 2.2 on 2020-04-30 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200430_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='subscription',
        ),
    ]