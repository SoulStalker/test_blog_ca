from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from src.models.blog import Post, Comment

from src.apps.blog.forms import EmailPostForm
from src.config import settings

from src.apps.blog.forms import CommentForm
from src.domain.post.service import CommentService

from api.src.apps.blog.repository import CommentRepository
from api.src.domain.post.dtos import CommentCreateDTO


# from src.domain.post.service import share_post_via_email


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                  {'post': post, 'comments': comments, 'form': form})


def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"Somebody recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\ncomments: {cd['comments']}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])
            sent = share_post_via_email(request, form.cleaned_data['cd'])

    else:
        form = EmailPostForm()
    return render(request,
                  'blog/post/share.html',
                  {'post': post, 'form': form, 'sent': sent})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(request.POST)
    service = CommentService(CommentRepository())
    if form.is_valid():
        service.create_comment(CommentCreateDTO(
            post=post_id,  # или получаем PostDTO ?
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            body=form.cleaned_data['body'],
        ))

        # comment = form.save(commit=False)
        # comment.post = post
        # comment.save()
        # вот тут мы должны не сохранять форму в базу а отправлять в репозиторий

    return render(request,
                  'blog/post/comment.html',
                  {'post': post, 'form': form, 'comment': comment})
