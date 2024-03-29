# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from crm.models.base_model_ import Model
from crm import util
from crm.models.addr import Addr


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, age: int=None, gender: str=None, addr: Addr=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param age: The age of this User.  # noqa: E501
        :type age: int
        :param gender: The gender of this User.  # noqa: E501
        :type gender: str
        :param addr: The addr of this User.  # noqa: E501
        :type addr: Addr
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'age': int,
            'gender': str,
            'addr': Addr
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'age': 'age',
            'gender': 'gender',
            'addr': 'addr'
        }

        self._id = id
        self._name = name
        self._age = age
        self._gender = gender
        self._addr = addr

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this User.


        :param name: The name of this User.
        :type name: str
        """

        self._name = name

    @property
    def age(self) -> int:
        """Gets the age of this User.


        :return: The age of this User.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """Sets the age of this User.


        :param age: The age of this User.
        :type age: int
        """

        self._age = age

    @property
    def gender(self) -> str:
        """Gets the gender of this User.


        :return: The gender of this User.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this User.


        :param gender: The gender of this User.
        :type gender: str
        """
        allowed_values = ["남자", "여자"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def addr(self) -> Addr:
        """Gets the addr of this User.


        :return: The addr of this User.
        :rtype: Addr
        """
        return self._addr

    @addr.setter
    def addr(self, addr: Addr):
        """Sets the addr of this User.


        :param addr: The addr of this User.
        :type addr: Addr
        """

        self._addr = addr
