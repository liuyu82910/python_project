from django.conf import settings
from django.db import models
from django.utils import timezone

class BlogPostManager(models.Manager):
    def published(self):
        now = timezone.now()
        return self.get_queryset().filter(publish_date__lte=now) # a better way to filter published blogs, <today

# Create your models here.
User =settings.AUTH_USER_MODEL #whenever need user for a foreign key import from auth user model
#anything else use 'django.contrib.auth.models.User'

class BlogPost(models.Model): #blogpost_set(lowercase) -> queryset
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated','-created'] #most recent date first put a negative sign
        # verbose_name_plural = "Bloggs" # this is to set the plural form of a model, default is add s at the end

    def __str__(self):
        return f'{self.id} - {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.slug}'

    def get_update_url(self):
        return f'/blog/update/{self.slug}'

    def get_delete_url(self):
        return f'/blog/delete/{self.slug}'

    def get_list_url(self):
        return '/blog'


