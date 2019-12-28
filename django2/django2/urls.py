"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from .views import home_page, contact_page_raw_form, about_page, example, contact_page_django_form
from blog.views import  blog_post_create_view
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    # re_path(r'^pages?/$', about_page),
    path('contact-raw-form', contact_page_raw_form),
    path('example', example),
    re_path(r'^about$', about_page),
    # path('about', about_page),
    path('blog/', include('blog.urls')),
    path('blog-create', blog_post_create_view, name='create-blog'),
    path('contact-django-form', contact_page_django_form),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)