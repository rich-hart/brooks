from django.shortcuts import render
from django.shortcuts import redirect
from podcasts.models import Podcast, Show
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Max
from django.contrib.auth.models import User
from django.conf import settings
from users.models import Profile, Testimonial 
import re
from django.http import HttpResponse
from django.core.mail import send_mail
class ShowList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shows.html'

    def get(self, request):

        queryset = Show.objects.all()
        for show in queryset:
            show.podcasts = show.podcast_set.all()
            show.videos = show.video_set.all()
        return Response({'shows':queryset})
#        queryset = []
#        for show in Show.objects.all():
#            podcast = Podcast.objects.filter(show=show.pk).first()
#            if podcast:
#                podcast.show = show.name
#                queryset.append(podcast)
#        return Response({'shows': queryset})

def index(request):
    return redirect('profile')

#def home(request):
#    return render(request, 'home.html')

class ProfileInstance(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile.html'

    def get(self, request):
#        import ipdb; ipdb.set_trace()
#        queryset = Profile.objects.filter(owner=settings.WEBSITE_OWNER)
#        return Response({'profile': queryset.pop()})
        queryset = Profile.objects.all()
        return Response({'profiles':[]})

def profile(request):
#    import ipdb; ipdb.set_trace()
    site_owner = User.objects.filter(username=settings.WEBSITE_OWNER)
    profile = Profile.objects.filter(owner=site_owner).first()
    about = re.sub(r'\n+',r'\n',profile.about)
    about = about.strip('\t\n ')
    about_line_list = about.split('\n')   
    data = {'about_line_list':about_line_list,
            'image':profile.image,} 
    return render(request, 'profile.html',data)

def podcasts(request):
    latest_shows = {}
    for (key, value) in Podcast.SHOWS:
           latest_shows[key]
    return render(request, 'podcasts.html')

def donate(request):
    return render(request, 'donate.html')

def message(request):
    user = User.objects.filter(username=settings.WEBSITE_OWNER).first()
    recipient_list = [user.email]
    name = request.POST.get('Name', '') 
    from_email = request.POST.get('Email', '')
    subject = request.POST.get('Subject', '')
    message = request.POST.get('Message', '')
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("Sent")

def example(request):
    user = User.objects.filter(username=settings.WEBSITE_OWNER).first()
    profile = Profile.objects.filter(owner=user).first()
    testimonials = Testimonial.objects.filter(recipient=user)
    for testimonial in testimonials:
        testimonial.owner_profile = Profile.objects.filter(owner=testimonial.owner).first()
        testimonial.image = testimonial.owner_profile.image
        testimonial.profession = testimonial.owner_profile.profession
        testimonial.first_name = testimonial.owner.first_name
        testimonial.last_name = testimonial.owner.last_name 
    shows = Show.objects.all()
    for show in shows:
        show.podcasts = show.podcast_set.all()
        show.videos = show.video_set.all()
    data = {
        'user': user,
        'profile': profile,
        'testimonials': testimonials,
        'shows': shows,
        'donation_link': settings.DONATION_LINK,
    }
    return render(request, 'example.html',data)
 
#def contact(request):
#    return render(request, 'contact.html')
