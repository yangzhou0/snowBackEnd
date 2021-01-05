from django.core.management.base import BaseCommand
from resorts.models import Resort
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_resorts()
        # clear_data()
        print("completed")

def seed_resorts():
    json_data = open('./resorts/data/resorts.json')
    resorts_data = json.load(json_data)['resorts']
    for resort in resorts_data:
        resort = Resort(
            name = resort['name'],
            description = resort['description'],
            latitude = resort['coordinates'][0],
            longitude = resort['coordinates'][1],
            website = resort['website'],
            likes = 0
        )
        resort.save()

def clear_data():
  Resort.objects.all().delete()


