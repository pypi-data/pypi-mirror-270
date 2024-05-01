from pydantic import BaseModel, field_validator, computed_field
from typing import List, Optional


class Page(BaseModel):
    """
    Attributes:
        pageNum: 页码.
        pageSize: 每页数量.
    """
    pageNum: int = 1
    pageSize: Optional[int] = 100
    totalCount: Optional[int] = 1
    totalPage: Optional[int] = 1