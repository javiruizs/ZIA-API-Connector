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
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/status|Yes|activation.get_status|`--pending`|
|POST|/status/activate|Yes|activation.activate_changes|`--apply`|

### Admin Audit Logs
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/auditlogEntryReport|Yes|audit_log.get_auditlog_entry_report_status||
|POST|/auditlogEntryReport|Yes|audit_log.req_auditlog_entry_report||
|DELETE|/auditlogEntryReport|Yes|audit_log.cncl_auditlog_entry_report||
|GET|/auditlogEntryReport/download|Yes|audit_log.dwl_auditlog_entry_report||

### Admin & Role Managent
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/adminRoles/lite|Yes|admin_roles.get_admin_roles||
|GET|/adminUsers|Yes|admin_roles.get_admin_users||
|POST|/adminUsers|Yes|admin_roles.create_admin_user||
|PUT||/adminUsers/{userId}Yes|admin_roles.update_admin_user||
|DELETE|/adminUsers/{userId}|Yes|admin_roles.delete_admin_user||

### API Authentication
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/authenticadtedSession|Yes|session.ZIAConnector.is_session_active||
|POST|/authenticadtedSession|Yes|session.ZIAConnector.login||
|DELETE|/authenticadtedSession|Yes|session.ZIAConnector.logout||

### Cloud Sandbox Report
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/sandbox/report/quota|Yes|sandbox.get_sandbox_quota||
|GET|/sandbox/report/{md5Hash}|Yes|sandbox.get_sandbox_file_report||
### Firewall Policies
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

### Location Management - `locs` subparser
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/locations|Yes|locations.search_locations|`search`|
|POST|/locations|Yes|locations.create_location|`create`|
|POST|/locations/bulkDelete|Yes|locations.bulk_del_location|`bulkdel`|
|GET|/locations/lite|Yes|locations.get_location_ids|`ids`|
|GET|/locations/{locationId}|Yes|locations.get_location_info|`info`|
|PUT|/locations/{locationId}|Yes|locations.update_location|`update`|
|DELETE|/locations/{locationId}|Yes|locations.delete_location|`delete`|
|GET|/locations/{locationId}/sublocations|Yes|locations.get_sublocations|`sublocs`|

### Security Policy Settings
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/security|No|
|PUT|/security|No|
|GET|/security/advanced|No|
|PUT|/security/advanced|No|
|POST|/security/advanced/blacklistUrls|No|

### SSL Inspection Settings
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
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/vpnCredentials|Yes|traffic_forwarding.get_vpn_creds||
|POST|/vpnCredentials|Yes|traffic_forwarding.add_vpn_creds||
|POST|/vpnCredentials/bulkDelete|Yes|traffic_forwarding.bulk_del_vpn_creds||
|GET|/vpnCredentials/{vpnId}|Yes|traffic_forwarding.get_vpn_cred_info||
|PUT|/vpnCredentials/{vpnId}|Yes|traffic_forwarding.upd_vpn_cred||
|DELETE|/vpnCredentials/{vpnId}|Yes|traffic_forwarding.del_vpn_cred||
|GET|/orgProvisioning/ipGreTunnelInfo|Yes|traffic_forwarding.ip_gre_tunnel_info||
|GET|/vips|Yes|traffic_forwarding.get_virtual_ips||

### User Management - `users` subparser
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/departments|Yes|users.get_departments|`depts`|
|GET|/departments/{id}|Yes|users.get_department|`deptinfo`|
|GET|/groups|Yes|users.get_groups|`groups`|
|GET|/groups/{groupId}|Yes|users.get_group_info|`groupinfo`|
|GET|/users|Yes|users.get_users|`search`|
|POST|/users|Yes|users.create_user|`create`|
|POST|/users/bulkDelete|Yes|users.bulk_del_user|`bulkdel`|
|GET|/users/{userId}|Yes|users.get_user_info|`info`|
|PUT|/users/{userId}|Yes|users.update_user|`update`|
|DELETE|/users/{userId}|Yes|users.del_user|`delete`|

### URL Categories
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
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/urlFilteringRules|No|
|POST|/urlFilteringRules|No|
|GET|/urlFilteringRules/{ruleId}|No|
|PUT|/urlFilteringRules/{ruleId}|No|
|DELETE|/urlFilteringRules/{ruleId}|No|

### User Authentication Settings
|Method|URL|Implemented|Function/Method|Sub-subparser|
|:---:|:---:|:---:|:---:|:---:|
|GET|/authSettings/exemptedUrls|Yes|user_auth.get_exempted_auth_urls||
|POST|/authSettings/exemptedUrls|Yes|user_auth.mod_auth_urls_exemptions||

