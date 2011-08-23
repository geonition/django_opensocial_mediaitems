from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from models import MediaItem
import os
import json

class mediaItemsTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user('user1', 'test1@test.com', 'user1')
        self.user2 = User.objects.create_user('user2', 'test2@test.com', 'user2')
        self.user3 = User.objects.create_user('user3', 'test3@test.com', 'user3')    
        self.user4 = User.objects.create_user('user4', 'test4@test.com', 'user4')
        
        self.group1 = Group(name='@family')
        self.group1.save()
        
        #create some media items
        root = os.path.dirname(__file__)
        f = open("%s%s" % (root, '/tests/test_pic.JPG'), 'rb')
        f.close()
        
        mi1 = MediaItem(owner_id=self.user1,
                        media_file='./tests/test_pic.JPG').save()
        mi2 = MediaItem(owner_id=self.user1,
                        media_file='./tests/test_pic.JPG').save()
        mi3 = MediaItem(owner_id=self.user2,
                        media_file='./tests/test_pic.JPG').save()
        mi4 = MediaItem(owner_id=self.user3,
                        media_file='./tests/test_pic.JPG').save()
        mi5 = MediaItem(owner_id=self.user4,
                        media_file='./tests/test_pic.JPG').save()
    
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
        
    def test_create_mediaitem(self):
        self.client.login(username='user1',
                          password='user1')
        
        base_url = reverse('mediaItems')
        
        root = os.path.dirname(__file__)
        
        f = open("%s%s" % (root, '/tests/test_pic.JPG'), 'rb')
        
        response = self.client.post("%s%s" % (base_url, "/user1/@self/@all"),
                                    {'mediaitem': f})
        f.close()
        
        #response 201 created, mediaitem-id
        self.assertContains(response,
                            "mediaitem-id",
                            status_code=201)
        
        
        #send another identical request and make sure the created location is different
        f = open("%s%s" % (root, '/tests/test_pic.JPG'), 'rb')
        
        response2 = self.client.post("%s%s" % (base_url, "/user1/@self/@all"),
                                    {'mediaitem': f})
        f.close()
        
        #response 201 created location
        self.assertContains(response2,
                            "location",
                            status_code=201)
        
        #the first response is different from the second
        self.assertNotEquals(json.loads(response.content)['location'],
                             json.loads(response2.content)['location'],
                             "The file as overriden by two identical requests")
        
    def test_update_mediaitem(self):
        pass
        
    
    def tearDown(self):
        
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()
        self.user4.delete()
        self.group1.delete()
        
