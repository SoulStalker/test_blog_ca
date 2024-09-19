from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    body = models.TextField(verbose_name='Body')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Publish')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='Status')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'], name='publish_idx')]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail",
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             verbose_name='Post',
                             related_name='comments')
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(max_length=255, verbose_name='Email')
    body = models.TextField(verbose_name='Body')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    active = models.BooleanField(default=True, verbose_name='Active')

    objects = models.Manager()

    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created']
        indexes = [models.Index(fields=['created'], name='created_at_idx')]

    def __str__(self):
        return f"{self.name} on {self.post}"
