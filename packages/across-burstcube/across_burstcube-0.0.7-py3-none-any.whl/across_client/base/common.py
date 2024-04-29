import json
import warnings
from typing import Type

import requests

from ..constants import API_URL
from ..functions import _tablefy
from .schema import BaseSchema, FileHolder


class ACROSSBase:
    """
    Mixin class for ACROSS API classes that provides a representation
    of the API data. Includes support for Jupyter notebooks.
    """

    @property
    def parameters(self) -> dict:
        """
        Return parameters as dict

        Returns
        -------
        dict
            Dictionary of parameters
        """
        if hasattr(self, "model_dump"):
            return {k: v for k, v in self.model_dump().items() if v is not None}
        else:
            return {k: v for k, v in self.__dict__.items() if v is not None}

    @property
    def _table(self) -> tuple:
        """
        Table with head showing results of the API query.

        Returns
        -------
        tuple
            Tuple containing two lists, the header and the table data
        """
        if hasattr(self, "entries") and len(self.entries) > 0:
            header = self.entries[0]._table[0]
            table = [t._table[1][0] for t in self.entries]
        else:
            # Start with arguments
            if hasattr(self, "_get_schema"):
                _parameters = list(self.parameters.keys())
            else:
                _parameters = []
            _parameters += list(self.parameters.keys())

            _parameters
            # Don't include api_token in table
            try:
                _parameters.pop(_parameters.index("api_token"))
            except ValueError:
                pass

            # Removed repeated values
            _parameters = list(set(_parameters))

            header = [par for par in _parameters]
            table = []
            for row in _parameters:
                value = getattr(self, row)
                table.append(value)
            table = [table]
        return header, table

    def _repr_html_(self) -> str:
        """Return a HTML summary of the API data, for e.g. Jupyter.

        Returns
        -------
        str
            HTML summary of data
        """
        header, table = self._table

        if len(table) > 0:
            return _tablefy(table, header)
        else:
            return "No data"

    def __repr__(self) -> str:
        # print a string showing the API call and arguments with their values
        # in a way that can be copied and pasted into a script
        args = ",".join([f"{k}={v}" for k, v in self.parameters.items()])
        return f"{self.__class__.__name__}({args})"


