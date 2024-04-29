import io
from datetime import datetime
from pathlib import Path, PosixPath
from typing import Any, Optional, Union
from uuid import uuid4

import requests
from astropy.coordinates import SkyCoord  # type: ignore
from pydantic import (
    AnyUrl,
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_serializer,
    model_validator,
)

from ..functions import _convert_to_dt  # type: ignore
from .coords import coord_convert  # type: ignore


class BaseSchema(BaseModel):
    """Base schema for all other schemas"""

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class OptionalCoordSchema(BaseSchema):
    """
    Schema that defines optional RA/Dec

    Attributes
    ----------
    ra : Optional[float]
        The right ascension in degrees.
    dec : Optional[float]
        The declination in degrees.
    """

    ra: Optional[float] = Field(ge=0, lt=360, default=None)
    dec: Optional[float] = Field(ge=-90, le=90, default=None)

    @model_validator(mode="before")
    @classmethod
    def coord_convert(cls, data: Any) -> Any:
        """Convert the coordinate data to a specific format"""
        if isinstance(data, dict):
            for key in data.keys():
                if key == "ra" or key == "dec":
                    data[key] = coord_convert(data[key])
        elif hasattr(data, "ra") and hasattr(data, "dec"):
            data.ra = coord_convert(data.ra)
            data.dec = coord_convert(data.dec)
        return data

    @model_validator(mode="after")
    @classmethod
    def check_ra_dec(cls, data: Any) -> Any:
        """Check if RA and Dec are both set or both not set"""
        if data.ra is None or data.dec is None:
            assert data.ra == data.dec, "RA/Dec should both be set, or both not set"
        return data

    @property
    def skycoord(self) -> Optional[SkyCoord]:
        """Get the SkyCoord representation of the coordinates"""
        if self.ra is not None and self.dec is not None:
            return SkyCoord(self.ra, self.dec, unit="deg")
        return None


class OptionalPositionSchema(OptionalCoordSchema):
    """
    Schema that defines position with error

    Attributes
    ----------
    error_radius : Optional[float]
        The error radius of the position in degrees.
    """

    error_radius: Optional[float] = None


class OptionalDateRangeSchema(BaseSchema):
    """
    Schema that defines optional date range

    Attributes
    ----------
    begin : datetime
        The start time.
    end : datetime
        The end time.
    """

    begin: Optional[datetime] = None
    end: Optional[datetime] = None

    @model_validator(mode="before")
    @classmethod
    def convert_date(cls, data: Any) -> datetime:
        """Check if the begin and end dates are both set or both not set"""
        if isinstance(data, dict):
            for key in data.keys():
                if key == "begin" or key == "end":
                    data[key] = _convert_to_dt(data[key])
        else:
            data.begin = _convert_to_dt(data.begin)
            data.end = _convert_to_dt(data.end)
        return data

    @model_validator(mode="after")
    @classmethod
    def check_dates(cls, data: Any) -> Any:
        """Check if the begin and end dates are both set or both not set"""
        if data.begin is None or data.end is None:
            assert (
                data.begin == data.end
            ), "Begin/End should both be set, or both not set."
        if data.begin is not None and data.end is not None:
            assert data.begin <= data.end, "End date should not be before begin."

        return data


class FileHolder(BaseSchema):
    """
    Schema to handle file uploads. Takes as input a file-like object, a
    filename or both. If a filename is not provided, one will be generated from
    the file-like object. If a file-like object is not provided, one will be
    generated from the filename. If the filename is a URL, the file will be
    downloaded and stored as a BytesIO file-like object, and the filename will
    be set to the URL.

    If a file-like object is provided, that does not have an associated
    filename, then a UUID4 unique identifier will be generated as the filename.
    For this reason, it is recommended to supply a filename if possible.

    Attributes
    ----------
    filename: Path | AnyUrl
        The name of the file.
    file: Optional[io.IOBase]
        The file-like object to upload.

    Properties
    ----------
    filetype: str
        The MIME type of the file. If the file is gzipped, it will return
        "application/x-gzip". Otherwise, it will return
        "application/octet-stream".
    upload_file_tuple: Tuple[str, io.IOBase, str]
        The tuple representation of the file and its name. Used by requests to
        upload files to the server.
    """

    filename: Union[Path, AnyUrl, None] = None
    file: Optional[io.IOBase] = None

    @field_serializer("filename")
    def serialize_filename(self, filename: Any, _info) -> str:
        """
        Serialize the filename to a string. If the filename is a Path object,
        return the name. Otherwise, return the string representation of the
        filename.
        """
        if isinstance(filename, PosixPath):
            return filename.name
        else:
            return str(filename)

    @field_serializer("file")
    def serialize_file(self, file: Any, _info) -> str:
        """
        Serialize the file-like object to a string. To allow model_dump_json to
        work.
        """
        return str(file)

    @model_validator(mode="before")
    @classmethod
    def set_filename_from_file(cls, data: Any) -> Any:
        """
        Set the filename from the file-like object if it is not provided. If
        the filename is a Path object, open the file and set file to be a
        file-like object. If the filename is a URL, download the file and set
        file to be a file-like object.

        Returns
        -------
        Any
            The data dictionary with the filename and file-like object set.
        """
        # Handle the case where the data is a file-like object.
        if isinstance(data, io.IOBase):
            fh = cls(file=data)
            data = {}
            data["file"] = fh.file
            data["filename"] = fh.filename
        elif isinstance(data, dict):
            # Verify type and filename is set
            if "filename" not in data.keys():
                try:
                    # Extract filename from file-like object if possible
                    data["filename"] = data["file"].name
                except AttributeError:
                    # It's gotta be something
                    data["filename"] = str(uuid4())
            else:
                try:
                    data["filename"] = AnyUrl(data["filename"])
                except ValidationError:
                    data["filename"] = Path(data["filename"])
            # Check if file-like object is present
            if "file" not in data.keys():
                if isinstance(data["filename"], PosixPath):
                    data["file"] = open(data["filename"], "rb")
                elif isinstance(data["filename"], AnyUrl):
                    # Download the binary file and turn into a BytesIO file-like object
                    data["file"] = io.BytesIO(
                        requests.get(str(data["filename"]), stream=True).raw.read()
                    )
        else:
            raise NotImplementedError("Data must be a dictionary.")
        return data

    @property
    def filetype(self):
        """
        Simple file type detection. This is used to determine the MIME type of
        the file. If the file is gzipped, it will return "application/x-gzip".
        Otherwise, it will return "application/octet-stream".

        Returns
        -------
        str
            The MIME type of the file.
        """
        # Check if this is gzipped
        header = self.file.read(2)
        self.file.seek(0)
        if header == b"\x1f\x8b":
            return "application/x-gzip"
        # Else just assume everything else
        return "application/octet-stream"

    @property
    def upload_file_tuple(self):
        """
        Get the tuple representation of the file and its name. This is used to
        upload files to the server. The tuple is in the form of (filename,
        file, filetype). The filename is the name of the file,stripped of path
        information,  or a URL to the file. The file is the file-like object to
        upload. The filetype is the MIME type of the file.

        Returns
        -------
        Tuple[str, io.IOBase, str]
            The tuple representation of the file and its name and MIME type.
        """
        filename = (
            self.filename.name
            if isinstance(self.filename, Path)
            else str(self.filename)
        )
        return (
            filename,
            self.file,
            self.filetype,
        )
