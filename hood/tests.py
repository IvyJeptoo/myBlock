from django.test import TestCase
from django.contrib.auth.models import User
from hood.models import *

# Create your tests here.
class BusinessTestCase(TestCase):
    """Set up for the models instances"""
    def setUp(self):
        self.user = User.objects.create(username='ivy',password='ivy123')
        self.business = Business.objects.create(name='hotel',user=self.user, contact=1234567890, location='kilimani', description='good food')
    
    def test_instance(self):
        """Test case to check if created business is an instance of business model class"""
        self.assertTrue(isinstance(self.business, Business))

    def test_save(self):
        """Test case to check if created business is being saved in our database"""
        self.business.save()
        all_businesses = Business.objects.all()
        self.assertEquals(len(all_businesses), 1)

    def test_update(self):
        """Test case to check if a saved business is being updated successfully"""

        self.business.name = 'new name'
        self.business.save()
        self.assertEquals(self.business.name,'new name')

    def test_delete(self):
        """Test case to check if a saved business is being removed from our db when deleted."""

        self.business.delete()
        all_businesses = Business.objects.all()
        self.assertEquals(len(all_businesses),0)

    def test_find_business_by_id(self):
        """Test case to check we can access the id of a saved business in the database."""
        self.business = Business.objects.create(name='hotel',user=self.user, contact=1234567890, location='kilimani', description='good food')
        self.business.save()
        found = Business.get_post(self.business.id)
        self.assertEquals(self.business, found)

class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='ivy',password='ivy123')
        self.post = Post.objects.create(user=self.user,  detail='take note')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save(self):
        self.post.save()
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)

    def test_update(self):
        self.post.detail = 'new detail'
        self.post.save()
        self.assertEquals(self.post.detail,'new detail')

    def test_delete(self):
        self.post.delete()
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts),0)

class ProfileTestCase(TestCase):

    def setUp(self):
      """Set up for the models instances"""
      self.user = User.objects.create(
            username='Tester', password='Test1234')
      self.profile = Profile(bio='This is my bio', photo='test.png', user=self.user, hood='sukari')


    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        """Test case to check if created profile is an instance of profile model class"""
        self.assertTrue(isinstance(self.profile, Profile))

    

   
    
    
    




