# ZIA-API-Connector

A Python Zscaler Internet Access (ZIA) API REST Client. Refer to official Zscaler documentation
[here](https://help.zscaler.com/zia/api-developers-guide).

## Implemented API calls
All available API calls that can be made are listed in 
[Zscaler's API reference](https://help.zscaler.com/zia/api-developers-guide).

I've recollected them and summarized them in the following table:

### Activation
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### Admin Audit Logs
|URL|Method|Implemented|
|---|---|---|
|/auditlogEntryReport|GET|Yes|
|/auditlogEntryReport|POST|Yes|
|/auditlogEntryReport|DELETE|Yes|
|/auditlogEntryReport/download|GET|Yes|


### Admin & Role Managent
|URL|Method|Implemented|
|---|---|---|
|/adminRoles/lite|GET|Yes|
|/adminUsers|GET|Yes|
|/adminUsers|POST|Yes|
|/adminUsers/{userId}|PUT|Yes|
|/adminUsers/{userId}|DELETE|Yes|


### API Authentication
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### Cloud Sandbox Report
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### Firewall Policies
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### Location Management
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### Security Policy Settings
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### SSL Inspection Settings
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### Traffic Forwarding
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### User Management
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### URL Categories
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### URL Filtering Policies
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|

### User Authentication Settings
|URL|Method|Implemented|
|---|---|---|
|/satus|GET|Yes|
|/satus/activate|POST|Yes|
