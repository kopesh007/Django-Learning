from django.core.management.base import BaseCommand
from blog.models import about

class Command(BaseCommand):

    def handle(self,*args,**kwargs):

        content = "Hi KOPESH and TOSY"

        about.objects.create(content=content)

        self.stdout.write(self.style.SUCCESS("About Page Data Updated !!! "))
