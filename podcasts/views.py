from .models import Podcast
from rest_framework import viewsets
from .serializers import PodcastSerializer


class PodcastViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Podcast.objects.all().order_by('-air_date')
    serializer_class = PodcastSerializer

