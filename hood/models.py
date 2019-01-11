from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    user = models.ForeignKey(User, related_name="poster", on_delete=models.CASCADE)
    neighbourhood_location = models.CharField(max_length=40)
    neighbourhood_name = models.CharField(max_length=40)
    occupants_count = models.IntegerField(default=0)
    area = ImageField(manual_crop='')

    def __str__(self):
        return self.name


    
