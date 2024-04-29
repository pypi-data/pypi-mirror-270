from typing import Optional
from ..base.schema import BaseSchema


class ResolveSchema(BaseSchema):
    """
    A schema for resolving astronomical coordinates.
    """

    name: Optional[str] = None
    ra: Optional[float] = None
    dec: Optional[float] = None
    resolver: Optional[str] = None


class ResolveGetSchema(BaseSchema):
    """Schema defines required parameters for a GET"""

    name: str
