# coding: utf-8

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.ladesk.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.ladesk.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import liveagent_api
from liveagent_api.api.subscriptions_api import SubscriptionsApi  # noqa: E501
from liveagent_api.rest import ApiException


class TestSubscriptionsApi(unittest.TestCase):
    """SubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = liveagent_api.api.subscriptions_api.SubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_addons(self):
        """Test case for change_addons

        Addon change  # noqa: E501
        """
        pass

    def test_change_plan(self):
        """Test case for change_plan

        Change plan  # noqa: E501
        """
        pass

    def test_get_active_addons(self):
        """Test case for get_active_addons

        Addon list  # noqa: E501
        """
        pass

    def test_get_billing_info(self):
        """Test case for get_billing_info

        Billing info  # noqa: E501
        """
        pass

    def test_get_billing_metrics(self):
        """Test case for get_billing_metrics

        Billing metrics  # noqa: E501
        """
        pass

    def test_get_billing_status(self):
        """Test case for get_billing_status

        Billing status  # noqa: E501
        """
        pass

    def test_get_domain_info(self):
        """Test case for get_domain_info

        Domain info  # noqa: E501
        """
        pass

    def test_get_payment_method(self):
        """Test case for get_payment_method

        Payment method  # noqa: E501
        """
        pass

    def test_get_payment_processor(self):
        """Test case for get_payment_processor

        Payment processor  # noqa: E501
        """
        pass

    def test_get_subscription(self):
        """Test case for get_subscription

        Subscription  # noqa: E501
        """
        pass

    def test_get_subscription_attributes(self):
        """Test case for get_subscription_attributes

        Subscription attribute list  # noqa: E501
        """
        pass

    def test_get_subscription_discounts(self):
        """Test case for get_subscription_discounts

        Subscription discounts  # noqa: E501
        """
        pass

    def test_get_subscription_invoices(self):
        """Test case for get_subscription_invoices

        Subscription invoice list  # noqa: E501
        """
        pass

    def test_get_upgrade_variations(self):
        """Test case for get_upgrade_variations

        Upgrade variation list  # noqa: E501
        """
        pass

    def test_resume_billing(self):
        """Test case for resume_billing

        Restart billing  # noqa: E501
        """
        pass

    def test_set_billing_info(self):
        """Test case for set_billing_info

        Billing info  # noqa: E501
        """
        pass

    def test_set_custom_domain(self):
        """Test case for set_custom_domain

        Custom domain  # noqa: E501
        """
        pass

    def test_set_payment_method(self):
        """Test case for set_payment_method

        Payment method  # noqa: E501
        """
        pass

    def test_set_subscription_usage(self):
        """Test case for set_subscription_usage

        Subscription usage  # noqa: E501
        """
        pass

    def test_stop_billing(self):
        """Test case for stop_billing

        Stop billing  # noqa: E501
        """
        pass

    def test_update_application(self):
        """Test case for update_application

        Update subscription  # noqa: E501
        """
        pass

    def test_validate_billing_info(self):
        """Test case for validate_billing_info

        Test Billing info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
