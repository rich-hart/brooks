from django.shortcuts import render
from django.shortcuts import redirect
from podcasts.models import Podcast, Show
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Max

class ShowList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shows.html'

    def get(self, request):
        queryset = []
        for show in Show.objects.all():
            podcast = Podcast.objects.filter(show=show.pk).first()
            if podcast:
                podcast.show = show.name
                queryset.append(podcast)
        return Response({'shows': queryset})

def index(request):
    return redirect('about')

#def home(request):
#    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def podcasts(request):
    latest_shows = {}
    for (key, value) in Podcast.SHOWS:
           latest_shows[key]
    return render(request, 'podcasts.html')

def donate(request):
    return render(request, 'donate.html')


#def contact(request):
#    return render(request, 'contact.html')
