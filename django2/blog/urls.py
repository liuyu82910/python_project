from django.urls import path, re_path
from.views import (blog_post_detail_page, blog_post_list_view, blog_post_retrieve_view,
                   blog_post_update_view, blog_post_delete_view)
urlpatterns = [
    path('<str:slug>', blog_post_retrieve_view, name='detail-blog'),
    # re_path(r'^blog/(?P<myid>\d+)$', blog_post_detail_page),
    path('', blog_post_list_view, name='list-blog'),
    path('update/<str:slug>', blog_post_update_view, name='update-blog'),
    path('delete/<str:slug>', blog_post_delete_view, name='delete-blog'),
]
