from api.src.domain.post.dtos import PostDTO, CommentDTO, CommentCreateDTO, PostCreateDTO


class IPostRepository:
    def get(self, year, month, day, post) -> PostDTO:
        pass

    def create(self, dto: PostCreateDTO) -> PostDTO:
        pass

    def delete(self, pk: int) -> None:
        pass

    def get_list(self) -> list[PostDTO]:
        pass


class ICommentRepository:
    def create(self, dto: CommentCreateDTO) -> CommentDTO:
        pass

    def delete(self, pk: int) -> None:
        pass

    def get_list(self, post_id: int) -> list[CommentDTO]:
        pass

    def change_activity(self, pk: int) -> None:
        pass
