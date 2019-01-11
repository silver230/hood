from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Neighbourhood(models.Model):
    user = models.ForeignKey(User, related_name="poster", on_delete=models.CASCADE)
    location = models.CharField(max_length=40,blank=True)
    name = models.CharField(max_length=40,blank=True)
    occupants_count = models.IntegerField(default=0)
    area = ImageField(manual_crop='')


    @classmethod
    def get_all(cls):
        neighbourhood = Neighbourhood.objects.all()
        return neighbourhood

    @classmethod
    def save_neighbourhood(self):
        return self.save()

    @classmethod
    def delete_neighbourhood(self):
        return self.delete()


    def __str__(self):
        return self.name


    
