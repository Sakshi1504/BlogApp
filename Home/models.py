from django.db import models
from django.db.models.fields import SlugField, TextField
from django.utils.text import slugify
from froala_editor.fields import FroalaField
from .helpers import *
from django.contrib.auth.models import User
# Create your models here.

class BlogModel(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=1000, null=True, blank=True)
    content=FroalaField(theme='dark')
    user=models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    img=models.ImageField(upload_to="pics")
    createdAt=models.DateTimeField(auto_now_add=True) #updated one time, when probably model is created
    uploadto=models.DateTimeField(auto_now=True) #updated every time model is updated

    def __str__(self):  
        return self.title

    #overriding save method
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    isverified=models.BooleanField(default=False)
    token = models.CharField(max_length=100)