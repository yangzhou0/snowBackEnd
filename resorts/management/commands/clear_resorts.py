from django.core.management.base import BaseCommand
from resorts.models import Resort
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        print("completed")

def clear_data():
  Resort.objects.all().delete()


