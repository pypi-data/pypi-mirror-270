from datetime import datetime
from typing import Any, List, Optional

from pydantic import model_validator

from across_client.base.coords import ACROSSSkyCoord

from ..base.common import ACROSSEndPoint
from ..base.schema import BaseSchema, FileHolder
from .schema import (
    BurstCubeTOOGetSchema,
    BurstCubeTOOPostSchema,
    BurstCubeTOOPutSchema,
    BurstCubeTOORequestsGetSchema,
    BurstCubeTriggerInfo,
    TOOReason,
    TOOStatus,
)

MISSION = "BurstCube"


class BurstCubeTOO(ACROSSEndPoint, ACROSSSkyCoord, BaseSchema):
    """
    Class representing a Target of Opportunity (TOO) request.

    Parameters
    ----------
    api_token: str
        The api_token for login (optional).
    trigger_time : Optional[datetime]
        The time at which the BurstCube TOO request was triggered.
    trigger_info : BurstCubeTriggerInfo
        Metadata about the BurstCube TOO request.
    exposure : int
        The exposure time for the BurstCube TOO request.
    offset : int
        The offset from `trigger_time` that indicates when the BurstCube TOO
        request dump time should begin. E.g. if offset is -50, the dump time
        will begin 50 seconds before `trigger_time`.
    healpix_filename : Optional[str]
        The filename of the healpix file that represents the object localization
        for the BurstCube TOO request.
    healpix_file : Union[io.BytesIO, io.BufferedReader, None]
        The healpix file handle for the TOO observation, takes a file like
        object.
    name : str
        The name of the celestial object. If given, the `ra` and `dec` values
        will be set using the `Resolve` API end point.

    Attributes
    ----------
    id : int
        The ID of the TOO request.
    created_on : datetime
        The time at which the TOO request was made.
    created_by : str
        The user who made the TOO request.
    modified_on : datetime
        The time at which the TOO request was last modified.
    modified_by : str
        The user who modified the TOO request.
    reject_reason : TOOReason
        The reason for rejecting the BurstCube TOO request. Default is `none`.
        Options are:
            - saa
            - earth_occult
            - moon_occult
            - sun_occult
            - too_old
            - other
            - none
    status : TOOStatus
        The status of the BurstCube TOO request. Default is `requested`.
        Options are:
            - requested
            - rejected
            - declined
            - approved
            - executed
            - other
    too_info : str
        Additional textual information about the BurstCube TOO request.
    version : int
        The version of the TOO request.
    skycoord : SkyCoord
        An astropy SkyCoord object representing the RA/Dec of the TOO.
    """

    # API definitions
    _mission = MISSION
    _api_name = "TOO"
    _put_schema = BurstCubeTOOPutSchema
    _post_schema = BurstCubeTOOPostSchema
    _get_schema = BurstCubeTOOGetSchema
    _del_schema = BurstCubeTOOGetSchema

    # Schema parameters
    id: Optional[int] = None
    ra: Optional[float] = None
    dec: Optional[float] = None
    error_radius: Optional[float] = None
    created_by: Optional[str] = None
    created_on: Optional[datetime] = None
    modified_by: Optional[str] = None
    modified_on: Optional[datetime] = None
    trigger_time: Optional[datetime] = None
    trigger_info: BurstCubeTriggerInfo = BurstCubeTriggerInfo()
    exposure: int = 200
    offset: int = -50
    reject_reason: TOOReason = TOOReason.none
    status: TOOStatus = TOOStatus.requested
    too_info: str = ""
    healpix_filename: Optional[str] = None
    version: Optional[int] = None

    # Local parameters
    healpix_file: Optional[FileHolder] = None
    api_token: Optional[str] = None

    # Aliases
    def submit(self):
        self.post()

    def update(self):
        self.put()

    @property
    def _table(self):
        if self.trigger_time is None:
            return [], []
        return (
            [
                "TOO ID",
                "Submitted",
                "Submitter",
                "Trigger Time",
                "Mission",
                "Instrument",
                "ID",
                "Status",
                "Reason",
            ],
            [
                [
                    self.id,
                    self.created_on,
                    self.created_by,
                    self.trigger_time,
                    self.trigger_info.trigger_mission,
                    self.trigger_info.trigger_instrument,
                    self.trigger_info.trigger_id,
                    self.status.value,
                    self.reject_reason.value,
                ]
            ],
        )


