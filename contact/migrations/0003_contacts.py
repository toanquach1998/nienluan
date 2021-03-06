# Generated by Django 2.0.13 on 2020-07-11 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200501_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=1000)),
                ('author_name', models.CharField(max_length=100)),
                ('contact_sex', models.IntegerField(choices=[(0, 'Nữ'), (1, 'Nam'), (2, 'Giới tính khác')], default=0)),
                ('contact_mail', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=10)),
                ('contact_time', models.IntegerField(choices=[(0, 'Nữ'), (1, 'Nam'), (2, 'Giới tính khác')], default=0)),
                ('contact_problem', models.CharField(max_length=254)),
                ('contact_note', models.CharField(max_length=254)),
            ],
        ),
    ]
