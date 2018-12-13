# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Call(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Call - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'ticket_id': 'str',
            'direction': 'str',
            'callee_status': 'str',
            'ivrs': 'list[Ivr]',
            'record_call': 'bool',
            'reroute_time': 'float',
            'max_queue_time': 'float',
            'max_ring_time': 'float',
            'online_ivr': 'str',
            'offline_ivr': 'str',
            'queue_ivr': 'str',
            'from_number': 'str',
            'caller_name': 'str',
            'to_number': 'str',
            'via_number': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'ticket_id': 'ticket_id',
            'direction': 'direction',
            'callee_status': 'callee_status',
            'ivrs': 'ivrs',
            'record_call': 'record_call',
            'reroute_time': 'reroute_time',
            'max_queue_time': 'max_queue_time',
            'max_ring_time': 'max_ring_time',
            'online_ivr': 'online_ivr',
            'offline_ivr': 'offline_ivr',
            'queue_ivr': 'queue_ivr',
            'from_number': 'from_number',
            'caller_name': 'caller_name',
            'to_number': 'to_number',
            'via_number': 'via_number'
        }

        self._id = None
        self._ticket_id = None
        self._direction = None
        self._callee_status = None
        self._ivrs = None
        self._record_call = False
        self._reroute_time = None
        self._max_queue_time = None
        self._max_ring_time = None
        self._online_ivr = None
        self._offline_ivr = None
        self._queue_ivr = None
        self._from_number = None
        self._caller_name = None
        self._to_number = None
        self._via_number = None

    @property
    def id(self):
        """
        Gets the id of this Call.


        :return: The id of this Call.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Call.


        :param id: The id of this Call.
        :type: str
        """
        self._id = id

    @property
    def ticket_id(self):
        """
        Gets the ticket_id of this Call.


        :return: The ticket_id of this Call.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        """
        Sets the ticket_id of this Call.


        :param ticket_id: The ticket_id of this Call.
        :type: str
        """
        self._ticket_id = ticket_id

    @property
    def direction(self):
        """
        Gets the direction of this Call.
        incoming call ('in' - default), outgoing call ('out'), internal call('int')

        :return: The direction of this Call.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this Call.
        incoming call ('in' - default), outgoing call ('out'), internal call('int')

        :param direction: The direction of this Call.
        :type: str
        """
        allowed_values = ["in", "out", "int"]
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction`, must be one of {0}"
                .format(allowed_values)
            )
        self._direction = direction

    @property
    def callee_status(self):
        """
        Gets the callee_status of this Call.
        O - online, F - offline, U - unknown

        :return: The callee_status of this Call.
        :rtype: str
        """
        return self._callee_status

    @callee_status.setter
    def callee_status(self, callee_status):
        """
        Sets the callee_status of this Call.
        O - online, F - offline, U - unknown

        :param callee_status: The callee_status of this Call.
        :type: str
        """
        allowed_values = ["O", "F", "U"]
        if callee_status not in allowed_values:
            raise ValueError(
                "Invalid value for `callee_status`, must be one of {0}"
                .format(allowed_values)
            )
        self._callee_status = callee_status

    @property
    def ivrs(self):
        """
        Gets the ivrs of this Call.


        :return: The ivrs of this Call.
        :rtype: list[Ivr]
        """
        return self._ivrs

    @ivrs.setter
    def ivrs(self, ivrs):
        """
        Sets the ivrs of this Call.


        :param ivrs: The ivrs of this Call.
        :type: list[Ivr]
        """
        self._ivrs = ivrs

    @property
    def record_call(self):
        """
        Gets the record_call of this Call.


        :return: The record_call of this Call.
        :rtype: bool
        """
        return self._record_call

    @record_call.setter
    def record_call(self, record_call):
        """
        Sets the record_call of this Call.


        :param record_call: The record_call of this Call.
        :type: bool
        """
        self._record_call = record_call

    @property
    def reroute_time(self):
        """
        Gets the reroute_time of this Call.


        :return: The reroute_time of this Call.
        :rtype: float
        """
        return self._reroute_time

    @reroute_time.setter
    def reroute_time(self, reroute_time):
        """
        Sets the reroute_time of this Call.


        :param reroute_time: The reroute_time of this Call.
        :type: float
        """
        self._reroute_time = reroute_time

    @property
    def max_queue_time(self):
        """
        Gets the max_queue_time of this Call.


        :return: The max_queue_time of this Call.
        :rtype: float
        """
        return self._max_queue_time

    @max_queue_time.setter
    def max_queue_time(self, max_queue_time):
        """
        Sets the max_queue_time of this Call.


        :param max_queue_time: The max_queue_time of this Call.
        :type: float
        """
        self._max_queue_time = max_queue_time

    @property
    def max_ring_time(self):
        """
        Gets the max_ring_time of this Call.


        :return: The max_ring_time of this Call.
        :rtype: float
        """
        return self._max_ring_time

    @max_ring_time.setter
    def max_ring_time(self, max_ring_time):
        """
        Sets the max_ring_time of this Call.


        :param max_ring_time: The max_ring_time of this Call.
        :type: float
        """
        self._max_ring_time = max_ring_time

    @property
    def online_ivr(self):
        """
        Gets the online_ivr of this Call.
        Name of IVR in case the service is online. If empty, call starts ringing to agents

        :return: The online_ivr of this Call.
        :rtype: str
        """
        return self._online_ivr

    @online_ivr.setter
    def online_ivr(self, online_ivr):
        """
        Sets the online_ivr of this Call.
        Name of IVR in case the service is online. If empty, call starts ringing to agents

        :param online_ivr: The online_ivr of this Call.
        :type: str
        """
        self._online_ivr = online_ivr

    @property
    def offline_ivr(self):
        """
        Gets the offline_ivr of this Call.
        Name of IVR in case the service is offline. If empty, call hangs up with not available tone

        :return: The offline_ivr of this Call.
        :rtype: str
        """
        return self._offline_ivr

    @offline_ivr.setter
    def offline_ivr(self, offline_ivr):
        """
        Sets the offline_ivr of this Call.
        Name of IVR in case the service is offline. If empty, call hangs up with not available tone

        :param offline_ivr: The offline_ivr of this Call.
        :type: str
        """
        self._offline_ivr = offline_ivr

    @property
    def queue_ivr(self):
        """
        Gets the queue_ivr of this Call.
        Name of IVR while waiting in queue. If empty, default in queue music is played

        :return: The queue_ivr of this Call.
        :rtype: str
        """
        return self._queue_ivr

    @queue_ivr.setter
    def queue_ivr(self, queue_ivr):
        """
        Sets the queue_ivr of this Call.
        Name of IVR while waiting in queue. If empty, default in queue music is played

        :param queue_ivr: The queue_ivr of this Call.
        :type: str
        """
        self._queue_ivr = queue_ivr

    @property
    def from_number(self):
        """
        Gets the from_number of this Call.
        Caller number

        :return: The from_number of this Call.
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """
        Sets the from_number of this Call.
        Caller number

        :param from_number: The from_number of this Call.
        :type: str
        """
        self._from_number = from_number

    @property
    def caller_name(self):
        """
        Gets the caller_name of this Call.
        Name of the caller in case it is known

        :return: The caller_name of this Call.
        :rtype: str
        """
        return self._caller_name

    @caller_name.setter
    def caller_name(self, caller_name):
        """
        Sets the caller_name of this Call.
        Name of the caller in case it is known

        :param caller_name: The caller_name of this Call.
        :type: str
        """
        self._caller_name = caller_name

    @property
    def to_number(self):
        """
        Gets the to_number of this Call.
        Callee number

        :return: The to_number of this Call.
        :rtype: str
        """
        return self._to_number

    @to_number.setter
    def to_number(self, to_number):
        """
        Sets the to_number of this Call.
        Callee number

        :param to_number: The to_number of this Call.
        :type: str
        """
        self._to_number = to_number

    @property
    def via_number(self):
        """
        Gets the via_number of this Call.
        trunk number via which call was made / received (if applicable)

        :return: The via_number of this Call.
        :rtype: str
        """
        return self._via_number

    @via_number.setter
    def via_number(self, via_number):
        """
        Sets the via_number of this Call.
        trunk number via which call was made / received (if applicable)

        :param via_number: The via_number of this Call.
        :type: str
        """
        self._via_number = via_number

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