class TOORequests(ACROSSEndPoint, BurstCubeTOORequestsGetSchema):
    """
    Represents a Targer of Opportunity (TOO) request.

    Parameters
    ----------
    trigger_time : datetime
        Trigger time of the TOO request.
    begin : datetime
        The start time of the observation.
    end : datetime
        The end time of the observation.
    limit : int
        The maximum number of TOOs to return.
    offset : int
        The limit offset for fetching TOOs.

    Attributes
    ----------
    entries : list
        The list of entries for the observation.

    Methods
    -------
    get_toos
        Fetch TOOs based on various criteria.

    """

    # API definitions
    _mission = MISSION
    _api_name = "TOO"
    _get_schema = BurstCubeTOORequestsGetSchema
    # Local parameters
    trigger_time: Optional[datetime] = None

    entries: List[BurstCubeTOO] = []

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, i):
        return self.entries[i]

    def by_id(self, id):
        """
        Return a TOO from the fetched list by the ID number.

        Parameters
        ----------
        id : int
            The ID of the TOO request.

        Returns
        -------
        BurstCubeTOO
            The TOO request.
        """
        for entry in self.entries:
            if entry.id == id:
                return entry

    @model_validator(mode="before")
    @classmethod
    def _trigger_time_validator(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if "trigger_time" in data and data["trigger_time"] is not None:
                data["begin"] = data["trigger_time"]
                data["end"] = data["trigger_time"]
        return data

    @property
    def _table(self):
        return (
            [
                "TOO ID",
                "Submitted",
                "Submitter",
                "Trigger Time",
                "Mission",
                "Instrument",
                "ID",
                "Status",
                "Reason",
            ],
            [
                [
                    entry.id,
                    entry.created_on,
                    entry.created_by,
                    entry.trigger_time,
                    entry.trigger_info.trigger_mission,
                    entry.trigger_info.trigger_instrument,
                    entry.trigger_info.trigger_id,
                    entry.status.value,
                    entry.reject_reason.value,
                ]
                for entry in self.entries
            ],
        )

    @classmethod
    def get_too_requests(cls, *args, **kwargs):
        """
        Fetch TOOs based on various criteria. Passing no arguments will fetch
        all. TOOs are returned in reverse order of receipt time.

        Parameters
        ----------
        trigger_time : datetime
            Trigger time of the TOO request to search for. Only returns trigger
            with this exact trigger time.
        begin : datetime
            Beginning trigger time to search.
        end : datetime
            Ending trigger time to search.
        limit : int
            The maximum number of TOOs to return.
        offset : int
            The limit offset for fetching TOOs. Provides pagination support.
            I.e. if limit is 10 and offset is 10, then the second page of 10
            TOOs will be returned.

        Returns
        ----------
        TOORequests
            The list of entries for the observation.
        """
        too_requests = cls(*args, **kwargs)
        too_requests.get()
        return too_requests


def get_too_by_id(id: int) -> BurstCubeTOO:
    """
    Get a TOO request by ID.

    Parameters
    ----------
    id : int
        The ID of the TOO request.
    api_token : str
        The API token for the user.

    Returns
    -------
    BurstCubeTOO
        The TOO request.
    """
    too = BurstCubeTOO(id=id)
    too.get()
    return too


def get_too_by_trigger_time(trigger_time: datetime) -> Optional[BurstCubeTOO]:
    """
    Get a TOO request by timestamp.

    Parameters
    ----------
    timestamp : str
        The timestamp of the TOO request.
    api_token : str
        The API token for the user.

    Returns
    -------
    BurstCubeTOO
        The TOO request.
    """
    too = TOORequests(trigger_time=trigger_time)
    too.get()
    if len(too) > 0:
        return too[0]
    return None


def delete_too_by_id(id: Optional[int]) -> bool:
    """
    Delete a TOO request by ID.

    Parameters
    ----------
    id : int
        The ID of the TOO request.
    api_token : str
        The API token for the user.

    Returns
    -------
    bool
        True if the request was deleted.
    """
    if id is None:
        return False
    too = BurstCubeTOO(id=id)
    return too.delete()


def delete_too_by_trigger_time(trigger_time: datetime) -> bool:
    """
    Delete a TOO request by timestamp.

    Parameters
    ----------
    timestamp : str
        The timestamp of the TOO request.
    api_token : str
        The API token for the user.

    Returns
    -------
    bool
        True if the request was deleted.
    """
    too = TOORequests(trigger_time=trigger_time)
    too.get()
    # There will only be 0 or 1 entries
    for entry in too.entries:
        return delete_too_by_id(entry.id)
    return False


# Alias
TOO = BurstCubeTOO
BurstCubeTOORequests = TOORequests
get_too_requests = TOORequests.get_too_requests
