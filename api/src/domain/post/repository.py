import abc
from src.domain.post.dtos import PostDTO, CommentDTO, CommentCreateDTO, PostCreateDTO


class IPostRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, year, month, day, post) -> PostDTO:
        pass

    @abc.abstractmethod
    def create(self, dto: PostCreateDTO) -> PostDTO:
        pass

    @abc.abstractmethod
    def delete(self, pk: int) -> None:
        pass

    @abc.abstractmethod
    def get_list(self) -> list[PostDTO]:
        pass


class ICommentRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, dto: CommentCreateDTO) -> CommentDTO:
        pass

    @abc.abstractmethod
    def delete(self, pk: int) -> None:
        pass

    @abc.abstractmethod
    def get_list(self, post_id: int) -> list[CommentDTO]:
        pass

    @abc.abstractmethod
    def change_activity(self, pk: int) -> None:
        pass
