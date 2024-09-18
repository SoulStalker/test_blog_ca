from src.domain.blog.repository import ICommentRepository
from src.models import Comment
from src.domain.blog.dtos import CreateCommentDTO


class CommentRepository(ICommentRepository):
    model = Comment

    def add_comment(self, dto: CreateCommentDTO):
        model = self.model(**dto.dict())
        model.save()

    # def get_list