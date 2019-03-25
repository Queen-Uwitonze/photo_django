from django.test import TestCase
from .models import Images,Category,Location
# Create your tests here.
class ImagesTestClass(TestCase):
  def setUp(self):
      # Creating a new editor and saving it
      self.post = Images(post="image",image_url="Imageurl",image_name="benz",description="nice car you can buy it if you like it",images_location=self.place)
      self.flowers.save_post()

      # Creating a new location and saving it
      self.new_location = Locations(name = 'testing')
      self.new_location.save()

      self.new_category= Category(name = 'Test category')
      self.new_category.save()

      self.new_category.locations.add(self.new_location)

  def tearDown(self):
      Images.objects.all().delete()
      Locations.objects.all().delete()
      Category.objects.all().delete()

  def test_get_images_of_day(self):
        images_of_day = Images.images_of_day()
        self.assertTrue(len(images_of_day)>0)

    

class LocationTestClass(TestCase):
    def setUp(self):
         self.kigali=Location(name="kigali")

    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))

#     def saving_name(self):
#         self.place.save_places()
#         place = Location.objects.all()
            

class CategoryTestClass(TestCase):
    def setUp(self):
        self.natural = Category(name='natural')

    def test_instance(self):
        self.assertTrue(isinstance(self.natural, Category))

    # def saving_category(self):
    #     self.test.save_category()
    #     images = Category.objects.all()
      

    # def deleting_category(self):
    #     self.test = Category(category="natural")
    #     self.test.save_category()
    #     self.test.delete_locations()
    #     place = Category.objects.all()
        
