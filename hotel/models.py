from django.db import models

class Villa(models.Model):
    name = models.CharField(max_length=255)
    metr = models.IntegerField()
    url = models.CharField(max_length=255, default=None, blank=True, null=True)
    bedrooms = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)
    inpageimg = models.ImageField(upload_to="",default=None)
    updated = models.TimeField(auto_now=True)
    created = models.TimeField(auto_now_add=True)
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
         return self.image.url
        

class Genel(models.Model):
     name = models.CharField(max_length=255)
     image = models.ImageField(upload_to="",  default=None, blank=True, null=True)
       
class Havuz(models.Model):
     name = models.CharField(max_length=255)
     image = models.ImageField(upload_to="",  default=None, blank=True, null=True)

class Galleryvilla(models.Model):
     name = models.CharField(max_length=255)
     image = models.ImageField(upload_to="",  default=None, blank=True, null=True)

class Aktivite(models.Model):
     name = models.CharField(max_length=255)
     image = models.ImageField(upload_to="",  default=None, blank=True, null=True)
    
class Restoran(models.Model):
     name = models.CharField(max_length=255)
     image = models.ImageField(upload_to="",  default=None, blank=True, null=True)

class Spa(models.Model):
     name = models.CharField(max_length=255)
     image = models.ImageField(upload_to="",  default=None, blank=True, null=True)
def __str__(self) :
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    page_info1 = models.TextField(null=True)
    page_info2 = models.TextField(null=True)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)
    updated = models.TimeField(auto_now=True)
    created = models.TimeField(auto_now_add=True)
    @property
    def food_image_url(self):
        if self.image and hasattr(self.image, 'url'):
         return self.image.url
