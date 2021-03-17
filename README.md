# ZIA-API-Connector

A Python Zscaler Internet Access (ZIA) API REST Client. Refer to official Zscaler documentation
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
|URL|Method|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|/status|GET|Yes|client.activation.get_status||
|/status/activate|POST|Yes|client.activation.activate_changes||

### Admin Audit Logs
|URL|Method|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|/auditlogEntryReport|GET|Yes|
|/auditlogEntryReport|POST|Yes|
|/auditlogEntryReport|DELETE|Yes|
|/auditlogEntryReport/download|GET|Yes|

### Admin & Role Managent
|URL|Method|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|/adminRoles/lite|GET|Yes|
|/adminUsers|GET|Yes|
|/adminUsers|POST|Yes|
|/adminUsers/{userId}|PUT|Yes|
|/adminUsers/{userId}|DELETE|Yes|

### API Authentication
|URL|Method|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|/authenticadtedSession|GET|Yes|
|/authenticadtedSession|POST|Yes|client.session.ZIAConnector.login||
|/authenticadtedSession|DELETE|Yes|client.session.ZIAConnector.logout||

### Cloud Sandbox Report
|URL|Method|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|/sandbox/report/quota|GET|No|
|/sandbox/report/{md5Hash}|GET|No|

### Firewall Policies
|Method|URL|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
GET|/firewallFilteringRules|No|
GET|/firewallFilteringRules/{ruleId}|No|
GET|/ipDestinationGroups|No|
GET|/ipDestinationGroups/lite|No|
GET|/ipDestinationGroups/{ipGroupId}|No|
GET|/ipSourceGroups|No|
GET|/ipSourceGroups/lite|No|
GET|/ipSourceGroups/{ipGroupId}|No|
GET|/networkApplicationGroups|No|
GET|/networkApplicationGroups/lite|No|
GET|/networkApplicationGroups/{groupId}|No|
GET|/networkApplications|No|
GET|/networkApplications/{appId}|No|
GET|/networkServiceGroups|No|
GET|/networkServiceGroups/lite|No|
GET|/networkServiceGroups/{serviceGroupId}|No|
GET|/networkServices|No|
GET|/networkServices/lite|No|
GET|/networkServices/{serviceid}|No|
GET|/timeWindows|No|
GET|/timeWindows/lite|No|

### Location Management
|Method|URL|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|GET|/locations|Yes|client.locations.search_locations||
|POST|/locations|Yes|client.locations.create_location||
|POST|/locations/bulkDelete|No|
|GET|/locations/lite|Yes|client.locations.get_location_ids||
|GET|/locations/{locationId}|Yes|client.locations.get_location_info||
|PUT|/locations/{locationId}|Yes|client.locations.update_location||
|DELETE|/locations/{locationId}|Yes|client.locations.delete_location||
|GET|/locations/{locationId}/sublocations|Yes|client.locations.get_sublocations||

### Security Policy Settings
|Method|URL|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|GET|/security|No|
|PUT|/security|No|
|GET|/security/advanced|No|
|PUT|/security/advanced|No|
|POST|/security/advanced/blacklistUrls|No|

### SSL Inspection Settings
|Method|URL|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|GET|/sslSettings/downloadcsr|No|
|POST|/sslSettings/generatecsr|No|
|GET|/sslSettings/showcert|No|
|POST|/sslSettings/uploadcert/text|No|
|POST|/sslSettings/uploadcertchain/text|No|
|DELETE|/sslSettings/certchain|No|
|GET|/sslSettings/exemptedUrls|No|
|POST|/sslSettings/exemptedUrls|No|

### Traffic Forwarding
|Method|URL|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|GET|/vpnCredentials|Yes|client.traffic_forwarding.get_vpn_creds||
|POST|/vpnCredentials|No|
|POST|/vpnCredentials/bulkDelete|No|
|GET|/vpnCredentials/{vpnId}|No|
|PUT|/vpnCredentials/{vpnId}|No|
|DELETE|/vpnCredentials/{vpnId}|Yes|client.traffic_forwarding.del_vpn_creds||
|GET|/orgProvisioning/ipGreTunnelInfo|Yes|client.traffic_forwarding.ip_gre_tunnel_info||
|GET|/vips|Yes|client.traffic_forwarding.get_virtual_ips||

### User Management
|Method|URL|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|GET|/departments|Yes|client.users.get_departments||
|GET|/departments/{id}|Yes|client.users.get_department||
|GET|/groups|Yes|client.users.get_groups||
|GET|/groups/{groupId}|No|
|GET|/users|Yes|client.users.get_users||
|POST|/users|No|
|POST|/users/bulkDelete|No|
|GET|/users/{userId}|Yes|client.users.get_user_info||
|PUT|/users/{userId}|Yes|client.users.update_user||
|DELETE|/users/{userId}|No|

### URL Categories
|Method|URL|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|GET|/urlCategories|No|
|POST|/urlCategories|No|
|GET|/urlCategories/lite|No|
|GET|/urlCategories/urlQuota|No|
|GET|/urlCategories/{categoryId}|No|
|PUT|/urlCategories/{categoryId}|No|
|DELETE|/urlCategories/{categoryId}|No|
|POST|/urlLookup|No|

### URL Filtering Policies
|Method|URL|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|GET|/urlFilteringRules|No|
|POST|/urlFilteringRules|No|
|GET|/urlFilteringRules/{ruleId}|No|
|PUT|/urlFilteringRules/{ruleId}|No|
|DELETE|/urlFilteringRules/{ruleId}|No|

### User Authentication Settings
|Method|URL|Implemented|Function/Method|Script Parser|
|---|---|---|---|---|
|GET|/authSettings/exemptedUrls|No|
|POST|/authSettings/exemptedUrls|No|

