# Generated by Django 3.2.7 on 2023-04-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20230407_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='course_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Course name'),
        ),
    ]
