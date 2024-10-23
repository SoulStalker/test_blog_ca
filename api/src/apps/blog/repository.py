from django.shortcuts import get_object_or_404

from api.src.domain.post.repository import ICommentRepository, IPostRepository
from api.src.domain.post.dtos import CommentCreateDTO, CommentDTO, PostDTO, PostCreateDTO
from api.src.models.blog import Comment, Post


class PostRepository(IPostRepository):
    model = Post

    def _post_orm_to_dto(self, post: Post) -> PostDTO:
        return PostDTO(
            title=post.title,
            slug=post.slug,
            body=post.body,
            author=post.author,
            publish=post.publish,
            status=post.status,
        )

    def get(self, year, month, day, post):
        return get_object_or_404(
            Post,
            status=Post.Status.PUBLISHED,
            slug=post,
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )

    def create(self, dto: PostCreateDTO) -> PostDTO:
        model = self.model(
            title=dto.title,
            slug=dto.slug,
            body=dto.body,
            author=dto.author,
            status=dto.status,
        )
        model.save()
        return dto

    def delete(self, pk: int) -> None:
        pass

    def get_list(self) -> list[PostDTO]:
        pass


class CommentRepository(ICommentRepository):
    model = Comment

    def create(self, dto: CommentCreateDTO) -> CommentDTO:
        pass

    def delete(self, pk: int) -> None:
        pass

    def get_list(self, post_id: int) -> list[CommentDTO]:
        query = self.model.objects.filter(post_id=post_id)
        comments = []
        for item in query:
            comment = CommentDTO(
                post_id=item.post_id,
                name=item.name,
                body=item.body,
                email=item.email,
            )
            comments.append(comment)

        return comments

    def change_activity(self) -> None:
        pass



