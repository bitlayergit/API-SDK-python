# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FilterCallLogs(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'start_time': 'str',
        'created_at': 'str',
        'direction': 'str',
        'called_number': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'start_time': 'start_time',
        'created_at': 'created_at',
        'direction': 'direction',
        'called_number': 'called_number',
        'type': 'type'
    }

    def __init__(self, id=None, start_time=None, created_at=None, direction=None, called_number=None, type=None):
        """
        FilterCallLogs - a model defined in Swagger
        """

        self._id = None
        self._start_time = None
        self._created_at = None
        self._direction = None
        self._called_number = None
        self._type = None

        if id is not None:
          self.id = id
        if start_time is not None:
          self.start_time = start_time
        if created_at is not None:
          self.created_at = created_at
        if direction is not None:
          self.direction = direction
        if called_number is not None:
          self.called_number = called_number
        if type is not None:
          self.type = type

    @property
    def id(self):
        """
        Gets the id of this FilterCallLogs.

        :return: The id of this FilterCallLogs.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FilterCallLogs.

        :param id: The id of this FilterCallLogs.
        :type: str
        """

        self._id = id

    @property
    def start_time(self):
        """
        Gets the start_time of this FilterCallLogs.

        :return: The start_time of this FilterCallLogs.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this FilterCallLogs.

        :param start_time: The start_time of this FilterCallLogs.
        :type: str
        """

        self._start_time = start_time

    @property
    def created_at(self):
        """
        Gets the created_at of this FilterCallLogs.

        :return: The created_at of this FilterCallLogs.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this FilterCallLogs.

        :param created_at: The created_at of this FilterCallLogs.
        :type: str
        """

        self._created_at = created_at

    @property
    def direction(self):
        """
        Gets the direction of this FilterCallLogs.

        :return: The direction of this FilterCallLogs.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this FilterCallLogs.

        :param direction: The direction of this FilterCallLogs.
        :type: str
        """

        self._direction = direction

    @property
    def called_number(self):
        """
        Gets the called_number of this FilterCallLogs.

        :return: The called_number of this FilterCallLogs.
        :rtype: str
        """
        return self._called_number

    @called_number.setter
    def called_number(self, called_number):
        """
        Sets the called_number of this FilterCallLogs.

        :param called_number: The called_number of this FilterCallLogs.
        :type: str
        """

        self._called_number = called_number

    @property
    def type(self):
        """
        Gets the type of this FilterCallLogs.

        :return: The type of this FilterCallLogs.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FilterCallLogs.

        :param type: The type of this FilterCallLogs.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, FilterCallLogs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
