# Generated by Django 4.2.2 on 2023-07-26 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 26, 17, 32, 48, 791157, tzinfo=datetime.timezone.utc)),
        ),
    ]
