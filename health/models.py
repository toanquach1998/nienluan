from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    sex_choice = ((0, "Nữ"), (1, "Nam"), (2, "Không xác định"))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=sex_choice, default=0)
    address = models.CharField(default="", max_length=300)
    phone_number = models.CharField(max_length=10)
    citizen_identity_card = models.CharField(max_length=9)
    image_cic_befor = models.ImageField(upload_to="new_picture/Citizen_Identity_card/Before")
    image_cic_after = models.ImageField(upload_to="new_picture/Citizen_Identity_card/After")
    