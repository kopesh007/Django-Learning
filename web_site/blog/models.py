from django.db import models
from django.utils.text import slugify



class cat(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class posts(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=500)
    image=models.ImageField(blank=True,null=True)
    data=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True)
    cato=models.ForeignKey(cat,on_delete=models.CASCADE,default=1)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

class about(models.Model):
    content = models.TextField(max_length=1000)


    def __str__(self):
        return self.content


class user_data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name



# Create your models here.
