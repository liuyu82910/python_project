from django.contrib import admin

# Register your models here.
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    # list_display = ('id', 'title', 'content', 'slug')
    # ordering = ('id',)
    search_fields = ('title', 'content')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.site_header = "Glog is the new blog"
admin.site.site_title = "Admin portal"
admin.site.index_title = "Welcome 2 Glog"