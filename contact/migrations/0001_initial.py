# Generated by Django 3.0.4 on 2020-03-22 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Khoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('khoa_name', models.CharField(max_length=100)),
                ('khoa_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bacsi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_bacsi', models.CharField(max_length=100)),
                ('bacsi_ngaysinh', models.DateTimeField()),
                ('bacsi_gioitinh', models.BooleanField(default='Nam')),
                ('bacsi_diachi', models.CharField(max_length=254)),
                ('mail_bacsi', models.EmailField(max_length=254)),
                ('anh_bacsi', models.ImageField(upload_to='static/images')),
                ('khoa_bacsi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Khoa')),
            ],
        ),
    ]
