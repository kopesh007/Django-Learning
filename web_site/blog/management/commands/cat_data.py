from django.core.management.base import BaseCommand
from blog.models import cat

class Command(BaseCommand):


    
    def handle(self,*args,**kwargs):
        c=["Sports","Elecrtonics","Mechanical","Artificial Inteligents","Hardwares","Softwares"]

        for i in c:
            cat.objects.create(name=i)

        self.stdout.write(self.style.SUCCESS("Cat Uploaded"))