from django.db import models

# Create your models here.
class UserData(models.Model):
    username = models.CharField(max_length=255)
    # file = models.FileField(upload_to='userdata/')
    file = models.ImageField(upload_to='userdata/')
