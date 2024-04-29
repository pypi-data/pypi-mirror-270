from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import ConfigDict, model_validator

from ..base.common import ACROSSBase
from ..base.schema import (
    BaseSchema,
    FileHolder,
    OptionalDateRangeSchema,
    OptionalPositionSchema,
)


class TOOReason(str, Enum):
    """
    Reasons for rejecting TOO observations

    Attributes
    ----------
    saa
        In SAA
    earth_occult
        Earth occulted
    moon_occult
        Moon occulted
    sun_occult
        Sun occulted
    too_old
        Too old
    other
        Other
    none
        None
    """

    saa = "In SAA"
    earth_occult = "Earth occulted"
    moon_occult = "Moon occulted"
    sun_occult = "Sun occulted"
    too_old = "Too old"
    other = "Other"
    none = "None"


class TOOStatus(str, Enum):
    """
    Enumeration class representing the status of a Target of Opportunity (TOO) request.

    Attributes:
    requested
        The TOO request has been submitted.
    rejected
        The TOO request has been rejected.
    declined
        The TOO request has been declined.
    approved
        The TOO request has been approved.
    executed
        The TOO request has been executed.
    other
        The TOO request has a status other than the predefined ones.
    """

    requested = "Requested"
    rejected = "Rejected"
    declined = "Declined"
    approved = "Approved"
    executed = "Executed"
    deleted = "Deleted"
    other = "Other"


class BurstCubeTriggerInfo(BaseSchema, ACROSSBase):
    """
    Metadata schema for the BurstCube Target of Opportunity (TOO) request. Note
    that this schema is not strictly defined, keys are only suggested, and
    additional keys can be added as needed.

    Attributes
    ----------
    trigger_name : Optional[str]
        The name of the trigger.
    trigger_mission : Optional[str]
        The mission that triggered the TOO request.
    trigger_instrument : Optional[str]
        The instrument that triggered the TOO request.
    trigger_id : Optional[str]
        The ID of the trigger.
    trigger_duration : Optional[float]
        The duration of the trigger.
    classification : Optional[str]
        The classification of the trigger.
    justification : Optional[str]
        Textual justification for the TOO request.
    """

    trigger_name: Optional[str] = None
    trigger_mission: Optional[str] = None
    trigger_instrument: Optional[str] = None
    trigger_id: Optional[str] = None
    trigger_duration: Optional[float] = None
    classification: Optional[str] = None
    justification: Optional[str] = None

    model_config = ConfigDict(extra="allow")


class BurstCubeTOODelSchema(BaseSchema):
    """
    Schema for BurstCubeTOO DELETE API call.

    Attributes
    ----------
    id
        The ID of the BurstCubeTOODel object.
    """

    id: int


class BurstCubeTOOPostSchema(OptionalPositionSchema):
    """
    Schema to submit a TOO request for BurstCube.
    """

    trigger_time: datetime
    trigger_info: BurstCubeTriggerInfo
    exposure: int = 200
    offset: int = -50
    healpix_file: Optional[FileHolder] = None

    @model_validator(mode="before")
    @classmethod
    def check_filename(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if data["healpix_file"] is None and data["healpix_filename"] is not None:
                data["healpix_file"] = FileHolder(filename=data["healpix_filename"])
            elif (
                data["healpix_file"] is not None
                and data["healpix_filename"] is not None
            ):
                data["healpix_file"].filename = data["healpix_filename"]
        else:
            if data.healpix_file is None and data.healpix_filename is not None:
                data.healpix_file = FileHolder(filename=data.healpix_filename)
            elif data.healpix_file is not None and data.healpix_filename is not None:
                data.healpix_file.filename = data.healpix_filename

        return data


class BurstCubeTOOGetSchema(BaseSchema):
    """
    Schema for BurstCubeTOO GET request.
    """

    id: int


class BurstCubeTOOPutSchema(BurstCubeTOOPostSchema):
    """
    Schema for BurstCubeTOO PUT request.
    """

    id: int
    trigger_time: datetime
    trigger_info: BurstCubeTriggerInfo
    exposure: int = 200
    offset: int = -50
    status: TOOStatus
    healpix_file: Optional[FileHolder] = None


class BurstCubeTOORequestsGetSchema(OptionalDateRangeSchema):
    """
    Schema for GET requests to retrieve BurstCube Target of Opportunity (TOO) requests.
    """

    duration: Optional[float] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
