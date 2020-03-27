from django.db import models

# Create your models here.
class Khoa(models.Model):
    khoa_name = models.CharField(max_length=100)
    khoa_time = models.DateTimeField()

class Bacsi(models.Model):
    khoa_bacsi = models.ForeignKey(Khoa, on_delete=models.CASCADE)
    ten_bacsi = models.CharField(max_length=100)
    bacsi_ngaysinh = models.DateTimeField()
    bacsi_gioitinh = models.BooleanField(default=0)
    bacsi_diachi = models.CharField(max_length=254)
    mail_bacsi = models.EmailField(max_length=254)
    anh_bacsi = models.ImageField(upload_to='static/images')
