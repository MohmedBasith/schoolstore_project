# Generated by Django 4.2.3 on 2023-11-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolstore_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='Year',
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(default='2002'),
            preserve_default=False,
        ),
    ]
