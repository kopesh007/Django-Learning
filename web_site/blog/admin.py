from django.contrib import admin
from .models import cat,posts,about



class postsAdmin(admin.ModelAdmin):
    list_display = ('title','content','cato')
    search_fields = ('title','content','posts__cato')
    list_filter = ('cato','data')

admin.site.register(cat)
admin.site.register(posts,postsAdmin)
admin.site.register(about)

# Register your models here.
