# coding: utf-8

# flake8: noqa

"""
    LiveAgent API

    This page contains complete API documentation for LiveAgent software. To display additional info and examples for specific API method, just click on the method name in the list below.<br/><br/>To be able to make API requests you need to generate an API key in your admin panel first. [See this article for detailed info.](https://support.ladesk.com/741982-API-key)<br/><br/>Additional info about more advanced agent, contact or ticket API filters can be found [in this article](https://support.ladesk.com/513528-APIv3-advanced-filter-examples).<br/><br/>If you have any question or doubts regarding this API, please do not hesitate to contact our support team.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from liveagent_api.api.agent_phone_api import AgentPhoneApi
from liveagent_api.api.agents_api import AgentsApi
from liveagent_api.api.api_api import ApiApi
from liveagent_api.api.bans_api import BansApi
from liveagent_api.api.billing_api import BillingApi
from liveagent_api.api.calls_api import CallsApi
from liveagent_api.api.canned_messages_api import CannedMessagesApi
from liveagent_api.api.chats_api import ChatsApi
from liveagent_api.api.companies_api import CompaniesApi
from liveagent_api.api.contact_phones_api import ContactPhonesApi
from liveagent_api.api.contacts_api import ContactsApi
from liveagent_api.api.countries_api import CountriesApi
from liveagent_api.api.custom_buttons_api import CustomButtonsApi
from liveagent_api.api.default_api import DefaultApi
from liveagent_api.api.departments_api import DepartmentsApi
from liveagent_api.api.devices_api import DevicesApi
from liveagent_api.api.elastic_api import ElasticApi
from liveagent_api.api.extensions_api import ExtensionsApi
from liveagent_api.api.files_api import FilesApi
from liveagent_api.api.filters_api import FiltersApi
from liveagent_api.api.grid_api import GridApi
from liveagent_api.api.groups_api import GroupsApi
from liveagent_api.api.hosting_api import HostingApi
from liveagent_api.api.invoices_api import InvoicesApi
from liveagent_api.api.mail_account_api import MailAccountApi
from liveagent_api.api.messages_api import MessagesApi
from liveagent_api.api.page_visits_api import PageVisitsApi
from liveagent_api.api.phone_numbers_api import PhoneNumbersApi
from liveagent_api.api.phones_api import PhonesApi
from liveagent_api.api.predefined_answers_api import PredefinedAnswersApi
from liveagent_api.api.queue_api import QueueApi
from liveagent_api.api.settings_api import SettingsApi
from liveagent_api.api.slack_api import SlackApi
from liveagent_api.api.slas_api import SlasApi
from liveagent_api.api.subscriptions_api import SubscriptionsApi
from liveagent_api.api.tags_api import TagsApi
from liveagent_api.api.tickets_api import TicketsApi
from liveagent_api.api.token_api import TokenApi
from liveagent_api.api.user_api import UserApi
from liveagent_api.api.variations_api import VariationsApi
from liveagent_api.api.viber_api import ViberApi

# import ApiClient
from liveagent_api.api_client import ApiClient
from liveagent_api.configuration import Configuration
# import models into sdk package
from liveagent_api.models.active_ticket import ActiveTicket
from liveagent_api.models.addon import Addon
from liveagent_api.models.addon_list import AddonList
from liveagent_api.models.agent import Agent
from liveagent_api.models.agent_activity import AgentActivity
from liveagent_api.models.agent_row import AgentRow
from liveagent_api.models.agent_status import AgentStatus
from liveagent_api.models.agent_statuses import AgentStatuses
from liveagent_api.models.api_info import ApiInfo
from liveagent_api.models.api_key import ApiKey
from liveagent_api.models.api_key_login import ApiKeyLogin
from liveagent_api.models.api_privilege import ApiPrivilege
from liveagent_api.models.attribute_simple import AttributeSimple
from liveagent_api.models.available_prefix import AvailablePrefix
from liveagent_api.models.ban import Ban
from liveagent_api.models.batch import Batch
from liveagent_api.models.billing_info import BillingInfo
from liveagent_api.models.billing_metric import BillingMetric
from liveagent_api.models.billing_status import BillingStatus
from liveagent_api.models.call import Call
from liveagent_api.models.call_agent import CallAgent
from liveagent_api.models.call_list_item import CallListItem
from liveagent_api.models.call_message import CallMessage
from liveagent_api.models.call_status import CallStatus
from liveagent_api.models.call_transfer_result import CallTransferResult
from liveagent_api.models.canned_message import CannedMessage
from liveagent_api.models.chat_information import ChatInformation
from liveagent_api.models.chat_row import ChatRow
from liveagent_api.models.company_list_item import CompanyListItem
from liveagent_api.models.company_request import CompanyRequest
from liveagent_api.models.contact_list_item import ContactListItem
from liveagent_api.models.contact_phone import ContactPhone
from liveagent_api.models.contact_request import ContactRequest
from liveagent_api.models.count import Count
from liveagent_api.models.country import Country
from liveagent_api.models.coupon import Coupon
from liveagent_api.models.custom_button import CustomButton
from liveagent_api.models.custom_fields import CustomFields
from liveagent_api.models.customer import Customer
from liveagent_api.models.day_interval import DayInterval
from liveagent_api.models.department import Department
from liveagent_api.models.department_row import DepartmentRow
from liveagent_api.models.device import Device
from liveagent_api.models.device_department import DeviceDepartment
from liveagent_api.models.device_department_list import DeviceDepartmentList
from liveagent_api.models.device_department_plan import DeviceDepartmentPlan
from liveagent_api.models.device_department_plan_list import DeviceDepartmentPlanList
from liveagent_api.models.discount_value import DiscountValue
from liveagent_api.models.domain import Domain
from liveagent_api.models.elastic_message import ElasticMessage
from liveagent_api.models.error_response import ErrorResponse
from liveagent_api.models.event_log_row import EventLogRow
from liveagent_api.models.extension import Extension
from liveagent_api.models.filter import Filter
from liveagent_api.models.filter_condition import FilterCondition
from liveagent_api.models.group import Group
from liveagent_api.models.hosting_info import HostingInfo
from liveagent_api.models.index_status import IndexStatus
from liveagent_api.models.index_status_data import IndexStatusData
from liveagent_api.models.invoice import Invoice
from liveagent_api.models.invoice_item import InvoiceItem
from liveagent_api.models.invoice_list import InvoiceList
from liveagent_api.models.ivr import Ivr
from liveagent_api.models.ivr_choice import IvrChoice
from liveagent_api.models.ivr_fetch import IvrFetch
from liveagent_api.models.ivr_fetch_param import IvrFetchParam
from liveagent_api.models.ivr_step import IvrStep
from liveagent_api.models.language_row import LanguageRow
from liveagent_api.models.mail_account import MailAccount
from liveagent_api.models.message import Message
from liveagent_api.models.message_group import MessageGroup
from liveagent_api.models.ok_response import OkResponse
from liveagent_api.models.page_visit import PageVisit
from liveagent_api.models.payment_info import PaymentInfo
from liveagent_api.models.payment_method import PaymentMethod
from liveagent_api.models.payment_processor_type import PaymentProcessorType
from liveagent_api.models.phone_device import PhoneDevice
from liveagent_api.models.phone_number import PhoneNumber
from liveagent_api.models.predefined_answer import PredefinedAnswer
from liveagent_api.models.reindex_data import ReindexData
from liveagent_api.models.sso_key import SSOKey
from liveagent_api.models.setting import Setting
from liveagent_api.models.sla import Sla
from liveagent_api.models.sla_business_hours import SlaBusinessHours
from liveagent_api.models.sla_history import SlaHistory
from liveagent_api.models.sla_log_row import SlaLogRow
from liveagent_api.models.sla_values import SlaValues
from liveagent_api.models.slack_conversation import SlackConversation
from liveagent_api.models.slack_template import SlackTemplate
from liveagent_api.models.slack_user import SlackUser
from liveagent_api.models.stop_reason import StopReason
from liveagent_api.models.stored_file import StoredFile
from liveagent_api.models.subscription import Subscription
from liveagent_api.models.tag import Tag
from liveagent_api.models.tag_row import TagRow
from liveagent_api.models.ticket import Ticket
from liveagent_api.models.ticket_attribute import TicketAttribute
from liveagent_api.models.ticket_history import TicketHistory
from liveagent_api.models.ticket_information import TicketInformation
from liveagent_api.models.ticket_list_item import TicketListItem
from liveagent_api.models.ticket_postpone import TicketPostpone
from liveagent_api.models.ticket_row import TicketRow
from liveagent_api.models.ticket_sla import TicketSla
from liveagent_api.models.ticket_updatable import TicketUpdatable
from liveagent_api.models.time_report_row import TimeReportRow
from liveagent_api.models.token import Token
from liveagent_api.models.upgrade import Upgrade
from liveagent_api.models.usage_data import UsageData
from liveagent_api.models.user import User
from liveagent_api.models.variation import Variation
from liveagent_api.models.variation_upgrade import VariationUpgrade
from liveagent_api.models.variation_upgrades import VariationUpgrades
from liveagent_api.models.viber_account import ViberAccount
from liveagent_api.models.api_key_with_privileges import ApiKeyWithPrivileges
from liveagent_api.models.ban_list_item import BanListItem
from liveagent_api.models.company import Company
from liveagent_api.models.contact import Contact
from liveagent_api.models.viber_account_list_item import ViberAccountListItem
