# ZIA-API-Connector

A Python Zscaler Internet Access (ZIA) API REST client. Refer to official Zscaler documentation
[here](https://help.zscaler.com/zia/api-developers-guide).

## Introduction
I've been building all this code for over a year now while I was working with ZIA installations of different customers 
for which the company I worked for, worked with. I mainly did this because I wanted to automatize recurring tasks 
that would take a long time if done manually.

My philosophy has been to create a module for every functionality group found on
[Zscaler's API reference](https://help.zscaler.com/zia/api-developers-guide).
Then, create a dedicated subparser (using `argparse`) with its subcommands for every API call in the `api_parser` 
package that would map command-line arguments to function argumnets.

The kind of tasks I had to fulfill were always about location and user management. That's where I can most confidently
assure you that the code works. For the rest that has been implemented, I have done very little to no testing at all.
I simply had no time for it, nor will have time from the date I last edited this README on. Feel free to fork this repo
or mail me in case you had any suggestions or wanted to improve my work.


## Usage

You have two options here. If your intentions are to work with locations, users and traffic forwarding, you can go ahead
and use the script named `ziaclient.py`.

If you want to use something else, perhaps I had the time to create a module dedicated to it, which you may find in the
`zia_client` package. If you're lucky, and that's the case, you can create a `ZIAConnector()` object and use the modules
and their functions.

### Script
You can get full usage documentation by creating it with Sphinx as mentioned [below](#build-documentation), or you can
discover what it can do by using the `-h`or `--help` arguments on every subcommand or subparser.

Please note that the keyword arguments prior to specifying the subparser can always be used.

### Built functionalities

I've kept track of everything I have implemented in the section [Implemented API calls](#implemented-api-calls).
If there's a 'Yes' in the 'Implemented' column, then there's a method for that call. But, remember, it may have not been
tested or ever used.

If there's something written in the 'Subparser' column, there's a specific subparser/subcommand in the script for that
functionality.

## Required packages and modules 

Theres's a conda YAML environment file for Windows. Use it to create one if you like with the following command,
although you might not need it.

```powershell
conda env create -f environment.yml
```

## Build documentation

Build the documentation with Sphinx by running: `make html` or `make latexpdf` in the **docs** folder.

HTML page will be found at `docs/_build/html/index.html`; PDF document at `docs/_build/latex/idontknowthename.pdf`.

I've used some Sphinx extensions, so perhaps you may need to install them if you don't create an environment from the
YAML file.

## Future improvements

If I ever had the time or would work with this tool again, here you are some of the things I would try to improve:
* Import the module's methods inside the connector's class and privatize the modules, so the methods could be called as
  members of the connector.
    
* Handle rates as described [here](https://help.zscaler.com/zia/about-rate-limiting) and
  [here](https://help.zscaler.com/zia/api-rate-limit-summary).

* Handle error codes as described [here](https://help.zscaler.com/zia/about-error-handling).

* Beautify documentation.

* Test every method thoroughly.


## Implemented API calls
All available API calls that can be made are listed in 
[Zscaler's API reference](https://help.zscaler.com/zia/api-developers-guide).

I've recollected them and summarized them in the following tables:

### Activation
* Module in `zia_client` package: Defined in root package.
* Subparser: Arguments in root parser

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/status|Yes|ZIAConnector().get_status|`--pending`|
|POST|/status/activate|Yes|ZIAConnector().activate_changes|`--apply_after`|

### Admin Audit Logs
* Module in `zia_client` package: `audit_log`
* Subparser: TODO

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/auditlogEntryReport|Yes|get_auditlog_entry_report_status||
|POST|/auditlogEntryReport|Yes|req_auditlog_entry_report||
|DELETE|/auditlogEntryReport|Yes|cncl_auditlog_entry_report||
|GET|/auditlogEntryReport/download|Yes|dwl_auditlog_entry_report||

### Admin & Role Managent
* Module in `zia_client` package: `admin_roles`
* Subparser: TODO

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/adminRoles/lite|Yes|get_admin_roles||
|GET|/adminUsers|Yes|get_admin_users||
|POST|/adminUsers|Yes|create_admin_user||
|PUT|/adminUsers/{userId}|Yes|update_admin_user||
|DELETE|/adminUsers/{userId}|Yes|delete_admin_user||

### API Authentication
* Module in `zia_client` package: Defined in root package.
* Subparser: Not needed.

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/authenticadtedSession|Yes|ZIAConnector().is_session_active|Not Needed.|
|POST|/authenticadtedSession|Yes|ZIAConnector().login|Not Needed.|
|DELETE|/authenticadtedSession|Yes|ZIAConnector().logout|Not Needed.|

### Cloud Sandbox Report
* Module in `zia_client` package: `sandbox`
* Subparser: TODO

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/sandbox/report/quota|Yes|get_sandbox_quota||
|GET|/sandbox/report/{md5Hash}|Yes|get_sandbox_file_report||

### Firewall Policies
* Module in `zia_client` package: None.
* Subparser: None.

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/firewallFilteringRules|No|
|GET|/firewallFilteringRules/{ruleId}|No|
|GET|/ipDestinationGroups|No|
|GET|/ipDestinationGroups/lite|No|
|GET|/ipDestinationGroups/{ipGroupId}|No|
|GET|/ipSourceGroups|No|
|GET|/ipSourceGroups/lite|No|
|GET|/ipSourceGroups/{ipGroupId}|No|
|GET|/networkApplicationGroups|No|
|GET|/networkApplicationGroups/lite|No|
|GET|/networkApplicationGroups/{groupId}|No|
|GET|/networkApplications|No|
|GET|/networkApplications/{appId}|No|
|GET|/networkServiceGroups|No|
|GET|/networkServiceGroups/lite|No|
|GET|/networkServiceGroups/{serviceGroupId}|No|
|GET|/networkServices|No|
|GET|/networkServices/lite|No|
|GET|/networkServices/{serviceid}|No|
|GET|/timeWindows|No|
|GET|/timeWindows/lite|No|

### Location Management
* Module in `zia_client` package: `activation`
* Subparser: `locs`

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/locations|Yes|search_locations|`search`|
|POST|/locations|Yes|create_location|`create`|
|POST|/locations/bulkDelete|Yes|bulk_del_location|`bulkdel`|
|GET|/locations/lite|Yes|get_location_ids|`ids`|
|GET|/locations/{locationId}|Yes|get_location_info|`info`|
|PUT|/locations/{locationId}|Yes|update_location|`update`|
|DELETE|/locations/{locationId}|Yes|delete_location|`delete`|
|GET|/locations/{locationId}/sublocations|Yes|get_sublocations|`sublocs`|

### Security Policy Settings
* Module in `zia_client` package: None.
* Subparser: None.

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/security|No|
|PUT|/security|No|
|GET|/security/advanced|No|
|PUT|/security/advanced|No|
|POST|/security/advanced/blacklistUrls|No|

### SSL Inspection Settings
* Module in `zia_client` package: `activation`
* Subparser: Arguments in root parser

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/sslSettings/downloadcsr|No|
|POST|/sslSettings/generatecsr|No|
|GET|/sslSettings/showcert|No|
|POST|/sslSettings/uploadcert/text|No|
|POST|/sslSettings/uploadcertchain/text|No|
|DELETE|/sslSettings/certchain|No|
|GET|/sslSettings/exemptedUrls|No|
|POST|/sslSettings/exemptedUrls|No|

### Traffic Forwarding
* Module in `zia_client` package: `traffic`
* Subparser: Arguments in root parser

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/vpnCredentials|Yes|get_vpn_creds||
|POST|/vpnCredentials|Yes|add_vpn_creds||
|POST|/vpnCredentials/bulkDelete|Yes|bulk_del_vpn_creds||
|GET|/vpnCredentials/{vpnId}|Yes|get_vpn_cred_info||
|PUT|/vpnCredentials/{vpnId}|Yes|upd_vpn_cred||
|DELETE|/vpnCredentials/{vpnId}|Yes|del_vpn_cred||
|GET|/orgProvisioning/ipGreTunnelInfo|Yes|ip_gre_tunnel_info||
|GET|/vips|Yes|get_virtual_ips||

### User Management
* Module in `zia_client` package: `users`
* Subparser: `users`

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/departments|Yes|get_departments|`depts`|
|GET|/departments/{id}|Yes|get_department|`deptinfo`|
|GET|/groups|Yes|get_groups|`groups`|
|GET|/groups/{groupId}|Yes|get_group_info|`groupinfo`|
|GET|/users|Yes|get_users|`search`|
|POST|/users|Yes|create_user|`create`|
|POST|/users/bulkDelete|Yes|bulk_del_user|`bulkdel`|
|GET|/users/{userId}|Yes|get_user_info|`info`|
|PUT|/users/{userId}|Yes|update_user|`update`|
|DELETE|/users/{userId}|Yes|del_user|`delete`|

### URL Categories
* Module in `zia_client` package: None.
* Subparser: None.

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/urlCategories|No|
|POST|/urlCategories|No|
|GET|/urlCategories/lite|No|
|GET|/urlCategories/urlQuota|No|
|GET|/urlCategories/{categoryId}|No|
|PUT|/urlCategories/{categoryId}|No|
|DELETE|/urlCategories/{categoryId}|No|
|POST|/urlLookup|No|

### URL Filtering Policies
* Module in `zia_client` package: None.
* Subparser: None.

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/urlFilteringRules|No|
|POST|/urlFilteringRules|No|
|GET|/urlFilteringRules/{ruleId}|No|
|PUT|/urlFilteringRules/{ruleId}|No|
|DELETE|/urlFilteringRules/{ruleId}|No|

### User Authentication Settings
* Module in `zia_client` package: `user_auth`
* Subparser: TODO

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/authSettings/exemptedUrls|Yes|get_exempted_auth_urls||
|POST|/authSettings/exemptedUrls|Yes|mod_auth_urls_exemptions||

