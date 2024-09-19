from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    title: str
    slug: str
    body: str
    author: str  # тут какой тип ?
    publish: datetime
    status: str


    # тут можно добавить методы типа
    # def add_tag_to_post или еще что-то