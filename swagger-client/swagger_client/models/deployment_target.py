# coding: utf-8

"""
    Platform API

    The REST API for Platform.sh.

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeploymentTarget(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, hosts=None, type=None, name=None):
        """
        DeploymentTarget - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'hosts': 'list[DeploymentTargetHosts]',
            'type': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'hosts': 'hosts',
            'type': 'type',
            'name': 'name'
        }

        self._hosts = hosts
        self._type = type
        self._name = name

    @property
    def hosts(self):
        """
        Gets the hosts of this DeploymentTarget.

        :return: The hosts of this DeploymentTarget.
        :rtype: list[DeploymentTargetHosts]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this DeploymentTarget.

        :param hosts: The hosts of this DeploymentTarget.
        :type: list[DeploymentTargetHosts]
        """
        if hosts is None:
            raise ValueError("Invalid value for `hosts`, must not be `None`")

        self._hosts = hosts

    @property
    def type(self):
        """
        Gets the type of this DeploymentTarget.

        :return: The type of this DeploymentTarget.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DeploymentTarget.

        :param type: The type of this DeploymentTarget.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this DeploymentTarget.

        :return: The name of this DeploymentTarget.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeploymentTarget.

        :param name: The name of this DeploymentTarget.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, DeploymentTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
