from django.urls.conf import path,re_path,include
from app_01.views import *
from haystack import urls

app_name='app_01'
urlpatterns=[
    re_path(r'^index/(\d?/?)$',get_page,name='blog_page'),
    path(r'posts/',blogs,name='blogs_page'),
    path(r'cgy/<str:category_name>',cgy_view,name='cgy_page'),
    path(r'tag/<str:tag_name>',tag_view,name='tag_page'),
    path(r'post/<str:blog_title>',blog_view,name='blog_content'),
    path(r'search/',SearchHandler(),name='haystack_search'),
]
