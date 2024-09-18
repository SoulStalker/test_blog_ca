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
class CommentDTO:
    post: PostDTO
    name: str
    email: str
    body: str
    active: bool
