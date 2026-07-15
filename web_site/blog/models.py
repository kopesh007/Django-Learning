from django.db import models


class posts(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=500)
    image=models.ImageField(blank=True,null=True)
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
