from django.db import models
from django.contrib.auth.models import User

class MediaItem(models.Model):
    """
    A MediaItem as described in opensocial spec 2.0 with
    additional fields:
    owner_id = user id of the person that uploaded the mediaitem
    """
    owner_id = models.ForeignKey(User)
    media_file = models.FileField(upload_to='mediaitems')
    