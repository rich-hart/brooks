from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, TestimonialSerializer
from .models import Testimonial

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    def perform_create(self, serializer):
        # Include the owner attribute directly, rather than from request data.
        instance = serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

