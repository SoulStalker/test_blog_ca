from django.core.mail import send_mail

from api.src.config import settings
from api.src.domain.post.dtos import PostDTO, CommentDTO, CommentCreateDTO, PostCreateDTO
from api.src.domain.post.repository import IPostRepository, ICommentRepository


class PostService:
    def __init__(self, repository: IPostRepository):
        self.repository = repository

    def get(self, year, month, day, post):
        self.repository.get()

    def create_post(self, dto: PostCreateDTO):
        self.repository.create(dto)

    def delete_post(self, pk: int):
        self.repository.delete(pk)

    def get_posts_list(self):
        return self.repository.get_list()


class CommentService:
    def __init__(self, repository: ICommentRepository):
        self.repository = repository

    def create(self, dto: CommentCreateDTO):
        self.repository.create(dto)

    def delete(self, pk: int):
        self.repository.delete(pk)

    def get_list(self, post_pk: int):
        return self.repository.get_list(post_pk)

    def change_activity(self):
        self.repository.change_activity()




# def share_post_via_email(request, cd) -> bool:
#     # todo в идеале это должен быть сервис отправки не через джанговский send_mail и причем
#     # функция должа принимать тип способ отправки. не только емайл, тему и пост айди
#     и наверно лучше вынести эту функцию в отдельный модуль Command
#     post = get_object_or_404(Post, pk=post_id, status=Post.Status.PUBLISHED)
#     post_url = request.build_absolute_uri(post.get_absolute_url())
#     subject = f'Post {post.title}'
#     message = f"Read {post.title} at {post_url}\n\ncomments: {cd['comments']}"
#     res = send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])
#     return res
