from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Gallery(models.Model):
  pic = models.ImageField(upload_to="gallery",null=True, blank=True, default="/gallery/default.jpg")
  caption= models.CharField(default="", max_length=100, blank=True)

  def _str_(self):
    return str(self.owner)

class User(AbstractUser):
    name = models.CharField(max_length=10)
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    program = models.CharField(max_length=9)
    institution = models.CharField(max_length=15)
    number = models.CharField(max_length=10)
    field_of_interest = models.CharField(max_length=12)
    gender = models.CharField(max_length=7)
    placement_letter = models.CharField(max_length=2089)


class UserProfile(models.Model):
  owner= models.ForeignKey(User, on_delete=models.CASCADE)
  pp = models.ImageField(upload_to="profiles",null=True, blank=True, default="/profiles/default.jpg")

  def _str_(self):
    return str(self.owner)