# Generated by Django 2.1.11 on 2019-08-29 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_heartrate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarmtask',
            name='sound',
        ),
        migrations.DeleteModel(
            name='Sound',
        ),
    ]