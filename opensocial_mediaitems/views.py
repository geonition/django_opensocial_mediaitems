from geonition_utils.HttpResponseExtenders import HttpResponseNotImplemented
from geonition_utils.HttpResponseExtenders import HttpResponseCreated
from geonition_utils.HttpResponseExtenders import HttpResponseUnauthorized
from django.core.urlresolvers import reverse
from models import MediaItem

import json

def media_items(request, *args, **kwargs):
    """
    albums are extended with a @all that can be used to request
    mediaitems when the albums service is not in use
    """
    
    if request.method == 'POST':
        
        if request.user.is_authenticated():
            
            mediaitem = MediaItem(owner_id = request.user,
                                media_file = request.FILES.get('mediaitem'))
            mediaitem.save()
            
            return HttpResponseCreated(json.dumps({"msg": "The file was uploaded and saved",
                                                    "mediaitem-id": mediaitem.id,
                                                    "location": "%s/%s/@self/@all/%s" % (reverse('mediaItems'),
                                                                                                    request.user,
                                                                                                    mediaitem.id)}))
        else:
            return HttpResponseUnauthorized("To save files you have to sign in first")
        
    return media_items_not_implemented()
    


def media_items_not_implemented():
    return HttpResponseNotImplemented("This part of mediaItems service has not been implemented")