from django.urls import path, include
from blog import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='about-page'),
    path('time/', views.method_splitter, {'GET': views.some_page_get, 'POST': views.some_page_post}),
]