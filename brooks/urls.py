"""brooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from users.views import UserViewSet
from groups.views import GroupViewSet
from brooks import views
from podcasts.views import PodcastViewSet, PodcastHighlight
from shows.views import ShowViewSet
from videos.views import VideoViewSet

router = routers.DefaultRouter()
router.register(r'podcasts', PodcastViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'shows', ShowViewSet)
router.register(r'videos', VideoViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/podcasts/(?P<pk>[0-9]+)/highlight/$', PodcastHighlight.as_view(),name='podcast-highlight'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.index, name='index'),
#    url(r'^home', views.home, name='home'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^shows', views.ShowList.as_view(), name='shows'),
    url(r'^donate', views.donate, name= 'donate'),
#    url(r'^contact', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, 
        document_root=settings.STATIC_ROOT,
    )

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT,
    )

