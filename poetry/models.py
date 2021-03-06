from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
from cloudinary.models import CloudinaryField
from datetime import datetime, date
from tinymce.models import HTMLField


# Create your models here.

class Spiritual(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w')
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Spiritual'

class Love(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Love'

class Death(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Death'

class Family(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Family'

class Famous(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Famous'


class Anger(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w')
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Anger'


class Friendship(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w')
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Friendship'


class Holiday(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Holiday'


class Life(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Life'


class Nature(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Nature'


class Sad(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Sad'


class Coronavirus(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Coronavirus'


class Christian(models.Model):
    image = cloudinary.models.CloudinaryField('profile_pics', default='https://unsplash.com/photos/zhgj7ZEUf1w') 
    title=models.CharField(max_length=20)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} Christian'


# class Love(models.Model):
#     computer=CloudinaryField('computers/', blank=True)
#     computer_name=models.CharField(max_length=30)
#     Operating_system=models.ForeignKey(Operatingsystem, on_delete=models.CASCADE, blank=True,null=True)
#     Ip_address=models.CharField(max_length=20)
#     Mac_address=models.CharField(max_length=30)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
#     location=models.CharField(max_length=30)
#     posted_date=models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.computer_name} Computer'