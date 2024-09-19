from api.src.domain.post.repository import ICommentRepository
from api.src.models.blog import Comment
from api.src.domain.post.dtos import CommentCreateDTO


class CommentRepository(ICommentRepository):
    model = Comment

    def create(self, dto: CommentCreateDTO):
        model = self.model(**dto.dict())
        model.save()

    # def get_list