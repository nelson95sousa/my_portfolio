from django.db import models

# Create your models here.


class Portfolio_Picture(models.Model):
    
    class ImageCategory(models.TextChoices):
        CITY = 'city'
        NATURE = 'nature'
        PANORAMA = 'panorama'
        LONG_EXPOSURE = 'long_exposure'
    
    image = models.ImageField(upload_to='images', unique=True)

    image_name = models.CharField(max_length=50, unique=True)

    image_category=models.CharField(max_length=19, choices=ImageCategory.choices)

    def __str__(self):
        return self.image_category + ' - ' + self.image_name


    