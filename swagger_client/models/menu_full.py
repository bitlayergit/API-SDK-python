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


class MenuFull(object):
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
        'id': 'int',
        'name': 'str',
        'allow_extension_dial': 'bool',
        'keypress_wait_time': 'int',
        'greeting': 'MediaSummary',
        'keypress_error': 'MediaSummary',
        'timeout_handler': 'RouteSummary',
        'options': 'list[Option]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'allow_extension_dial': 'allow_extension_dial',
        'keypress_wait_time': 'keypress_wait_time',
        'greeting': 'greeting',
        'keypress_error': 'keypress_error',
        'timeout_handler': 'timeout_handler',
        'options': 'options'
    }

    def __init__(self, id=None, name=None, allow_extension_dial=None, keypress_wait_time=None, greeting=None, keypress_error=None, timeout_handler=None, options=None):
        """
        MenuFull - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._allow_extension_dial = None
        self._keypress_wait_time = None
        self._greeting = None
        self._keypress_error = None
        self._timeout_handler = None
        self._options = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if allow_extension_dial is not None:
          self.allow_extension_dial = allow_extension_dial
        if keypress_wait_time is not None:
          self.keypress_wait_time = keypress_wait_time
        if greeting is not None:
          self.greeting = greeting
        if keypress_error is not None:
          self.keypress_error = keypress_error
        if timeout_handler is not None:
          self.timeout_handler = timeout_handler
        if options is not None:
          self.options = options

    @property
    def id(self):
        """
        Gets the id of this MenuFull.
        Integer Menu ID. Read-only.

        :return: The id of this MenuFull.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MenuFull.
        Integer Menu ID. Read-only.

        :param id: The id of this MenuFull.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this MenuFull.
        Name. Required. Unique.

        :return: The name of this MenuFull.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MenuFull.
        Name. Required. Unique.

        :param name: The name of this MenuFull.
        :type: str
        """

        self._name = name

    @property
    def allow_extension_dial(self):
        """
        Gets the allow_extension_dial of this MenuFull.
        Boolean. Determines whether a caller can enter an extension number to bypass the menu.

        :return: The allow_extension_dial of this MenuFull.
        :rtype: bool
        """
        return self._allow_extension_dial

    @allow_extension_dial.setter
    def allow_extension_dial(self, allow_extension_dial):
        """
        Sets the allow_extension_dial of this MenuFull.
        Boolean. Determines whether a caller can enter an extension number to bypass the menu.

        :param allow_extension_dial: The allow_extension_dial of this MenuFull.
        :type: bool
        """

        self._allow_extension_dial = allow_extension_dial

    @property
    def keypress_wait_time(self):
        """
        Gets the keypress_wait_time of this MenuFull.
        Number of seconds to wait for the caller to choose a menu option. Must be between 1 and 5 seconds.

        :return: The keypress_wait_time of this MenuFull.
        :rtype: int
        """
        return self._keypress_wait_time

    @keypress_wait_time.setter
    def keypress_wait_time(self, keypress_wait_time):
        """
        Sets the keypress_wait_time of this MenuFull.
        Number of seconds to wait for the caller to choose a menu option. Must be between 1 and 5 seconds.

        :param keypress_wait_time: The keypress_wait_time of this MenuFull.
        :type: int
        """

        self._keypress_wait_time = keypress_wait_time

    @property
    def greeting(self):
        """
        Gets the greeting of this MenuFull.
        Greeting that is played when a caller enters a menu. Output is a Media Summary Object. Input must be a Media Lookup Object. Must refer to a media recording that has is_hold_music set to FALSE.

        :return: The greeting of this MenuFull.
        :rtype: MediaSummary
        """
        return self._greeting

    @greeting.setter
    def greeting(self, greeting):
        """
        Sets the greeting of this MenuFull.
        Greeting that is played when a caller enters a menu. Output is a Media Summary Object. Input must be a Media Lookup Object. Must refer to a media recording that has is_hold_music set to FALSE.

        :param greeting: The greeting of this MenuFull.
        :type: MediaSummary
        """

        self._greeting = greeting

    @property
    def keypress_error(self):
        """
        Gets the keypress_error of this MenuFull.
        Message that is played when the caller makes a keypress error. Output is a Media Summary Object. Input must be a Media Lookup Object. Must refer to a media recording that has is_hold_music set to FALSE.

        :return: The keypress_error of this MenuFull.
        :rtype: MediaSummary
        """
        return self._keypress_error

    @keypress_error.setter
    def keypress_error(self, keypress_error):
        """
        Sets the keypress_error of this MenuFull.
        Message that is played when the caller makes a keypress error. Output is a Media Summary Object. Input must be a Media Lookup Object. Must refer to a media recording that has is_hold_music set to FALSE.

        :param keypress_error: The keypress_error of this MenuFull.
        :type: MediaSummary
        """

        self._keypress_error = keypress_error

    @property
    def timeout_handler(self):
        """
        Gets the timeout_handler of this MenuFull.
        Route that will be entered when the caller fails to choose a menu option within the allotted time. Output is a Route Summary Object if the route is named, otherwise the Full Route Object will be shown. Input must be a Route Lookup Object pointing to a named route.

        :return: The timeout_handler of this MenuFull.
        :rtype: RouteSummary
        """
        return self._timeout_handler

    @timeout_handler.setter
    def timeout_handler(self, timeout_handler):
        """
        Sets the timeout_handler of this MenuFull.
        Route that will be entered when the caller fails to choose a menu option within the allotted time. Output is a Route Summary Object if the route is named, otherwise the Full Route Object will be shown. Input must be a Route Lookup Object pointing to a named route.

        :param timeout_handler: The timeout_handler of this MenuFull.
        :type: RouteSummary
        """

        self._timeout_handler = timeout_handler

    @property
    def options(self):
        """
        Gets the options of this MenuFull.
        Array of menu option objects. See below for details.

        :return: The options of this MenuFull.
        :rtype: list[Option]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this MenuFull.
        Array of menu option objects. See below for details.

        :param options: The options of this MenuFull.
        :type: list[Option]
        """

        self._options = options

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
        if not isinstance(other, MenuFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
