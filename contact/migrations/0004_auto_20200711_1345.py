# Generated by Django 2.0.13 on 2020-07-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='author_name',
            new_name='contact_old',
        ),
        migrations.AlterField(
            model_name='contacts',
            name='contact_time',
            field=models.IntegerField(choices=[(0, '7:30-8:00'), (1, '8:05-8:35'), (2, '8:40-9:10'), (3, '9:15-9:45'), (4, '9:50-10:20'), (5, '10:25-10:55'), (6, '11:00-11:30'), (7, '13:30-14:00'), (8, '14:05-14:35'), (9, '14:40-15:10'), (10, '15:15-15:45'), (11, '15:50-16:20'), (12, '16:25-17:55')], default=0),
        ),
    ]
