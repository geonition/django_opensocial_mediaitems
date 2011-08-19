from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class mediaItemsTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user('user1', 'test1@test.com', 'user1')
        self.user2 = User.objects.create_user('user2', 'test2@test.com', 'user2')
        self.user3 = User.objects.create_user('user3', 'test3@test.com', 'user3')    
        self.user4 = User.objects.create_user('user4', 'test4@test.com', 'user4')
        
        self.group1 = Group(name='@family')
        self.group1.save()
    
    def test_mediaitems_rest(self):
        base_url = reverse('mediaItems')
        self.client.get(base_url)
        
        url = "%s%s" % (base_url, "/user1")
        self.client.get(url)
        
        url = "%s%s" % (base_url, "/@me/@family")
        self.client.get(url)
        
        url = "%s%s" % (base_url, "/@me/@self")
        self.client.get(url)
        
        url = "%s%s" % (base_url, "/@me/@self/@all")
        self.client.get(url)
        
        url = "%s%s" % (base_url, "/@me/@self/@all/pic_home")
        self.client.get(url)
        
