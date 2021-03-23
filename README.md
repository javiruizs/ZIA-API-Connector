# ZIA-API-Connector

A Python Zscaler Internet Access (ZIA) API REST  Refer to official Zscaler documentation
[here](https://help.zscaler.com/zia/api-developers-guide).

## Script

### Usage

### Built functionalities

See section [Implemented API calls](#implemented-api-calls).

## Required packages and modules 

Theres's a conda YAML environment file for Windows. Use it to create one if you like with the following command,
although you might not need it.

```powershell
conda env create -f environment.yml
```

## Build documentation

Run:
```powershell
cd docs
make html
```

Open `docs/_build/html/index.html` on your browser.


## Implemented API calls
All available API calls that can be made are listed in 
[Zscaler's API reference](https://help.zscaler.com/zia/api-developers-guide).

I've recollected them and summarized them in the following table:

### Activation
* Module in `zia_client` package: `activation`
* Subparser: Arguments in root parser

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/status|Yes|activation.get_status|`--pending`|
|POST|/status/activate|Yes|activation.activate_changes|`--apply`|

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
|PUT||/adminUsers/{userId}|Yes|update_admin_user||
|DELETE|/adminUsers/{userId}|Yes|delete_admin_user||

### API Authentication
* Module in `zia_client` package: Defined in root package.
* Subparser: TODO

|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/authenticadtedSession|Yes|ZIAConnector().is_session_active||
|POST|/authenticadtedSession|Yes|ZIAConnector().login||
|DELETE|/authenticadtedSession|Yes|ZIAConnector().logout||

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

