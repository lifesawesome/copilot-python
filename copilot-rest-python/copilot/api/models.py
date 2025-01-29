from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics')
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
