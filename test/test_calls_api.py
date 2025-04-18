# coding: utf-8

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.liveagent.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.liveagent.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import liveagent_api
from liveagent_api.api.calls_api import CallsApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestCallsApi(unittest.TestCase):
    """CallsApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.calls_api.CallsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_call_add_message(self):
        """Test case for call_add_message

        Adds a message to the call group in corresponding ticket  # noqa: E501
        """
        pass

    def test_call_add_recording(self):
        """Test case for call_add_recording

        Adds a recording to the call group in corresponding ticket  # noqa: E501
        """
        pass

    def test_call_answer(self):
        """Test case for call_answer

        Set call as answered by agent  # noqa: E501
        """
        pass

    def test_call_blind_transfer(self):
        """Test case for call_blind_transfer

        Transfers call to different department / agent  # noqa: E501
        """
        pass

    def test_call_change_channel_status(self):
        """Test case for call_change_channel_status

        Change channel status  # noqa: E501
        """
        pass

    def test_call_create(self):
        """Test case for call_create

        Create new call  # noqa: E501
        """
        pass

    def test_call_fetch_ivr(self):
        """Test case for call_fetch_ivr

        Fetches IVR for the call from external URL  # noqa: E501
        """
        pass

    def test_call_get_status(self):
        """Test case for call_get_status

        Return the status of call  # noqa: E501
        """
        pass

    def test_call_id(self):
        """Test case for call_id

        Return the call ID  # noqa: E501
        """
        pass

    def test_call_move_channel(self):
        """Test case for call_move_channel

        Moves existing channel to target call  # noqa: E501
        """
        pass

    def test_call_pickup(self):
        """Test case for call_pickup

        Pick up call from queue  # noqa: E501
        """
        pass

    def test_call_remove_channel(self):
        """Test case for call_remove_channel

        Removes channel from the call  # noqa: E501
        """
        pass

    def test_call_reroute(self):
        """Test case for call_reroute

        Let the call ring to another agent  # noqa: E501
        """
        pass

    def test_call_ring(self):
        """Test case for call_ring

        Let the call ring  # noqa: E501
        """
        pass

    def test_call_start(self):
        """Test case for call_start

        Starts new outcoming / internal call  # noqa: E501
        """
        pass

    def test_call_start_canceled(self):
        """Test case for call_start_canceled

        Callback that starting call canceled  # noqa: E501
        """
        pass

    def test_call_start_failed(self):
        """Test case for call_start_failed

        Callback that starting call failed  # noqa: E501
        """
        pass

    def test_call_stop(self):
        """Test case for call_stop

        Stops the call  # noqa: E501
        """
        pass

    def test_call_transfer(self):
        """Test case for call_transfer

        Transfers call to different department / agent  # noqa: E501
        """
        pass

    def test_confirm_ring(self):
        """Test case for confirm_ring

        Confirm that call is ringing  # noqa: E501
        """
        pass

    def test_dtmf_channel(self):
        """Test case for dtmf_channel

        Send provided DTMF to channel  # noqa: E501
        """
        pass

    def test_end_channel(self):
        """Test case for end_channel

        End channel  # noqa: E501
        """
        pass

    def test_get_calls_count(self):
        """Test case for get_calls_count

        Gets count for calls history  # noqa: E501
        """
        pass

    def test_get_calls_list(self):
        """Test case for get_calls_list

        Gets list of calls  # noqa: E501
        """
        pass

    def test_hold_channel(self):
        """Test case for hold_channel

        Hold channel  # noqa: E501
        """
        pass

    def test_merge(self):
        """Test case for merge

        Merge two calls  # noqa: E501
        """
        pass

    def test_mute_channel(self):
        """Test case for mute_channel

        Mute channel  # noqa: E501
        """
        pass

    def test_stop_ring(self):
        """Test case for stop_ring

        Stop ringing of call  # noqa: E501
        """
        pass

    def test_unhold_channel(self):
        """Test case for unhold_channel

        Unhold channel  # noqa: E501
        """
        pass

    def test_unmute_channel(self):
        """Test case for unmute_channel

        Unmute channel  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
