# Generated by Django 3.1.5 on 2024-04-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otheracademic', '0002_auto_20240411_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveformtable',
            name='hod',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
