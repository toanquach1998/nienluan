from django.db import models

# Create your models here.
class Khoa(models.Model):
    khoa_name = models.CharField(max_length=100)
    khoa_time = models.DateTimeField()
    
    def __str__(self):
        return self.khoa_name

class Bacsi(models.Model):
    khoa_bacsi = models.ForeignKey(Khoa, on_delete=models.CASCADE)
    ten_bacsi = models.CharField(max_length=100, blank = False, null = False)
    bacsi_ngaysinh = models.DateTimeField()
    bacsi_gioitinh = models.BooleanField(default=0)
    bacsi_diachi = models.CharField(max_length=254)
    mail_bacsi = models.EmailField(max_length=254)
    anh_bacsi = models.ImageField(upload_to='static/images')
    
    def __str__(self):
        return self.ten_bacsi



class Contacts(models.Model):
    sex_choice = ((0, "Nữ"), (1, "Nam"), (2, "Giới tính khác"))
    time_choice = (
        (0, "7:30-8:00"),
        (1, "8:05-8:35"),
        (2, "8:40-9:10"),
        (3, "9:15-9:45"),
        (4, "9:50-10:20"),
        (5, "10:25-10:55"),
        (6, "11:00-11:30"),
        (7, "13:30-14:00"),
        (8, "14:05-14:35"),
        (9, "14:40-15:10"),
        (10, "15:15-15:45"),
        (11, "15:50-16:20"),
        (12, "16:25-17:55"),
    )
    contact_name = models.CharField(max_length=1000)
    contact_old = models.CharField(max_length=100)
    contact_sex = models.IntegerField(choices=sex_choice, default=0)
    contact_mail = models.EmailField(max_length=254)
    contact_phone = models.CharField(max_length=10)
    contact_time = models.IntegerField(choices=time_choice, default=0)
    contact_problem = models.CharField(max_length=254)
    contact_note = models.CharField(max_length=254)

    def __str__(self):
        return self.contact_name

