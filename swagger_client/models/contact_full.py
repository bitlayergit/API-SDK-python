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


class ContactFull(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, prefix=None, first_name=None, middle_name=None, last_name=None, suffix=None, nickname=None, company=None, phonetic_first_name=None, phonetic_middle_name=None, phonetic_last_name=None, department=None, job_title=None, emails=None, phone_numbers=None, addresses=None, group=None, created_at=None, updated_at=None):
        """
        ContactFull - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'prefix': 'str',
            'first_name': 'str',
            'middle_name': 'str',
            'last_name': 'str',
            'suffix': 'str',
            'nickname': 'str',
            'company': 'str',
            'phonetic_first_name': 'str',
            'phonetic_middle_name': 'str',
            'phonetic_last_name': 'str',
            'department': 'str',
            'job_title': 'str',
            'emails': 'list[Email]',
            'phone_numbers': 'list[PhoneNumberContact]',
            'addresses': 'list[AddressListContacts]',
            'group': 'GroupListContacts',
            'created_at': 'int',
            'updated_at': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'prefix': 'prefix',
            'first_name': 'first_name',
            'middle_name': 'middle_name',
            'last_name': 'last_name',
            'suffix': 'suffix',
            'nickname': 'nickname',
            'company': 'company',
            'phonetic_first_name': 'phonetic_first_name',
            'phonetic_middle_name': 'phonetic_middle_name',
            'phonetic_last_name': 'phonetic_last_name',
            'department': 'department',
            'job_title': 'job_title',
            'emails': 'emails',
            'phone_numbers': 'phone_numbers',
            'addresses': 'addresses',
            'group': 'group',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._prefix = prefix
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._suffix = suffix
        self._nickname = nickname
        self._company = company
        self._phonetic_first_name = phonetic_first_name
        self._phonetic_middle_name = phonetic_middle_name
        self._phonetic_last_name = phonetic_last_name
        self._department = department
        self._job_title = job_title
        self._emails = emails
        self._phone_numbers = phone_numbers
        self._addresses = addresses
        self._group = group
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        """
        Gets the id of this ContactFull.
        Integer ID. Read-only.

        :return: The id of this ContactFull.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContactFull.
        Integer ID. Read-only.

        :param id: The id of this ContactFull.
        :type: int
        """

        self._id = id

    @property
    def prefix(self):
        """
        Gets the prefix of this ContactFull.
        Salutation, such as Mr, Mrs, or Dr

        :return: The prefix of this ContactFull.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this ContactFull.
        Salutation, such as Mr, Mrs, or Dr

        :param prefix: The prefix of this ContactFull.
        :type: str
        """

        self._prefix = prefix

    @property
    def first_name(self):
        """
        Gets the first_name of this ContactFull.
        First name or given name

        :return: The first_name of this ContactFull.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this ContactFull.
        First name or given name

        :param first_name: The first_name of this ContactFull.
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this ContactFull.
        Middle or second name

        :return: The middle_name of this ContactFull.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this ContactFull.
        Middle or second name

        :param middle_name: The middle_name of this ContactFull.
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this ContactFull.
        Last name or surname

        :return: The last_name of this ContactFull.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this ContactFull.
        Last name or surname

        :param last_name: The last_name of this ContactFull.
        :type: str
        """

        self._last_name = last_name

    @property
    def suffix(self):
        """
        Gets the suffix of this ContactFull.
        Suffix, such as \"Jr.\", \"Sr.\", \"II\", or \"III\"

        :return: The suffix of this ContactFull.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this ContactFull.
        Suffix, such as \"Jr.\", \"Sr.\", \"II\", or \"III\"

        :param suffix: The suffix of this ContactFull.
        :type: str
        """

        self._suffix = suffix

    @property
    def nickname(self):
        """
        Gets the nickname of this ContactFull.
        Nickname, or a shortened informal version of the contact's name

        :return: The nickname of this ContactFull.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this ContactFull.
        Nickname, or a shortened informal version of the contact's name

        :param nickname: The nickname of this ContactFull.
        :type: str
        """

        self._nickname = nickname

    @property
    def company(self):
        """
        Gets the company of this ContactFull.
        Name of the contact's company

        :return: The company of this ContactFull.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this ContactFull.
        Name of the contact's company

        :param company: The company of this ContactFull.
        :type: str
        """

        self._company = company

    @property
    def phonetic_first_name(self):
        """
        Gets the phonetic_first_name of this ContactFull.
        Phonetic first name. Useful for remembering how to pronounce the contact's name.

        :return: The phonetic_first_name of this ContactFull.
        :rtype: str
        """
        return self._phonetic_first_name

    @phonetic_first_name.setter
    def phonetic_first_name(self, phonetic_first_name):
        """
        Sets the phonetic_first_name of this ContactFull.
        Phonetic first name. Useful for remembering how to pronounce the contact's name.

        :param phonetic_first_name: The phonetic_first_name of this ContactFull.
        :type: str
        """

        self._phonetic_first_name = phonetic_first_name

    @property
    def phonetic_middle_name(self):
        """
        Gets the phonetic_middle_name of this ContactFull.
        Phonetic middle name. Useful for remembering how to pronounce the contact's name.

        :return: The phonetic_middle_name of this ContactFull.
        :rtype: str
        """
        return self._phonetic_middle_name

    @phonetic_middle_name.setter
    def phonetic_middle_name(self, phonetic_middle_name):
        """
        Sets the phonetic_middle_name of this ContactFull.
        Phonetic middle name. Useful for remembering how to pronounce the contact's name.

        :param phonetic_middle_name: The phonetic_middle_name of this ContactFull.
        :type: str
        """

        self._phonetic_middle_name = phonetic_middle_name

    @property
    def phonetic_last_name(self):
        """
        Gets the phonetic_last_name of this ContactFull.
        Phonetic last name. Useful for remembering how to pronounce the contact's name.

        :return: The phonetic_last_name of this ContactFull.
        :rtype: str
        """
        return self._phonetic_last_name

    @phonetic_last_name.setter
    def phonetic_last_name(self, phonetic_last_name):
        """
        Sets the phonetic_last_name of this ContactFull.
        Phonetic last name. Useful for remembering how to pronounce the contact's name.

        :param phonetic_last_name: The phonetic_last_name of this ContactFull.
        :type: str
        """

        self._phonetic_last_name = phonetic_last_name

    @property
    def department(self):
        """
        Gets the department of this ContactFull.
        Name of the contact's department

        :return: The department of this ContactFull.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """
        Sets the department of this ContactFull.
        Name of the contact's department

        :param department: The department of this ContactFull.
        :type: str
        """

        self._department = department

    @property
    def job_title(self):
        """
        Gets the job_title of this ContactFull.
        Contact's job title

        :return: The job_title of this ContactFull.
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """
        Sets the job_title of this ContactFull.
        Contact's job title

        :param job_title: The job_title of this ContactFull.
        :type: str
        """

        self._job_title = job_title

    @property
    def emails(self):
        """
        Gets the emails of this ContactFull.
        Array of Contact Email Objects. See below for details.

        :return: The emails of this ContactFull.
        :rtype: list[Email]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this ContactFull.
        Array of Contact Email Objects. See below for details.

        :param emails: The emails of this ContactFull.
        :type: list[Email]
        """

        self._emails = emails

    @property
    def phone_numbers(self):
        """
        Gets the phone_numbers of this ContactFull.
        Array of Contact Phone Number Objects. See below for details.

        :return: The phone_numbers of this ContactFull.
        :rtype: list[PhoneNumberContact]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """
        Sets the phone_numbers of this ContactFull.
        Array of Contact Phone Number Objects. See below for details.

        :param phone_numbers: The phone_numbers of this ContactFull.
        :type: list[PhoneNumberContact]
        """

        self._phone_numbers = phone_numbers

    @property
    def addresses(self):
        """
        Gets the addresses of this ContactFull.
        Array of Contact Address Objects. See below for details.

        :return: The addresses of this ContactFull.
        :rtype: list[AddressListContacts]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this ContactFull.
        Array of Contact Address Objects. See below for details.

        :param addresses: The addresses of this ContactFull.
        :type: list[AddressListContacts]
        """

        self._addresses = addresses

    @property
    def group(self):
        """
        Gets the group of this ContactFull.

        :return: The group of this ContactFull.
        :rtype: GroupListContacts
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this ContactFull.

        :param group: The group of this ContactFull.
        :type: GroupListContacts
        """

        self._group = group

    @property
    def created_at(self):
        """
        Gets the created_at of this ContactFull.
        Integer UNIX timestamp when the contact was created. Read-only.

        :return: The created_at of this ContactFull.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ContactFull.
        Integer UNIX timestamp when the contact was created. Read-only.

        :param created_at: The created_at of this ContactFull.
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ContactFull.
        Integer UNIX timestamp when the contact was created. Read-only.

        :return: The updated_at of this ContactFull.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ContactFull.
        Integer UNIX timestamp when the contact was created. Read-only.

        :param updated_at: The updated_at of this ContactFull.
        :type: int
        """

        self._updated_at = updated_at

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
        if not isinstance(other, ContactFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other