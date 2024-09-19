from django.urls import path
from .views import PostListView, post_detail, post_share, post_comment

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('share/<int:post_id>', post_share, name='post_share'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
]