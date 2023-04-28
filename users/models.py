from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # Same as references in SQL
    image = models.ImageField(default='profilepic.png',upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username