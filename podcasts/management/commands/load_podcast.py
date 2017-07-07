from django.core.management.base import BaseCommand
from django.conf import settings
import requests
from pyPodcastParser.Podcast import Podcast as PodcastReader
import yaml
import os
class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(settings.PODCAST_RSS_FEED_URL)
        data = PodcastReader(response.content)
        if data.items:
            episode = data.items.pop(0)
            podcast = {
                'podcast': str(data.title),
                'title': str(episode.title),
                'description': str(episode.description),
                'link': str(episode.link or episode.enclosure_url),                             'pubDate': episode.date_time.strftime('%B %w, %Y'),
            }
        episode_path = os.path.join(settings.BASE_DIR, 'episode.yaml')
        with open(episode_path, 'w') as outfile:
            yaml.dump(podcast, outfile)             
