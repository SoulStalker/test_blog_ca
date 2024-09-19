from dataclasses import dataclass
from datetime import datetime


@dataclass
class PostDTO:
    title: str
    slug: str
    body: str
    author: str  # тут какой тип ?
    publish: datetime
    status: str


@dataclass
class PostCreateDTO:
    title: str
    slug: str
    body: str
    author: str  # тут какой тип ?
    publish: datetime
    status: str


@dataclass
class CommentCreateDTO:
    post: PostDTO
    name: str
    email: str
    body: str
    active: bool = True


@dataclass
class CommentDTO:
    post_id: int  # может int post_id?
    name: str
    email: str
    body: str
    active: bool
