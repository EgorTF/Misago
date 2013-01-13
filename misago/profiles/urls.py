from django.conf import settings
from django.conf.urls import patterns, include, url
from django.utils.importlib import import_module

urlpatterns = patterns('misago.profiles.views',
    url(r'^$', 'list', name="users"),
)

# Build extensions URLs
iteration = 0
for extension in settings.PROFILE_EXTENSIONS:
    iteration += 1
    profile_extension = import_module(extension + '.urls')
    try:
        urlpatterns += patterns('',
            (r'^(?P<username>\w+)-(?P<user>\d+)/', include(profile_extension.register_profile_urls(iteration == 1))),
        )
    except AttributeError:
        pass

urlpatterns += patterns('misago.profiles.views',
    url(r'^(?P<rank_slug>(\w|-)+)/$', 'list', name="users"),
)