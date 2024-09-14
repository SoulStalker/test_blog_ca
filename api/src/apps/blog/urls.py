from django.urls import path
from src.apps.blog.views import post_list, post_detail

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
]