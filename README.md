# liveagent-api
LiveAgent API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import liveagent_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import liveagent_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import liveagent_api
from liveagent_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
liveagent_api.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# liveagent_api.configuration.api_key_prefix['apikey'] = 'Bearer'
# Configure OAuth2 access token for authorization: privileges
liveagent_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = liveagent_api.AgentPhoneApi()
agent_id = 'agent_id_example' # str | 
type = 'I' # str | API (I - default), SIP (S) (optional) (default to I)

try:
    # Gets phone currently used by agent (use me as agentId for self)
    api_response = api_instance.get_agent_phone(agent_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPhoneApi->get_agent_phone: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentPhoneApi* | [**get_agent_phone**](docs/AgentPhoneApi.md#get_agent_phone) | **GET** /agent_phone/{agentId} | Gets phone currently used by agent (use me as agentId for self)
*AgentPhoneApi* | [**set_agent_phone**](docs/AgentPhoneApi.md#set_agent_phone) | **PUT** /agent_phone/{agentId} | Sets phone currently used by agent (use me as agentId for self)
*AgentsApi* | [**convert_registered_visitor**](docs/AgentsApi.md#convert_registered_visitor) | **POST** /agents/convert | Convert registered visitor
*AgentsApi* | [**delete_agent**](docs/AgentsApi.md#delete_agent) | **DELETE** /agents/{userId} | Agent
*AgentsApi* | [**get_agent**](docs/AgentsApi.md#get_agent) | **GET** /agents/{userId} | Agent
*AgentsApi* | [**get_agent_statuses**](docs/AgentsApi.md#get_agent_statuses) | **GET** /agents/{userId}/status | Get agent statuses in departments
*AgentsApi* | [**get_agents**](docs/AgentsApi.md#get_agents) | **GET** /agents/ | Agent list
*AgentsApi* | [**get_agents_activity**](docs/AgentsApi.md#get_agents_activity) | **GET** /agents/activity | Agent Activity list
*AgentsApi* | [**login_agent**](docs/AgentsApi.md#login_agent) | **POST** /agents/{userId}/_login | Login agent
*AgentsApi* | [**logout_agent**](docs/AgentsApi.md#logout_agent) | **POST** /agents/{userId}/_logout | Logout agent
*AgentsApi* | [**pause_agent**](docs/AgentsApi.md#pause_agent) | **POST** /agents/{userId}/_pause | Pause agent
*AgentsApi* | [**undelete_agent**](docs/AgentsApi.md#undelete_agent) | **POST** /agents/undelete | Undelete agent
*AgentsApi* | [**update_agent**](docs/AgentsApi.md#update_agent) | **PUT** /agents/{userId} | Update agent
*ApiApi* | [**create_api_keys**](docs/ApiApi.md#create_api_keys) | **POST** /apikeys | Creates api key
*ApiApi* | [**delete_api_key**](docs/ApiApi.md#delete_api_key) | **DELETE** /apikeys/{apikeyId} | Deletes api key
*ApiApi* | [**generate_api_key**](docs/ApiApi.md#generate_api_key) | **POST** /apikeys/_generate | Gets new api keys
*ApiApi* | [**get_api_info**](docs/ApiApi.md#get_api_info) | **GET** /api/info/{apiVersion} | Gets api info
*ApiApi* | [**get_api_key**](docs/ApiApi.md#get_api_key) | **GET** /apikeys/{apikeyId} | Gets api keys
*ApiApi* | [**get_api_keys**](docs/ApiApi.md#get_api_keys) | **GET** /apikeys | Gets api keys
*ApiApi* | [**get_api_privileges**](docs/ApiApi.md#get_api_privileges) | **GET** /api/privileges | Gets api privileges
*ApiApi* | [**login**](docs/ApiApi.md#login) | **POST** /apikeys/_login | Creates or returns API key from login.
*ApiApi* | [**update_api_key**](docs/ApiApi.md#update_api_key) | **PUT** /apikeys/{apikeyId} | Updates api key
*BansApi* | [**create_ban**](docs/BansApi.md#create_ban) | **POST** /bans/ | Create ban
*BansApi* | [**expire_ban**](docs/BansApi.md#expire_ban) | **POST** /bans/{banId}/_expire | Expire ban
*BansApi* | [**get_ban**](docs/BansApi.md#get_ban) | **GET** /bans/{banId} | Get ban item
*BansApi* | [**get_bans**](docs/BansApi.md#get_bans) | **GET** /bans/ | Bans list
*BansApi* | [**update_ban**](docs/BansApi.md#update_ban) | **PUT** /bans/{banId} | Update ban
*BillingApi* | [**check_vat**](docs/BillingApi.md#check_vat) | **POST** /billing/_check_vat | Vat validity
*BillingApi* | [**get_coupon**](docs/BillingApi.md#get_coupon) | **GET** /coupons/{couponCode} | Coupon
*CallsApi* | [**call_add_message**](docs/CallsApi.md#call_add_message) | **POST** /calls/{callId}/messages | Adds a message to the call group in corresponfing ticket
*CallsApi* | [**call_add_recording**](docs/CallsApi.md#call_add_recording) | **POST** /calls/{callId}/recordings | Adds a recording to the call group in corresponfing ticket
*CallsApi* | [**call_answer**](docs/CallsApi.md#call_answer) | **POST** /calls/{callId}/_answer | Set call as answered by agent
*CallsApi* | [**call_change_channel_status**](docs/CallsApi.md#call_change_channel_status) | **PUT** /calls/{callId}/channels/{channelId}/_status | Change channel status
*CallsApi* | [**call_create**](docs/CallsApi.md#call_create) | **POST** /calls/{callId} | Create new call
*CallsApi* | [**call_fetch_ivr**](docs/CallsApi.md#call_fetch_ivr) | **POST** /calls/{callId}/_fetchIvr | Fetches IVR for the call from external URL
*CallsApi* | [**call_get_status**](docs/CallsApi.md#call_get_status) | **GET** /calls/{callId}/status | Return the status of call
*CallsApi* | [**call_move_channel**](docs/CallsApi.md#call_move_channel) | **POST** /calls/{callId}/channels/{channelId}/_move | Moves existing channel to target call
*CallsApi* | [**call_remove_channel**](docs/CallsApi.md#call_remove_channel) | **DELETE** /calls/{callId}/channels/{channelId} | Removes channel from the call
*CallsApi* | [**call_reroute**](docs/CallsApi.md#call_reroute) | **POST** /calls/{callId}/_reroute | Let the call ring to another agent
*CallsApi* | [**call_ring**](docs/CallsApi.md#call_ring) | **POST** /calls/{callId}/_ring | Let the call ring
*CallsApi* | [**call_start**](docs/CallsApi.md#call_start) | **POST** /call/_start | Starts new outcoming / internal call
*CallsApi* | [**call_start_canceled**](docs/CallsApi.md#call_start_canceled) | **POST** /call/_startCanceled | Callback that starting call canceled
*CallsApi* | [**call_start_failed**](docs/CallsApi.md#call_start_failed) | **POST** /call/_startFailed | Callback that starting call failed
*CallsApi* | [**call_stop**](docs/CallsApi.md#call_stop) | **POST** /calls/{callId}/_stop | Stops the call
*CallsApi* | [**call_transfer**](docs/CallsApi.md#call_transfer) | **POST** /calls/{callId}/_transfer | Transfers call to different department / agent
*CallsApi* | [**confirm_ring**](docs/CallsApi.md#confirm_ring) | **POST** /calls/{callId}/_confirmRing | Confirm that call is ringing
*CallsApi* | [**dtmf_channel**](docs/CallsApi.md#dtmf_channel) | **POST** /calls/{callId}/channels/{channelId}/_dtmf | Send provided DTMF to channel
*CallsApi* | [**end_channel**](docs/CallsApi.md#end_channel) | **POST** /calls/{callId}/channels/{channelId}/_end | End channel
*CallsApi* | [**get_calls_list**](docs/CallsApi.md#get_calls_list) | **GET** /calls | Gets list of calls
*CallsApi* | [**hold_channel**](docs/CallsApi.md#hold_channel) | **POST** /calls/{callId}/channels/{channelId}/_hold | Hold channel
*CallsApi* | [**merge**](docs/CallsApi.md#merge) | **POST** /calls/{callId}/_merge | Merge two calls
*CallsApi* | [**mute_channel**](docs/CallsApi.md#mute_channel) | **POST** /calls/{callId}/channels/{channelId}/_mute | Mute channel
*CallsApi* | [**stop_ring**](docs/CallsApi.md#stop_ring) | **POST** /calls/{callId}/_stopRing | Stop ringing of call
*CallsApi* | [**unhol_channel**](docs/CallsApi.md#unhol_channel) | **POST** /calls/{callId}/channels/{channelId}/_unhold | Unhold channel
*CallsApi* | [**unmute_channel**](docs/CallsApi.md#unmute_channel) | **POST** /calls/{callId}/channels/{channelId}/_unmute | Unmute channel
*CannedMessagesApi* | [**create_canned_message**](docs/CannedMessagesApi.md#create_canned_message) | **POST** /canned_messages | Create canned message
*CannedMessagesApi* | [**delete_canned_message**](docs/CannedMessagesApi.md#delete_canned_message) | **DELETE** /canned_messages/{cannedMessageId} | Canned message
*CannedMessagesApi* | [**get_canned_message**](docs/CannedMessagesApi.md#get_canned_message) | **GET** /canned_messages/{cannedMessageId} | Gets canned message
*CannedMessagesApi* | [**get_canned_messages_list**](docs/CannedMessagesApi.md#get_canned_messages_list) | **GET** /canned_messages | Gets list of canned messages
*CannedMessagesApi* | [**update_canned_message**](docs/CannedMessagesApi.md#update_canned_message) | **PUT** /canned_messages/{cannedMessageId} | Update canned message
*ChatsApi* | [**get_chats_list**](docs/ChatsApi.md#get_chats_list) | **GET** /chats | Gets list of chats
*CompaniesApi* | [**create_company**](docs/CompaniesApi.md#create_company) | **POST** /companies | Create new company
*CompaniesApi* | [**delete_company**](docs/CompaniesApi.md#delete_company) | **DELETE** /companies/{companyId} | Delete company
*CompaniesApi* | [**get_companies_list**](docs/CompaniesApi.md#get_companies_list) | **GET** /companies | Gets list of companies
*CompaniesApi* | [**get_specific_company**](docs/CompaniesApi.md#get_specific_company) | **GET** /companies/{companyId} | Get company by specific id
*CompaniesApi* | [**update_company**](docs/CompaniesApi.md#update_company) | **PUT** /companies/{companyId} | Update company
*ContactPhonesApi* | [**get_contact_phone**](docs/ContactPhonesApi.md#get_contact_phone) | **GET** /contact_phones/{phone} | Get contact phone
*ContactPhonesApi* | [**get_contact_phones_list**](docs/ContactPhonesApi.md#get_contact_phones_list) | **GET** /contact_phones | Gets list of contact phones
*ContactsApi* | [**create_contact**](docs/ContactsApi.md#create_contact) | **POST** /contacts | Create new contact
*ContactsApi* | [**delete_contact**](docs/ContactsApi.md#delete_contact) | **DELETE** /contacts/{contactId} | Delete contact
*ContactsApi* | [**get_contacts_list**](docs/ContactsApi.md#get_contacts_list) | **GET** /contacts | Gets list of contacts
*ContactsApi* | [**get_specific_contact**](docs/ContactsApi.md#get_specific_contact) | **GET** /contacts/{contactId} | Get contact by specific id
*ContactsApi* | [**update_contact**](docs/ContactsApi.md#update_contact) | **PUT** /contacts/{contactId} | Update contact
*CountriesApi* | [**get_countries**](docs/CountriesApi.md#get_countries) | **GET** /countries/ | Country list
*CustomButtonsApi* | [**create_custom_button**](docs/CustomButtonsApi.md#create_custom_button) | **POST** /custom_buttons | Create new custom button
*CustomButtonsApi* | [**delete_custom_button**](docs/CustomButtonsApi.md#delete_custom_button) | **DELETE** /custom_buttons/{customButtonId} | Delete custom button
*CustomButtonsApi* | [**get_custom_button**](docs/CustomButtonsApi.md#get_custom_button) | **GET** /custom_buttons/{customButtonId} | Get custom button by id
*CustomButtonsApi* | [**get_custom_buttons_list**](docs/CustomButtonsApi.md#get_custom_buttons_list) | **GET** /custom_buttons | Gets list of custom buttons
*CustomButtonsApi* | [**update_custom_button**](docs/CustomButtonsApi.md#update_custom_button) | **PUT** /custom_buttons/{customButtonId} | Update custom button
*DefaultApi* | [**ping**](docs/DefaultApi.md#ping) | **GET** /ping | Check that API is responding
*DepartmentsApi* | [**get_department_list**](docs/DepartmentsApi.md#get_department_list) | **GET** /departments | Gets list of departments
*DepartmentsApi* | [**get_specific_department**](docs/DepartmentsApi.md#get_specific_department) | **GET** /departments/{departmentId} | Get department by specific id
*DepartmentsApi* | [**if_agent_is_in_department**](docs/DepartmentsApi.md#if_agent_is_in_department) | **GET** /departments/{departmentId}/{agentId} | Is agent is department
*DepartmentsApi* | [**update_department_mail_account**](docs/DepartmentsApi.md#update_department_mail_account) | **PUT** /departments/{departmentId}/mailAccount/{mailAccountId} | Update department mail account
*DevicesApi* | [**create_device**](docs/DevicesApi.md#create_device) | **POST** /devices | Create new device
*DevicesApi* | [**create_device_department_plans**](docs/DevicesApi.md#create_device_department_plans) | **POST** /devices/{deviceId}/departments/{departmentId}/plans | Create device department plans
*DevicesApi* | [**delete_device**](docs/DevicesApi.md#delete_device) | **DELETE** /devices/{deviceId} | Delete device
*DevicesApi* | [**delete_device_department**](docs/DevicesApi.md#delete_device_department) | **DELETE** /devices/{deviceId}/departments/{departmentId} | Delete device department
*DevicesApi* | [**delete_device_department_plans**](docs/DevicesApi.md#delete_device_department_plans) | **DELETE** /devices/{deviceId}/departments/{departmentId}/plans | Delete device department plans
*DevicesApi* | [**delete_device_departments**](docs/DevicesApi.md#delete_device_departments) | **DELETE** /devices/{deviceId}/departments | Delete device departments
*DevicesApi* | [**get_device**](docs/DevicesApi.md#get_device) | **GET** /devices/{deviceId} | Get device by id
*DevicesApi* | [**get_device_department**](docs/DevicesApi.md#get_device_department) | **GET** /devices/{deviceId}/departments/{departmentId} | Get device department by id
*DevicesApi* | [**get_device_department_plan**](docs/DevicesApi.md#get_device_department_plan) | **GET** /devices/{deviceId}/departments/{departmentId}/plans | Get device department plan
*DevicesApi* | [**get_device_departments**](docs/DevicesApi.md#get_device_departments) | **GET** /devices/{deviceId}/departments | Get device departments
*DevicesApi* | [**get_device_departments_by_department_id**](docs/DevicesApi.md#get_device_departments_by_department_id) | **GET** /devices/departments/{departmentId} | Get device departments by department id
*DevicesApi* | [**get_devices_list**](docs/DevicesApi.md#get_devices_list) | **GET** /devices | Gets list of devices
*DevicesApi* | [**get_my_mobile_devices_list**](docs/DevicesApi.md#get_my_mobile_devices_list) | **GET** /devices/_app_/ | Gets list of current agent&#39;s mobile devices. Creates new one if there are no devices.
*DevicesApi* | [**update_device**](docs/DevicesApi.md#update_device) | **PUT** /devices/{deviceId} | Update device
*DevicesApi* | [**update_device_department**](docs/DevicesApi.md#update_device_department) | **PUT** /devices/{deviceId}/departments/{departmentId} | Update device department
*DevicesApi* | [**update_device_department_plan**](docs/DevicesApi.md#update_device_department_plan) | **PUT** /devices/{deviceId}/departments/{departmentId}/plans | Update device department plan
*DevicesApi* | [**update_device_departments**](docs/DevicesApi.md#update_device_departments) | **PUT** /devices/departments/update | Update device departments
*ExtensionsApi* | [**get_extension**](docs/ExtensionsApi.md#get_extension) | **GET** /extensions/{extensionId} | Gets Extension
*ExtensionsApi* | [**get_extensions_list**](docs/ExtensionsApi.md#get_extensions_list) | **GET** /extensions | Gets list of extensions
*ExtensionsApi* | [**set_extension**](docs/ExtensionsApi.md#set_extension) | **PUT** /extensions/{extensionId} | Set extension
*FilesApi* | [**upload_file**](docs/FilesApi.md#upload_file) | **POST** /files | Upload new file to the system
*FiltersApi* | [**create_filter**](docs/FiltersApi.md#create_filter) | **POST** /filters/ | Create filter
*FiltersApi* | [**delete_filter**](docs/FiltersApi.md#delete_filter) | **DELETE** /filters/{filterId} | Delete filter
*FiltersApi* | [**get_filter**](docs/FiltersApi.md#get_filter) | **GET** /filters/{filterId} | Get filter
*FiltersApi* | [**get_filters**](docs/FiltersApi.md#get_filters) | **GET** /filters/ | Filters list
*FiltersApi* | [**update_filter**](docs/FiltersApi.md#update_filter) | **PUT** /filters/{filterId} | Update filter
*GroupsApi* | [**create_group**](docs/GroupsApi.md#create_group) | **POST** /groups | Create contact group
*GroupsApi* | [**delete_group**](docs/GroupsApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete contact group
*GroupsApi* | [**get_group_by_id**](docs/GroupsApi.md#get_group_by_id) | **GET** /groups/{groupId} | Get contact group by group id
*GroupsApi* | [**get_groups_list**](docs/GroupsApi.md#get_groups_list) | **GET** /groups | Gets list of contact groups
*GroupsApi* | [**update_group**](docs/GroupsApi.md#update_group) | **PUT** /groups/{groupId} | Update contact group
*HostingApi* | [**get_info**](docs/HostingApi.md#get_info) | **GET** /hosting/info | Used hosting system info
*InvoicesApi* | [**dowload_invoice**](docs/InvoicesApi.md#dowload_invoice) | **POST** /invoices/{invoiceNumber}/_download | Download invoice
*InvoicesApi* | [**get_invoices**](docs/InvoicesApi.md#get_invoices) | **GET** /invoices/ | Invoice list
*MailAccountApi* | [**get_mail_account**](docs/MailAccountApi.md#get_mail_account) | **GET** /mail_accounts/{mailAccountId} | Gets mail account
*MailAccountApi* | [**get_mail_account_list**](docs/MailAccountApi.md#get_mail_account_list) | **GET** /mail_accounts | Gets list of mail accounts
*MessagesApi* | [**get_message**](docs/MessagesApi.md#get_message) | **GET** /messages/{messageId} | Get message
*PageVisitsApi* | [**get_page_visit_by_contact_id**](docs/PageVisitsApi.md#get_page_visit_by_contact_id) | **GET** /page_visits/{contactId}/contact | Gets a page visits
*PhoneNumbersApi* | [**add_number**](docs/PhoneNumbersApi.md#add_number) | **POST** /phone_numbers | Add new number
*PhoneNumbersApi* | [**get_phone_number**](docs/PhoneNumbersApi.md#get_phone_number) | **GET** /phone_numbers/{phoneNumberId} | Gets phone number
*PhoneNumbersApi* | [**get_phone_numbers_list**](docs/PhoneNumbersApi.md#get_phone_numbers_list) | **GET** /phone_numbers | Gets list of available phone numbers
*PhoneNumbersApi* | [**remove_phone_number**](docs/PhoneNumbersApi.md#remove_phone_number) | **DELETE** /phone_numbers/{phoneNumberId} | Remove phone number
*PhoneNumbersApi* | [**update_phone_number**](docs/PhoneNumbersApi.md#update_phone_number) | **PUT** /phone_numbers/{phoneNumberId} | Update phone number
*PhoneNumbersApi* | [**update_phone_number_status**](docs/PhoneNumbersApi.md#update_phone_number_status) | **PUT** /phone_numbers/{phoneNumberId}/status | Update phone number status
*PhonesApi* | [**create_phone**](docs/PhonesApi.md#create_phone) | **POST** /phones | Creates external phone
*PhonesApi* | [**get_phone**](docs/PhonesApi.md#get_phone) | **GET** /phones/{phoneId} | Gets phone device (use _app_ for LiveAgent Phone app device and _web_ for web device)
*PhonesApi* | [**get_phones_list**](docs/PhonesApi.md#get_phones_list) | **GET** /phones | Gets list of available phone devices. Special filters (userId - filter phones available for specified user only) 
*PhonesApi* | [**remove_phone**](docs/PhonesApi.md#remove_phone) | **DELETE** /phones/{phoneId} | Remove phone
*PhonesApi* | [**update_phone**](docs/PhonesApi.md#update_phone) | **PUT** /phones/{phoneId} | Update phone
*PhonesApi* | [**update_phone_params**](docs/PhonesApi.md#update_phone_params) | **PUT** /phones/{phoneId}/_updateParams | Update phone paramas
*PlansApi* | [**get_device_department_plan**](docs/PlansApi.md#get_device_department_plan) | **GET** /devices/{deviceId}/departments/{departmentId}/plans | Get device department plan
*PredefinedAnswersApi* | [**create_predefined_answer**](docs/PredefinedAnswersApi.md#create_predefined_answer) | **POST** /predefined_answers | Create predefined answer
*PredefinedAnswersApi* | [**delete_predefined_answer**](docs/PredefinedAnswersApi.md#delete_predefined_answer) | **DELETE** /predefined_answers/{predefinedAnswerId} | Predefined answer
*PredefinedAnswersApi* | [**get_predefined_answer**](docs/PredefinedAnswersApi.md#get_predefined_answer) | **GET** /predefined_answers/{predefinedAnswerId} | Gets canned message
*PredefinedAnswersApi* | [**get_predefined_answers_list**](docs/PredefinedAnswersApi.md#get_predefined_answers_list) | **GET** /predefined_answers | Gets list of predefined answers
*PredefinedAnswersApi* | [**update_predefined_answer**](docs/PredefinedAnswersApi.md#update_predefined_answer) | **PUT** /predefined_answers/{predefinedAnswerId} | Update predefined answer
*QueueApi* | [**get_queue_batch**](docs/QueueApi.md#get_queue_batch) | **GET** /queue/batch/{batchId} | Retrieves the batch status and remaining items to process
*SettingsApi* | [**get_settings**](docs/SettingsApi.md#get_settings) | **GET** /settings | Gets settings list
*SlasApi* | [**get_sla**](docs/SlasApi.md#get_sla) | **GET** /slas/{levelId} | Gets sla
*SlasApi* | [**get_sla_ticket_history**](docs/SlasApi.md#get_sla_ticket_history) | **GET** /slas/{ticketId}/history | Gets ticket sla history
*SlasApi* | [**get_slas_list**](docs/SlasApi.md#get_slas_list) | **GET** /slas | Gets list of slas
*SubscriptionsApi* | [**change_addons**](docs/SubscriptionsApi.md#change_addons) | **PUT** /subscriptions/{subscriptionId}/addons/ | Addon change
*SubscriptionsApi* | [**change_plan**](docs/SubscriptionsApi.md#change_plan) | **POST** /subscriptions/{subscriptionId}/_upgrade | Change plan
*SubscriptionsApi* | [**get_active_addons**](docs/SubscriptionsApi.md#get_active_addons) | **GET** /subscriptions/{subscriptionId}/addons/ | Addon list
*SubscriptionsApi* | [**get_billing_info**](docs/SubscriptionsApi.md#get_billing_info) | **GET** /subscriptions/{subscriptionId}/billingInfo | Billing info
*SubscriptionsApi* | [**get_billing_metrics**](docs/SubscriptionsApi.md#get_billing_metrics) | **GET** /subscriptions/{subscriptionId}/billingMetrics | Billing metrics
*SubscriptionsApi* | [**get_billing_status**](docs/SubscriptionsApi.md#get_billing_status) | **GET** /subscriptions/{subscriptionId}/billingStatus | Billing status
*SubscriptionsApi* | [**get_domain_info**](docs/SubscriptionsApi.md#get_domain_info) | **GET** /subscriptions/{subscriptionId}/domain | Domain info
*SubscriptionsApi* | [**get_payment_method**](docs/SubscriptionsApi.md#get_payment_method) | **GET** /subscriptions/{subscriptionId}/paymentMethod | Payment method
*SubscriptionsApi* | [**get_payment_processor**](docs/SubscriptionsApi.md#get_payment_processor) | **GET** /subscriptions/{subscriptionId}/paymentProcessor | Payment processor
*SubscriptionsApi* | [**get_subscription**](docs/SubscriptionsApi.md#get_subscription) | **GET** /subscriptions/{subscriptionId} | Subscription
*SubscriptionsApi* | [**get_subscription_attributes**](docs/SubscriptionsApi.md#get_subscription_attributes) | **GET** /subscriptions/{subscriptionId}/attributes/ | Subscription attribute list
*SubscriptionsApi* | [**get_subscription_discounts**](docs/SubscriptionsApi.md#get_subscription_discounts) | **GET** /subscriptions/{subscriptionId}/discounts | Subscription discounts
*SubscriptionsApi* | [**get_subscription_invoices**](docs/SubscriptionsApi.md#get_subscription_invoices) | **GET** /subscriptions/{subscriptionId}/invoices/ | Subscription invoice list
*SubscriptionsApi* | [**get_upgrade_variations**](docs/SubscriptionsApi.md#get_upgrade_variations) | **GET** /subscriptions/{subscriptionId}/upgradeVariations | Upgrade variation list
*SubscriptionsApi* | [**resume_billing**](docs/SubscriptionsApi.md#resume_billing) | **POST** /subscriptions/{subscriptionId}/_cancelStop | Restart billing
*SubscriptionsApi* | [**set_billing_info**](docs/SubscriptionsApi.md#set_billing_info) | **PUT** /subscriptions/{subscriptionId}/billingInfo | Billing info
*SubscriptionsApi* | [**set_custom_domain**](docs/SubscriptionsApi.md#set_custom_domain) | **PUT** /subscriptions/{subscriptionId}/domain | Custom domain
*SubscriptionsApi* | [**set_payment_method**](docs/SubscriptionsApi.md#set_payment_method) | **PUT** /subscriptions/{subscriptionId}/paymentMethod | Payment method
*SubscriptionsApi* | [**set_subscription_usage**](docs/SubscriptionsApi.md#set_subscription_usage) | **PUT** /subscriptions/{subscriptionId}/usage | Subscription usage
*SubscriptionsApi* | [**stop_billing**](docs/SubscriptionsApi.md#stop_billing) | **POST** /subscriptions/{subscriptionId}/_stop | Stop billing
*SubscriptionsApi* | [**update_application**](docs/SubscriptionsApi.md#update_application) | **POST** /subscriptions/{subscriptionId}/_update | Update subscription
*SubscriptionsApi* | [**validate_billing_info**](docs/SubscriptionsApi.md#validate_billing_info) | **POST** /subscriptions/{subscriptionId}/_validateBillingInfo | Test Billing info
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /tags | Create tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /tags/{tagId} | Delete tag
*TagsApi* | [**get_tag_by_id**](docs/TagsApi.md#get_tag_by_id) | **GET** /tags/{tagId} | Get tag by tag id
*TagsApi* | [**get_tags_list**](docs/TagsApi.md#get_tags_list) | **GET** /tags | Gets list of tags
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PUT** /tags/{tagId} | Update tag
*TicketsApi* | [**create_ticket**](docs/TicketsApi.md#create_ticket) | **POST** /tickets | Create ticket
*TicketsApi* | [**delete_ticket**](docs/TicketsApi.md#delete_ticket) | **DELETE** /tickets/{ticketId} | Deletes ticket
*TicketsApi* | [**get_ticket**](docs/TicketsApi.md#get_ticket) | **GET** /tickets/{ticketId} | Gets ticket
*TicketsApi* | [**get_ticket_attribute**](docs/TicketsApi.md#get_ticket_attribute) | **GET** /tickets/{ticketId}/attributes/{attributeName} | Gets ticket attribute
*TicketsApi* | [**get_ticket_history**](docs/TicketsApi.md#get_ticket_history) | **GET** /tickets/history | Gets ticket
*TicketsApi* | [**get_ticket_history_0**](docs/TicketsApi.md#get_ticket_history_0) | **GET** /tickets/{ticketId}/history | Gets ticket history
*TicketsApi* | [**get_ticket_message_groups**](docs/TicketsApi.md#get_ticket_message_groups) | **GET** /tickets/{ticketId}/messages | Gets ticket message groups and messages
*TicketsApi* | [**get_ticket_sla**](docs/TicketsApi.md#get_ticket_sla) | **GET** /tickets/{ticketId}/sla | Gets ticket Sla
*TicketsApi* | [**get_tickets_list**](docs/TicketsApi.md#get_tickets_list) | **GET** /tickets | Gets list of tickets
*TicketsApi* | [**set_ticket_attribute**](docs/TicketsApi.md#set_ticket_attribute) | **PUT** /tickets/{ticketId}/attributes/{attributeName} | Sets ticket attribute
*TicketsApi* | [**set_ticket_postpone**](docs/TicketsApi.md#set_ticket_postpone) | **PUT** /tickets/{ticketId}/postpone | Sets postpone status to ticket
*TicketsApi* | [**update_ticket**](docs/TicketsApi.md#update_ticket) | **PUT** /tickets/{ticketId} | Updates ticket
*TokenApi* | [**get_access_token**](docs/TokenApi.md#get_access_token) | **GET** /token | Access token
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /users/{userId} | User
*VariationsApi* | [**get_variation**](docs/VariationsApi.md#get_variation) | **GET** /variations/{variationId} | Variation


## Documentation For Models

 - [ActiveTicket](docs/ActiveTicket.md)
 - [Addon](docs/Addon.md)
 - [AddonList](docs/AddonList.md)
 - [Agent](docs/Agent.md)
 - [AgentActivity](docs/AgentActivity.md)
 - [AgentStatus](docs/AgentStatus.md)
 - [AgentStatuses](docs/AgentStatuses.md)
 - [ApiInfo](docs/ApiInfo.md)
 - [ApiKey](docs/ApiKey.md)
 - [ApiKeyLogin](docs/ApiKeyLogin.md)
 - [ApiPrivilege](docs/ApiPrivilege.md)
 - [AttributeSimple](docs/AttributeSimple.md)
 - [Ban](docs/Ban.md)
 - [Batch](docs/Batch.md)
 - [BillingInfo](docs/BillingInfo.md)
 - [BillingMetric](docs/BillingMetric.md)
 - [BillingStatus](docs/BillingStatus.md)
 - [Call](docs/Call.md)
 - [CallAgent](docs/CallAgent.md)
 - [CallListItem](docs/CallListItem.md)
 - [CallMessage](docs/CallMessage.md)
 - [CallStatus](docs/CallStatus.md)
 - [CallTransferResult](docs/CallTransferResult.md)
 - [CannedMessage](docs/CannedMessage.md)
 - [ChatInformation](docs/ChatInformation.md)
 - [CompanyListItem](docs/CompanyListItem.md)
 - [ContactListItem](docs/ContactListItem.md)
 - [ContactPhone](docs/ContactPhone.md)
 - [Country](docs/Country.md)
 - [Coupon](docs/Coupon.md)
 - [CustomButton](docs/CustomButton.md)
 - [CustomFields](docs/CustomFields.md)
 - [Customer](docs/Customer.md)
 - [DayInterval](docs/DayInterval.md)
 - [Department](docs/Department.md)
 - [Device](docs/Device.md)
 - [DeviceDepartment](docs/DeviceDepartment.md)
 - [DeviceDepartmentList](docs/DeviceDepartmentList.md)
 - [DeviceDepartmentPlan](docs/DeviceDepartmentPlan.md)
 - [DeviceDepartmentPlanList](docs/DeviceDepartmentPlanList.md)
 - [DiscountValue](docs/DiscountValue.md)
 - [Domain](docs/Domain.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Extension](docs/Extension.md)
 - [Filter](docs/Filter.md)
 - [FilterCondition](docs/FilterCondition.md)
 - [Group](docs/Group.md)
 - [HostingInfo](docs/HostingInfo.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceItem](docs/InvoiceItem.md)
 - [InvoiceList](docs/InvoiceList.md)
 - [Ivr](docs/Ivr.md)
 - [IvrChoice](docs/IvrChoice.md)
 - [IvrFetch](docs/IvrFetch.md)
 - [IvrFetchParam](docs/IvrFetchParam.md)
 - [IvrStep](docs/IvrStep.md)
 - [MailAccount](docs/MailAccount.md)
 - [Message](docs/Message.md)
 - [MessageGroup](docs/MessageGroup.md)
 - [OkResponse](docs/OkResponse.md)
 - [PageVisit](docs/PageVisit.md)
 - [PaymentInfo](docs/PaymentInfo.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentProcessorType](docs/PaymentProcessorType.md)
 - [PhoneDevice](docs/PhoneDevice.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [PredefinedAnswer](docs/PredefinedAnswer.md)
 - [Setting](docs/Setting.md)
 - [Sla](docs/Sla.md)
 - [SlaBusinessHours](docs/SlaBusinessHours.md)
 - [SlaHistory](docs/SlaHistory.md)
 - [SlaValues](docs/SlaValues.md)
 - [StopReason](docs/StopReason.md)
 - [StoredFile](docs/StoredFile.md)
 - [Subscription](docs/Subscription.md)
 - [Tag](docs/Tag.md)
 - [Ticket](docs/Ticket.md)
 - [TicketAttribute](docs/TicketAttribute.md)
 - [TicketHistory](docs/TicketHistory.md)
 - [TicketInformation](docs/TicketInformation.md)
 - [TicketListItem](docs/TicketListItem.md)
 - [TicketPostpone](docs/TicketPostpone.md)
 - [TicketSla](docs/TicketSla.md)
 - [TicketUpdatable](docs/TicketUpdatable.md)
 - [Token](docs/Token.md)
 - [Upgrade](docs/Upgrade.md)
 - [UsageData](docs/UsageData.md)
 - [User](docs/User.md)
 - [Variation](docs/Variation.md)
 - [VariationUpgrade](docs/VariationUpgrade.md)
 - [VariationUpgrades](docs/VariationUpgrades.md)
 - [ApiKeyWithPrivileges](docs/ApiKeyWithPrivileges.md)
 - [BanListItem](docs/BanListItem.md)
 - [Company](docs/Company.md)
 - [Contact](docs/Contact.md)


## Documentation For Authorization


## apikey

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: HTTP header

## privileges

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: 
- **Scopes**: 
 - **invoice.read**: Read invoices
 - **subscription.own**: Read/write own subscriptions (use 'me' as subscriptionId)
 - **subscription.read**: Subscriptions read
 - **subscription.write**: Subscriptions write
 - **hosted_account.read**: Hosted account read
 - **hosted_account.write**: Hosted account write
 - **call.write**: Call write
 - **call.read**: Call read
 - **agent.read**: Agent read
 - **agent.write**: Agent write
 - **agent_status.read**: Agent status read
 - **phone.read**: Read all phones
 - **phone.write**: Write all phones
 - **phone.own**: Read/write phones available to me
 - **phone_number.read**: Read all phone numbers
 - **phone_number.own**: Read phone numbers available to me
 - **phone_number.write**: Write all phone numbers
 - **user.read**: Read all contacts
 - **user.write**: Write contact
 - **file.add**: Upload files
 - **hosting.login**: agent login
 - **tag.read**: Read tags
 - **tag.write**: Modify tags
 - **canned_message.read**: Read canned messages
 - **canned_message.write**: Modify canned messages
 - **predefined_answer.read**: Read predefined answer
 - **predefined_answer.write**: Modify predefined answer
 - **agent_phone.read**: Read agent phone device assigments
 - **agent_phone.write**: Change agent phone device assigments
 - **agent_phone.own**: Change my own phone device assigments
 - **conversation.create**: Create new conversation
 - **api.read**: Read api
 - **api.write**: Modify api
 - **api.delete**: Delete api keys
 - **ticket.read**: Ticket read
 - **ticket.write**: Ticket write
 - **device.read**: Device read
 - **device.write**: Device write
 - **sla.read**: Read sla
 - **extension.own**: Read/Write own extensions
 - **extension.write**: Write extension
 - **extension.read**: Read extension
 - **contact_phone.read**: Read contact phone
 - **chats.read**: Read chats
 - **settings.read**: Read ban
 - **settings.write**: Write ban
 - **page_visit.read**: Read page visits
 - **page_visit.write**: Write page visits
 - **mail_account.read**: Read mail_account


## Author

support@qualityunit.com

