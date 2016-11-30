from .models import Show
from rest_framework import viewsets
from .serializers import ShowSerializer


class ShowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

