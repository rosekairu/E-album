import datetime as dt
from django.db import models
from cloudinary.models import CloudinaryField


# category and location.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()



# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    #image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE,)
    location = models.ForeignKey(Location, on_delete = models.CASCADE,)
    
    

    
    @classmethod
    def get_all_images(cls):
        images = cls.objects.order_by()
        return images

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def filter_by_category(cls, id):
        images = cls.objects.filter(category_id=id)
        return images

    @classmethod
    def filter_by_location(cls,id):
        images = cls.objects.filter(location_id=id)
        return images

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    

