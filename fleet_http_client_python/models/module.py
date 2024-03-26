# coding: utf-8

"""
    Fleet v2 HTTP API

    HTTP-based API for Fleet Protocol v2 serving for communication between the External Server and the end users.

    The version of the OpenAPI document: 2.2.0
    Contact: jiri.strouhal@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from fleet_http_client_python.models.device_id import DeviceId
from typing import Optional, Set
from typing_extensions import Self

class Module(BaseModel):
    """
    A module containing at least one device (specified by device Id).
    """ # noqa: E501
    module_id: Annotated[int, Field(strict=True, ge=0)] = Field(description="Id (unsigned integer) of the module.")
    device_list: List[DeviceId] = Field(description="List of Ids of devices contained in the module.")
    __properties: ClassVar[List[str]] = ["module_id", "device_list"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Module from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in device_list (list)
        _items = []
        if self.device_list:
            for _item in self.device_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['device_list'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Module from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "module_id": obj.get("module_id"),
            "device_list": [DeviceId.from_dict(_item) for _item in obj["device_list"]] if obj.get("device_list") is not None else None
        })
        return _obj


