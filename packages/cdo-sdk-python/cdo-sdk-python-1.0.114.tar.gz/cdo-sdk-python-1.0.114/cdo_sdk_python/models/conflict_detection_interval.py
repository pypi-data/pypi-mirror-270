# coding: utf-8

"""
    CDO API

    Use the documentation to explore the endpoints CDO has to offer

    The version of the OpenAPI document: 0.1.0
    Contact: cdo.tac@cisco.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ConflictDetectionInterval(str, Enum):
    """
    Specifies the default interval at which CDO checks for changes made out-of-band on the devices on the tenant.
    """

    """
    allowed enum values
    """
    EVERY_10_MINUTES = 'EVERY_10_MINUTES'
    EVERY_HOUR = 'EVERY_HOUR'
    EVERY_6_HOURS = 'EVERY_6_HOURS'
    EVERY_24_HOURS = 'EVERY_24_HOURS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConflictDetectionInterval from a JSON string"""
        return cls(json.loads(json_str))


