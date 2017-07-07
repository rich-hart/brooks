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
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings
import yaml
import os 
def home(request):
    episode_path = os.path.join(settings.BASE_DIR, 'episode.yaml') 
    try:
        with open(episode_path, 'r') as stream:
            episode = yaml.load(stream)
    except yaml.YAMLError as exc:
        episode = {}
    except FileNotFoundError:
        episode = {}
    finally:
        return render(request, 'home.html', episode)

urlpatterns = [
    url(r'^$', home),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
