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


class ListPhoneNumbers(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, filters=None, sort=None, total=None, offset=None, limit=None, items=None):
        """
        ListPhoneNumbers - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'filters': 'FilterIdNamePhoneNumberArray',
            'sort': 'SortIdNamePhoneNumber',
            'total': 'int',
            'offset': 'int',
            'limit': 'int',
            'items': 'list[PhoneNumberFull]'
        }

        self.attribute_map = {
            'filters': 'filters',
            'sort': 'sort',
            'total': 'total',
            'offset': 'offset',
            'limit': 'limit',
            'items': 'items'
        }

        self._filters = filters
        self._sort = sort
        self._total = total
        self._offset = offset
        self._limit = limit
        self._items = items

    @property
    def filters(self):
        """
        Gets the filters of this ListPhoneNumbers.

        :return: The filters of this ListPhoneNumbers.
        :rtype: FilterIdNamePhoneNumberArray
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this ListPhoneNumbers.

        :param filters: The filters of this ListPhoneNumbers.
        :type: FilterIdNamePhoneNumberArray
        """

        self._filters = filters

    @property
    def sort(self):
        """
        Gets the sort of this ListPhoneNumbers.

        :return: The sort of this ListPhoneNumbers.
        :rtype: SortIdNamePhoneNumber
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this ListPhoneNumbers.

        :param sort: The sort of this ListPhoneNumbers.
        :type: SortIdNamePhoneNumber
        """

        self._sort = sort

    @property
    def total(self):
        """
        Gets the total of this ListPhoneNumbers.

        :return: The total of this ListPhoneNumbers.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this ListPhoneNumbers.

        :param total: The total of this ListPhoneNumbers.
        :type: int
        """

        self._total = total

    @property
    def offset(self):
        """
        Gets the offset of this ListPhoneNumbers.

        :return: The offset of this ListPhoneNumbers.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this ListPhoneNumbers.

        :param offset: The offset of this ListPhoneNumbers.
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """
        Gets the limit of this ListPhoneNumbers.

        :return: The limit of this ListPhoneNumbers.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this ListPhoneNumbers.

        :param limit: The limit of this ListPhoneNumbers.
        :type: int
        """

        self._limit = limit

    @property
    def items(self):
        """
        Gets the items of this ListPhoneNumbers.
        Array of Contact Phone Number Objects. See below for details.

        :return: The items of this ListPhoneNumbers.
        :rtype: list[PhoneNumberFull]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ListPhoneNumbers.
        Array of Contact Phone Number Objects. See below for details.

        :param items: The items of this ListPhoneNumbers.
        :type: list[PhoneNumberFull]
        """

        self._items = items

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
        if not isinstance(other, ListPhoneNumbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
