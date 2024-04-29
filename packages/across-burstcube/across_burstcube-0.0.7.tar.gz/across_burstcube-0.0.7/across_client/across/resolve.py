from ..base.common import ACROSSEndPoint
from .schema import ResolveGetSchema, ResolveSchema


class Resolve(ACROSSEndPoint, ResolveSchema):
    """
    Represents a resolver for resolving celestial object coordinates.

    Attributes
    ----------
    name : Optional[str]
        The name of the celestial object.
    ra : Optional[float]
        The right ascension of the celestial object.
    dec : Optional[float]
        The declination of the celestial object.
    resolver : Optional[str]
        The resolver used for resolving the coordinates.
    """

    _mission = "ACROSS"
    _api_name = "Resolve"
    _get_schema = ResolveGetSchema


def resolve(name: str) -> Resolve:
    """Resolve a target name to coordinates

    Parameters
    ----------
    name : str
        Target name that can be resolved by the Resolve class

    Returns
    -------
    Resolve
        A Resolve object with the coordinates of the target
    """
    r = Resolve(name=name)
    r.get()
    return r
