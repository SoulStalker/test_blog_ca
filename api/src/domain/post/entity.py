from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Post:
    title: str
    slug: str
    body: str
    author: str  # тут какой тип ?
    publish: datetime
    status: str
