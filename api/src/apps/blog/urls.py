from django.urls import path
from src.apps.blog.views import PostListView, post_detail, post_share

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('share/<int:post_id>', post_share, name='post_share'),
]