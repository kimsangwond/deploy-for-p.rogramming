from django.urls import path
from blog.views import post_new, post_list

app_name = 'blog'


urlpatterns = [
    path('', post_list, name='post_list'),
    path('new/', post_new, name='post_new'),

]
