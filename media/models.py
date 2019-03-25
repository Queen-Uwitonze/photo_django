from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Images(models.Model):
    post =models.ImageField(upload_to='gallery/')
    images_name = models.CharField(max_length =30)
    images_description = models.CharField(max_length =60)
    images_category = models.ForeignKey(Category)
    images_location = models.ForeignKey(Location)
    
    def __str__(self):
      return self.images_name

    @classmethod
    def get_images(cls,post_id):
        images = Images.objects.get(id=post_id)
        return images     

    @classmethod
    def get_all_images(cls):
            images = Images.objects.all()
            return images 
    
    @classmethod
    def search_by_category(cls,search_term):
        images=cls.objects.filter(images_category__name__icontains=search_term)
    
        return images  

    @classmethod
    def filter_by_location(cls,search_term):
        images=cls.objects.filter(images_location__name__icontains=search_term)
    
        return images       
    
    def save_images(self):
        self.save()

    def delete_images(self):
      self.remove()
    
    def update_images(self):
      self.remove()
    
    def get_image_by_id(id):
      pass
     
    def search_results(images):
      pass
    
    def filter_by_location(request,location_id):
      pass
    class Meta:
        ordering = ['images_name']

class GalleryLetterForm(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


