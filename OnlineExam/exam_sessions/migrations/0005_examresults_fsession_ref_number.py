# Generated by Django 3.2.7 on 2023-04-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sessions', '0004_auto_20230409_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='examresults',
            name='fsession_ref_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Free Session reference code'),
        ),
    ]
