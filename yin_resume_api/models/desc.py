from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from yin_resume_api.models.base_model import Model
from yin_resume_api import util


class Desc(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name_id=None, name=None, profile=None, mail=None, phone=None, phone_prefix=None, address=None, desc=None):  # noqa: E501
        """Desc - a model defined in OpenAPI

        :param name_id: The name_id of this Desc.  # noqa: E501
        :type name_id: str
        :param name: The name of this Desc.  # noqa: E501
        :type name: str
        :param profile: The profile of this Desc.  # noqa: E501
        :type profile: str
        :param mail: The mail of this Desc.  # noqa: E501
        :type mail: str
        :param phone: The phone of this Desc.  # noqa: E501
        :type phone: int
        :param phone_prefix: The phone_prefix of this Desc.  # noqa: E501
        :type phone_prefix: int
        :param address: The address of this Desc.  # noqa: E501
        :type address: str
        :param desc: The desc of this Desc.  # noqa: E501
        :type desc: str
        """
        self.openapi_types = {
            'name_id': str,
            'name': str,
            'profile': str,
            'mail': str,
            'phone': int,
            'phone_prefix': int,
            'address': str,
            'desc': str
        }

        self.attribute_map = {
            'name_id': 'name_id',
            'name': 'name',
            'profile': 'profile',
            'mail': 'mail',
            'phone': 'phone',
            'phone_prefix': 'phone-prefix',
            'address': 'address',
            'desc': 'desc'
        }

        self._name_id = name_id
        self._name = name
        self._profile = profile
        self._mail = mail
        self._phone = phone
        self._phone_prefix = phone_prefix
        self._address = address
        self._desc = desc

    @classmethod
    def from_dict(cls, dikt) -> 'Desc':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Desc of this Desc.  # noqa: E501
        :rtype: Desc
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name_id(self) -> str:
        """Gets the name_id of this Desc.


        :return: The name_id of this Desc.
        :rtype: str
        """
        return self._name_id

    @name_id.setter
    def name_id(self, name_id: str):
        """Sets the name_id of this Desc.


        :param name_id: The name_id of this Desc.
        :type name_id: str
        """

        self._name_id = name_id

    @property
    def name(self) -> str:
        """Gets the name of this Desc.


        :return: The name of this Desc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Desc.


        :param name: The name of this Desc.
        :type name: str
        """

        self._name = name

    @property
    def profile(self) -> str:
        """Gets the profile of this Desc.


        :return: The profile of this Desc.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile: str):
        """Sets the profile of this Desc.


        :param profile: The profile of this Desc.
        :type profile: str
        """

        self._profile = profile

    @property
    def mail(self) -> str:
        """Gets the mail of this Desc.


        :return: The mail of this Desc.
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail: str):
        """Sets the mail of this Desc.


        :param mail: The mail of this Desc.
        :type mail: str
        """

        self._mail = mail

    @property
    def phone(self) -> int:
        """Gets the phone of this Desc.


        :return: The phone of this Desc.
        :rtype: int
        """
        return self._phone

    @phone.setter
    def phone(self, phone: int):
        """Sets the phone of this Desc.


        :param phone: The phone of this Desc.
        :type phone: int
        """

        self._phone = phone

    @property
    def phone_prefix(self) -> int:
        """Gets the phone_prefix of this Desc.


        :return: The phone_prefix of this Desc.
        :rtype: int
        """
        return self._phone_prefix

    @phone_prefix.setter
    def phone_prefix(self, phone_prefix: int):
        """Sets the phone_prefix of this Desc.


        :param phone_prefix: The phone_prefix of this Desc.
        :type phone_prefix: int
        """

        self._phone_prefix = phone_prefix

    @property
    def address(self) -> str:
        """Gets the address of this Desc.


        :return: The address of this Desc.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this Desc.


        :param address: The address of this Desc.
        :type address: str
        """

        self._address = address

    @property
    def desc(self) -> str:
        """Gets the desc of this Desc.


        :return: The desc of this Desc.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc: str):
        """Sets the desc of this Desc.


        :param desc: The desc of this Desc.
        :type desc: str
        """

        self._desc = desc
