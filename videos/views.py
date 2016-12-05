from .models import Video
from rest_framework import viewsets
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

# Create your views here.
