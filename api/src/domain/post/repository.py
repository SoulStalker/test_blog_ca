from api.src.domain.post.dtos import PostDTO, CommentDTO


class IPostRepository:
    def create(self, dto: PostDTO) -> PostDTO:
        pass

    def delete(self, pk: int) -> None:
        pass

    def get_list(self) -> list[PostDTO]:
        pass


class ICommentRepository:
    def create(self, dto: CommentDTO) -> CommentDTO:
        pass

    def delete(self, pk: int) -> None:
        pass

    def get_list(self, post_id: int) -> list[CommentDTO]:
        pass

    def change_activity(self) -> None:
        pass
