from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Naivasha')
        self.location.save_location()

        self.category = Category(name='home')
        self.category.save_category()

        self.image_test = Image(id=1, name='image', description='this is a testing image', location=self.location,
                                category=self.category)
    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image)) 

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)                               