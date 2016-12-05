from .models import Podcast
from rest_framework import viewsets
from .serializers import PodcastSerializer
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import generics
from django.template.response import TemplateResponse

class PodcastViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Podcast.objects.all().order_by('-air_date')
    serializer_class = PodcastSerializer


class PodcastHighlight(generics.GenericAPIView):
    queryset = Podcast.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        podcast = self.get_object()
        #data =  {'first_name': 'John', 'last_name': 'Doe'}
        data = {
            'show': podcast.show.name,
            'title': podcast.title,
            'air_date': podcast.air_date,
            'host': podcast.host, 
        }
        return TemplateResponse(request, 'podcast.html', data)
