from .models import Video
from rest_framework import viewsets
from .serializers import VideoSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import renderers
from django.template.response import TemplateResponse


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

# Create your views here.
class VideoHighlight(generics.GenericAPIView):
    queryset = Video.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        #return HttpResponse()
        video = self.get_object()
        #data =  {'first_name': 'John', 'last_name': 'Doe'}
        data = {
            'show': video.show.name,
            'title': video.title,
            'air_date': video.air_date,
            'host': video.host, 
        }

        return TemplateResponse(request,'video.html',data)