class ACROSSEndPoint(ACROSSBase):
    """
    Base class for ACROSS API Classes including common methods for all API
    endpoint classes.

    Methods
    -------
    api_url(argdict)
        URL for this API call.
    get()
        Perform a 'GET' submission to ACROSS API.
    put()
        Perform a 'PUT' submission to ACROSS API.
    post()
        Perform a 'POST' submission to ACROSS API.
    delete()
        Perform a 'DELETE' submission to ACROSS API.
    validate_get()
        Validate arguments for GET
    validate_put()
        Validate arguments for PUT
    validate_post()
        Validate arguments for POST
    validate_del()
        Validate arguments for DELETE

    """

    # API descriptors type hints
    _get_schema: Type[BaseSchema]
    _put_schema: Type[BaseSchema]
    _post_schema: Type[BaseSchema]
    _del_schema: Type[BaseSchema]

    _mission: str
    _api_name: str

    def __getitem__(self, i):
        return self.entries[i]

    def api_url(self, argdict) -> str:
        """
        URL for this API call.

        Returns
        -------
        str
            URL for API call
        """
        # If arguments has `id` in it, then put this in the path
        if "id" in argdict.keys() and argdict["id"] is not None:
            return f"{API_URL}{self._mission.lower()}/{self._api_name.lower()}/{argdict['id']}"
        return f"{API_URL}{self._mission.lower()}/{self._api_name.lower()}"

    @property
    def headers(self) -> dict:
        # If we have a api_token, then use this to authenticate
        if hasattr(self, "api_token"):
            headers = {"Authorization": f"Bearer {self.api_token}"}
        else:
            headers = {}
        return headers

    def get(self) -> bool:
        """
        Perform a 'GET' submission to ACROSS API. Used for fetching
        information.

        Returns
        -------
        bool
            Was the get successful?

        Raises
        ------
        HTTPError
            Raised if GET doesn't return a 200 response.
        """
        if self.validate_get():
            # Create an array of parameters from the schema
            get_params = {
                key: value
                for key, value in self._get_schema.model_validate(self)
                if key in self._get_schema.model_fields
            }

            # Do the GET request
            req = requests.get(
                self.api_url(get_params),
                params=get_params,
                headers=self.headers,
                timeout=60,
            )

            if req.status_code == 200:
                # Parse, validate and record values from returned API JSON
                assert hasattr(self, "model_validate")
                for k, v in self.model_validate(req.json()):
                    setattr(self, k, v)
                return True
            elif req.status_code == 404:
                """Handle 404 errors gracefully, by issuing a warning"""
                warnings.warn(req.json()["detail"])
            else:
                # Raise an exception if the HTML response was not 200
                req.raise_for_status()
        return False

    def delete(self) -> bool:
        """
        Perform a 'GET' submission to ACROSS API. Used for fetching
        information.

        Returns
        -------
        bool
            Was the get successful?

        Raises
        ------
        HTTPError
            Raised if GET doesn't return a 200 response.
        """
        if self.validate_del():
            # Create an array of parameters from the schema
            del_params = {
                key: value for key, value in self._del_schema.model_validate(self)
            }
            # Do the DELETE request
            req = requests.delete(
                self.api_url(del_params),
                params=del_params,
                headers=self.headers,
                timeout=60,
            )
            if req.status_code == 200:
                # Parse, validate and record values from returned API JSON
                assert hasattr(self, "model_validate")
                for k, v in self.model_validate(req.json()):
                    setattr(self, k, v)
                return True
            else:
                # Raise an exception if the HTML response was not 200
                req.raise_for_status()
        return False

    def put(self) -> bool:
        """
        Perform a 'PUT' submission to ACROSS API. Used for pushing/replacing
        information.

        Returns
        -------
        bool
            Was the get successful?

        Raises
        ------
        HTTPError
            Raised if PUT doesn't return a 201 response.
        """

        if self.validate_put():
            # Extract all POST parameters from the schema
            all_params = self._put_schema.model_validate(self).model_dump(
                mode="json", exclude_none=True
            )

            # Extract query parameters
            put_params = {
                k: all_params[k]
                for k in all_params
                if not isinstance(all_params[k], dict)
            }

            # URL for this API call
            api_url = self.api_url(put_params)
            if "id" in put_params.keys():
                put_params.pop("id")  # Remove id from query parameters

            # Add any files and json data to files
            files = dict()
            for k in all_params:
                if isinstance(getattr(self, k), FileHolder):
                    files[k] = getattr(self, k).upload_file_tuple
                elif isinstance(all_params[k], dict):
                    files[k] = (None, json.dumps(all_params[k]), "application/json")

            # Submit request
            req = requests.put(
                api_url,
                params=put_params,
                headers=self.headers,
                files=files,
                timeout=60,
            )

            if req.status_code == 201:
                # Parse, validate and record values from returned API JSON
                assert hasattr(self, "model_validate")
                for k, v in self.model_validate(req.json()):
                    setattr(self, k, v)
                return True
            elif req.status_code == 304:
                # No changes made
                warnings.warn("Update identical to values on server. No changes made.")
                return False
            else:
                print("ERROR: ", req.status_code, req.json())
                req.raise_for_status()
        return False

    def post(self) -> bool:
        """
        Perform a 'POST' submission to ACROSS API. For submitting new
        information to the API.

        Returns
        -------
        bool
            Was the get successful?

        Raises
        ------
        HTTPError
            Raised if POST doesn't return a 201 response.
        """
        if self.validate_post():
            # Extract all POST parameters from the schema
            all_params = self._post_schema.model_validate(self).model_dump(
                mode="json", exclude_none=True
            )

            # Extract query parameters
            post_params = {
                k: all_params[k]
                for k in all_params
                if not isinstance(all_params[k], dict)
            }

            # Add any files and json data to files
            files = dict()
            for k in all_params:
                if isinstance(getattr(self, k), FileHolder):
                    files[k] = getattr(self, k).upload_file_tuple
                elif isinstance(all_params[k], dict):
                    files[k] = (None, json.dumps(all_params[k]), "application/json")

            # Submit request
            req = requests.post(
                self.api_url(post_params),
                params=post_params,
                headers=self.headers,
                files=files,
                timeout=60,
            )

            if req.status_code == 201:
                # Parse, validate and record values from returned API JSON
                assert hasattr(self, "model_validate")
                for k, v in self.model_validate(req.json()):
                    setattr(self, k, v)
                return True
            elif req.status_code == 200:
                warnings.warn(req.json()["detail"])
                return False
            else:
                # Raise an exception if the HTML response was not 200
                try:
                    req.raise_for_status()
                except requests.HTTPError as exc:
                    print(f"HTTP Exception: {exc}: {req.json()['detail']}.")

        return False

    def validate_get(self) -> bool:
        """Validate arguments for GET

        Returns
        -------
        bool
            Do arguments validate? True | False

        Raises
        ------
        ValidationError
            If arguments don't validate
        """
        if hasattr(self, "_get_schema"):
            self._get_schema.model_validate(self)
        else:
            warnings.warn("GET not allowed for this class.")
            return False
        return True

    def validate_put(self) -> bool:
        """Validate if value to be PUT matches Schema

        Returns
        -------
        bool
            Is it validated? True | False

        Raises
        ------
        ValidationError
            If the value to be PUT doesn't match the Schema


        """
        if hasattr(self, "_put_schema"):
            self._put_schema.model_validate(self.__dict__)
        else:
            warnings.warn("PUT not allowed for this class.")
            return False
        return True

    def validate_post(self) -> bool:
        """Validate if value to be POST matches Schema

        Returns
        -------
        bool
            Is it validated? True | False
        """
        if hasattr(self, "_post_schema"):
            self._post_schema.model_validate(self.__dict__)
            # self._post_schema.model_validate(self)
        else:
            warnings.warn("POST not allowed for this class.")
            return False
        return True

    def validate_del(self) -> bool:
        """Validate if value to be POST matches Schema

        Returns
        -------
        bool
            Is it validated? True | False
        """
        if hasattr(self, "_del_schema"):
            self._del_schema.model_validate(self.__dict__)
        else:
            warnings.warn("DELETE not allowed for this class.")
            return False
        return True
