from django.apps import AppConfig

from django.db.models.signals import post_migrate



class BlogConfig(AppConfig):
    name = 'blog'
    def ready(self):
        from blog.signals import create_g_p
        post_migrate.connect(create_g_p)
