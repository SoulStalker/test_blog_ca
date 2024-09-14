from django.contrib import admin
from src.models.blog import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'publish')
    list_filter = ('status', 'author', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    raw_id_fields = ('author',)
    ordering = ['status', '-publish']


