from pydantic import BaseModel
from typing import List,Optional


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None


Comment.model_rebuild()

comment = Comment(
    id=1,
    content="Pubg Khele ga",
    replies=[
        Comment(id=2, content="Haa bhai. khelenge"),
        Comment(id=3, content="To aaja fir", replies=[
            Comment(id=4, content="Battery down hai."
                    )])

    ]
)
print(comment)
