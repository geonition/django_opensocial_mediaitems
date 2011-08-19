from geonition_utils.HttpResponseExtenders import HttpResponseNotImplemented


def media_items(request, *args, **kwargs):
    """
    albums are extended with a @all that can be used to request
    mediaitems when the albums service is not in use
    """
    #print request
    print args
    print kwargs
    return media_items_not_implemented()
    


def media_items_not_implemented():
    return HttpResponseNotImplemented("This part of mediaItems service has not been implemented")