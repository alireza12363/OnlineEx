# Generated by Django 3.2.7 on 2021-09-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sessions', '0002_auto_20210926_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseexamsession',
            name='session_descriptions',
            field=models.CharField(default='Description', max_length=150, verbose_name='Session descriptions'),
        ),
        migrations.AddField(
            model_name='courseexamsession',
            name='session_name',
            field=models.CharField(default='New Session', max_length=20, verbose_name='Session name'),
        ),
        migrations.AddField(
            model_name='subjectexamsession',
            name='session_descriptions',
            field=models.CharField(default='Description', max_length=150, verbose_name='Session descriptions'),
        ),
        migrations.AddField(
            model_name='subjectexamsession',
            name='session_name',
            field=models.CharField(default='New Session', max_length=20, verbose_name='Session name'),
        ),
    ]
