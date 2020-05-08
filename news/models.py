from django.db import models

# Create your models here.
class News(models.Model):
    new_name = models.CharField(max_length=1000)
    author_name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date_time = models.DateField()
    date_write = models.DateField()
    picture = models.ImageField(upload_to="new_picture")
    

    def __str__(self):
        return self.new_name