# Generated by Django 2.2 on 2020-04-19 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20200414_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
    ]