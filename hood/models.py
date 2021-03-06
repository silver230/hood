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

class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profilir", on_delete=models.CASCADE)
    picture = ImageField(manual_crop='')
    contact = models.BigIntegerField()
    bio = models.TextField()
    email = models.EmailField()
    # neighbourhood = models.ForeignKey(Neighbourhood, related_name="pos", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('dump', kwargs={'pk':self.pk})


    @classmethod
    def get_all(cls):
        all_objects = Profile.objects.all()
        return all_objects

    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(user__name__icontains=search_term)
        return profile

    @classmethod
    def update_caption(cls,current_value,new_value):
        fetched_object = Profile.objects.filter(name=current_value).update(name=new_value)

    @classmethod
    def get_all(cls):
        profiles = Profile.objects.all()
        return profiles

    @classmethod
    def save_profile(self):
        return self.save()

    @classmethod
    def delete_profile(self):
        return self.delete()

    def __str__(self):
        return self.user.username
    
 