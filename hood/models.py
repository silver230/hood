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


class Business(models.Model):
    user = models.ForeignKey(User, related_name="silver", on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name="neigh", on_delete=models.CASCADE)
    business_name = models.CharField(max_length=40)
    business_emails = models.CharField(max_length=40)
    

    def get_absolute_url(self):
        return reverse('dump', kwargs={'pk':self.pk})


    def __str__(self):
        return self.business_name

    @classmethod
    def show_business(cls):
        business = cls.objects.order_by('business_name')
        return business


    @classmethod
    def get_business(cls, id):
        business = cls.objects.get(id=id)
        return business

    @classmethod
    def search_by_name(cls,search_term):
        business=cls.objects.filter(business_name__icontains=search_term)
        return business

    
 