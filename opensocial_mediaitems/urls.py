# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('opensocial_mediaitems.views',
                       url(r'^mediaItems$',
                           'media_items',
                           {'user': '@me',
                            'group': '@self'},
                            name="mediaItems"),
                       
                       (r'^mediaItems/(?P<user>@?\w+)$',
                        'media_items',
                        {'group': '@self'}),
                       
                       (r'^mediaItems/(?P<user>@?\w+)/(?P<group>@?\w+)$',
                        'media_items'),
                       
                       (r'^mediaItems/(?P<user>@?\w+)/(?P<group>@?\w+)/(?P<album>@?\w+)$',
                        'media_items'),
                       
                       (r'^mediaItems/(?P<user>@?\w+)/(?P<group>@?\w+)/(?P<album>@?\w+)/(?P<mediaitem>\w+)$',
                        'media_items'),
        )
