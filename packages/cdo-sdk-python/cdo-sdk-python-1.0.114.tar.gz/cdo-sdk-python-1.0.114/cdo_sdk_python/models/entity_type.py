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


class EntityType(str, Enum):
    """
    The type of the device.
    """

    """
    allowed enum values
    """
    ASA = 'ASA'
    CDFMC_MANAGED_FTD = 'CDFMC_MANAGED_FTD'
    ONPREM_FMC_MANAGED_FTD = 'ONPREM_FMC_MANAGED_FTD'
    ONPREM_FMC_MANAGED_FIREPOWER = 'ONPREM_FMC_MANAGED_FIREPOWER'
    ONPREM_FMC_NGIPS = 'ONPREM_FMC_NGIPS'
    FDM_MANAGED_FTD = 'FDM_MANAGED_FTD'
    IOS = 'IOS'
    SSH_DEVICE = 'SSH_DEVICE'
    GENERIC_DEVICE = 'GENERIC_DEVICE'
    MERAKI_MX = 'MERAKI_MX'
    CLOUD_DNG = 'CLOUD_DNG'
    SFCN = 'SFCN'
    SFCN_DNG = 'SFCN_DNG'
    SFCN_STS = 'SFCN_STS'
    ONPREM_FMC = 'ONPREM_FMC'
    CDFMC = 'CDFMC'
    AWS_VPC = 'AWS_VPC'
    AZURE_VNET = 'AZURE_VNET'
    DUO_ADMIN_PANEL = 'DUO_ADMIN_PANEL'
    UMBRELLA_ORGANIZATION = 'UMBRELLA_ORGANIZATION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EntityType from a JSON string"""
        return cls(json.loads(json_str))


