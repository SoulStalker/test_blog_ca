from pprint import pprint

from django.shortcuts import render
from .custom_view import BaseView

from src.apps.blog.repository import PostRepository

from src.apps.blog.forms import CommentForm
from src.domain.post.service import CommentService, PostService


class PostListView(BaseView):

    def get(self, *args, **kwargs):
        posts = self.post_service.get_posts_list()
        paginated_posts = self.paginate_queryset(posts)

        # pprint(posts)

        context = {
            'posts': paginated_posts,
            'pagination': {
                "current_page": paginated_posts['current_page'],
                "total_pages": paginated_posts['total_pages'],
                "has_next": paginated_posts['has_next'],
                "has_previous": paginated_posts['has_previous'],
                "page_range": paginated_posts['page_range'],
            }
        }
        return render(self.request, 'blog/post/list.html', context)

    # queryset = post_service.get_posts_list()
    # context_object_name = 'posts'
    # paginate_by = 3
    # template_name = 'blog/post/list.html'


# def post_list(request):
#     posts = Post.published.all()
#     return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    service = PostService(PostRepository)

    post = service.get(year=year, month=month, day=day, post=post)

    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                  {'post': post, 'comments': comments, 'form': form})


# def post_share(request, post_id):
#     post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLISHED)
#     sent = False
#
#     if request.method == 'POST':
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = f"Somebody recommends you read {post.title}"
#             message = f"Read {post.title} at {post_url}\n\ncomments: {cd['comments']}"
#             send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])
#             # sent = share_post_via_email(request, form.cleaned_data['cd'])
#             sent = True
#
#     else:
#         form = EmailPostForm()
#     return render(request,
#                   'blog/post/share.html',
#                   {'post': post, 'form': form, 'sent': sent})
#
#
# @require_POST
# def post_comment(request, post_id):
#     post = get_object_or_404(Post,
#                              id=post_id,
#                              status=Post.Status.PUBLISHED)
#     comment = None
#     form = CommentForm(request.POST)
#     service = CommentService(ICommentRepository())
#     if form.is_valid():
#         service.create(CommentCreateDTO(
#             post=post_id,  # или получаем PostDTO ?
#             name=form.cleaned_data['name'],
#             email=form.cleaned_data['email'],
#             body=form.cleaned_data['body'],
#         ))
#
#         # comment = form.save(commit=False)
#         # comment.post = post
#         # comment.save()
#         # вот тут мы должны не сохранять форму в базу а отправлять в репозиторий
#
#     return render(request,
#                   'blog/post/comment.html',
#                   {'post': post, 'form': form, 'comment': comment})
