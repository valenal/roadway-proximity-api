# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RoadwayData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, roadtype: str=None, latitude: float=None, longitude: float=None, distance: float=None, aadt: float=None, speed: float=None, through_lanes: float=None):  # noqa: E501
        """RoadwayData - a model defined in Swagger

        :param name: The name of this RoadwayData.  # noqa: E501
        :type name: str
        :param roadtype: The roadtype of this RoadwayData.  # noqa: E501
        :type roadtype: str
        :param latitude: The latitude of this RoadwayData.  # noqa: E501
        :type latitude: float
        :param longitude: The longitude of this RoadwayData.  # noqa: E501
        :type longitude: float
        :param distance: The distance of this RoadwayData.  # noqa: E501
        :type distance: float
        :param aadt: The aadt of this RoadwayData.  # noqa: E501
        :type aadt: float
        :param speed: The speed of this RoadwayData.  # noqa: E501
        :type speed: float
        :param through_lanes: The through_lanes of this RoadwayData.  # noqa: E501
        :type through_lanes: float
        """
        self.swagger_types = {
            'name': str,
            'roadtype': str,
            'latitude': float,
            'longitude': float,
            'distance': float,
            'aadt': float,
            'speed': float,
            'through_lanes': float
        }

        self.attribute_map = {
            'name': 'name',
            'roadtype': 'roadtype',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'distance': 'distance',
            'aadt': 'aadt',
            'speed': 'speed',
            'through_lanes': 'through_lanes'
        }

        self._name = name
        self._roadtype = roadtype
        self._latitude = latitude
        self._longitude = longitude
        self._distance = distance
        self._aadt = aadt
        self._speed = speed
        self._through_lanes = through_lanes

    @classmethod
    def from_dict(cls, dikt) -> 'RoadwayData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RoadwayData of this RoadwayData.  # noqa: E501
        :rtype: RoadwayData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this RoadwayData.


        :return: The name of this RoadwayData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this RoadwayData.


        :param name: The name of this RoadwayData.
        :type name: str
        """

        self._name = name

    @property
    def roadtype(self) -> str:
        """Gets the roadtype of this RoadwayData.


        :return: The roadtype of this RoadwayData.
        :rtype: str
        """
        return self._roadtype

    @roadtype.setter
    def roadtype(self, roadtype: str):
        """Sets the roadtype of this RoadwayData.


        :param roadtype: The roadtype of this RoadwayData.
        :type roadtype: str
        """
        if roadtype is None:
            raise ValueError("Invalid value for `roadtype`, must not be `None`")  # noqa: E501

        self._roadtype = roadtype

    @property
    def latitude(self) -> float:
        """Gets the latitude of this RoadwayData.


        :return: The latitude of this RoadwayData.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this RoadwayData.


        :param latitude: The latitude of this RoadwayData.
        :type latitude: float
        """
        if latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Gets the longitude of this RoadwayData.


        :return: The longitude of this RoadwayData.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this RoadwayData.


        :param longitude: The longitude of this RoadwayData.
        :type longitude: float
        """
        if longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def distance(self) -> float:
        """Gets the distance of this RoadwayData.


        :return: The distance of this RoadwayData.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance: float):
        """Sets the distance of this RoadwayData.


        :param distance: The distance of this RoadwayData.
        :type distance: float
        """
        if distance is None:
            raise ValueError("Invalid value for `distance`, must not be `None`")  # noqa: E501

        self._distance = distance

    @property
    def aadt(self) -> float:
        """Gets the aadt of this RoadwayData.


        :return: The aadt of this RoadwayData.
        :rtype: float
        """
        return self._aadt

    @aadt.setter
    def aadt(self, aadt: float):
        """Sets the aadt of this RoadwayData.


        :param aadt: The aadt of this RoadwayData.
        :type aadt: float
        """
        if aadt is None:
            raise ValueError("Invalid value for `aadt`, must not be `None`")  # noqa: E501

        self._aadt = aadt

    @property
    def speed(self) -> float:
        """Gets the speed of this RoadwayData.


        :return: The speed of this RoadwayData.
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed: float):
        """Sets the speed of this RoadwayData.


        :param speed: The speed of this RoadwayData.
        :type speed: float
        """
        if speed is None:
            raise ValueError("Invalid value for `speed`, must not be `None`")  # noqa: E501

        self._speed = speed

    @property
    def through_lanes(self) -> float:
        """Gets the through_lanes of this RoadwayData.


        :return: The through_lanes of this RoadwayData.
        :rtype: float
        """
        return self._through_lanes

    @through_lanes.setter
    def through_lanes(self, through_lanes: float):
        """Sets the through_lanes of this RoadwayData.


        :param through_lanes: The through_lanes of this RoadwayData.
        :type through_lanes: float
        """
        if through_lanes is None:
            raise ValueError("Invalid value for `through_lanes`, must not be `None`")  # noqa: E501

        self._through_lanes = through_lanes
