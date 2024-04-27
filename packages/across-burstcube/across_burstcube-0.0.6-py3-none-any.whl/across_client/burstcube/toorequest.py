from datetime import datetime
import io
from typing import Any, Optional, Union

from pydantic import model_validator

from ..across.resolve import ACROSSResolveName
from ..base.common import ACROSSBase
from .constants import MISSION
from .schema import (
    BurstCubeTOOGetSchema,
    BurstCubeTOOPostSchema,
    BurstCubeTOOPutSchema,
    BurstCubeTOORequestsGetSchema,
    BurstCubeTOORequestsSchema,
    BurstCubeTOOSchema,
)


class BurstCubeTOO(ACROSSBase, ACROSSResolveName, BurstCubeTOOSchema):
    """
    Class representing a Target of Opportunity (TOO) request.

    Parameters:
    ----------
    api_token: str
        The api_token for login (optional).
    trigger_time : datetime
        The time of the trigger.
    ra : Optional[float]
        The right ascension of the target (optional).
    dec : Optional[float]
        The declination of the target (optional).
    begin : datetime
        The start time of the TOO observation.
    end : datetime
        The end time of the TOO observation.
    exposure : float
        The exposure time for the TOO observation.
    offset : float
        The offset for the TOO observation.
    healpix_filename : Optional[FilePath]
        The healpix filename that represents the object localization for the TOO. This should be a file
        on disk.
    healpix_file : Union[io.BytesIO, io.BufferedReader, None]
        The healpix file handle for the TOO observation, takes a file like object.
    trigger_info : BurstCubeTriggerInfo
        The trigger information for the TOO observation.
    too_info : str
        The information about the TOO observation.
    status : str
        The status of the TOO request.
    id : id
        The ID of the TOO request.


    Attributes:
    ----------
    created_on : datetime
        The time at which the TOO request was made.
    created_by : str
        The user who made the TOO request.
    modified_on : datetime
        The time at which the TOO request was last modified.
    modified_by : str
        The user who modified the TOO request.
    reject_reason : str
        The reason for the TOO request being rejected.
    status : str
        The status of the TOO request.
    too_info : str
        The information about the TOO request.
    id : str
        The ID of the TOO request.
    version : int
        The version of the TOO request.
    """

    # API definitions
    _mission = MISSION
    _api_name = "TOO"
    _schema = BurstCubeTOOSchema
    _put_schema = BurstCubeTOOPutSchema
    _post_schema = BurstCubeTOOPostSchema
    _get_schema = BurstCubeTOOGetSchema
    _del_schema = BurstCubeTOOGetSchema

    # Local parameters
    healpix_file: Union[io.BytesIO, io.BufferedReader, None] = None
    api_token: Optional[str] = None

    # Aliases
    def submit(self):
        self.post()

    def update(self):
        self.put()

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


class TOORequests(ACROSSBase, BurstCubeTOORequestsSchema):
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
    """

    # API definitions
    _mission = MISSION
    _api_name = "TOO"
    _schema = BurstCubeTOORequestsSchema
    _get_schema = BurstCubeTOORequestsGetSchema
    # Local parameters
    trigger_time: Optional[datetime] = None

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, i):
        return self.entries[i]

    def by_id(self, id):
        """
        Get a TOO request by ID.
        """
        for entry in self.entries:
            if entry.id == id:
                return entry

    @model_validator(mode="before")
    @classmethod
    def check_card_number_omitted(cls, data: Any) -> Any:
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
    def get_toos(cls, *args, **kwargs):
        """
        Fetch TOOs based on various criteria.

        Parameters
        ----------
        trigger_time : datetime
            Trigger time of the TOO request.
        begin : datetime
            Beginning trigger time to search.
        end : datetime
            Ending trigger time to search.
        limit : int
            The maximum number of TOOs to return.
        offset : int
            The limit offset for fetching TOOs.

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


# Alias
TOO = BurstCubeTOO
BurstCubeTOORequests = TOORequests
get_too_requests = TOORequests.get_toos
