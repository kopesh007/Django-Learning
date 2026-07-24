from django.contrib import admin
from .models import cat,posts,about,user_data



class postsAdmin(admin.ModelAdmin):
    list_display = ('title','content','cato')
    search_fields = ('title','content','posts__cato')
    list_filter = ('cato','data')


class catAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class user_dataAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields = ('name','email','message')

admin.site.register(cat,catAdmin)
admin.site.register(posts,postsAdmin)
admin.site.register(about)
admin.site.register(user_data,user_dataAdmin)

# Register your models here.
