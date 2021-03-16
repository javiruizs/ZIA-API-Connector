"""
Class that encapsulates the session management while connecting to the Zscaler ZIA API. For each of the references that
 exist (see https://help.zscaler.com/zia/api), I will try to create a specific method. Also, I'll try to create methods
that will apply on the general use that I will make of it.
"""

import json
import sys
import time

import requests as re
from dateutil import parser

import utils as u
from .exceptions import ResponseException


class ZIAConnector:
    """Specific connector for the ZIA API. Every method represents
    in a general way all the possible actions that can be made.
    """

    def __init__(self, config_file, verbosity=None):
        """Constructor for the connector.
        It only loads the configuration from the file.
        In future it may also log in.

        Args:
            config_file (String): The path for the config file. Must be a JSON.
        """
        self.s = None
        with open(config_file) as f:
            config = json.load(f)

        self.urls = config['urls']

        self.creds = config['creds']

        self.host = config['host'] + config['api_uri']

        self.retries = config['retries']

        self.debug = False if 'debug' not in config else config['debug']

        self.verbosity = config['verbosity'] if not verbosity else verbosity

        self.sleep_time = config['sleep']

        # Setting default
        sys.excepthook = self.my_except_hook

    def login(self):
        """Logs in. Please, make sure you've put the correct
        username, password and API key in the config file.

        Raises:
            Exception: If login was not successful.
        """

        headers = {
            'content-type': 'application/json',
            'cache-control': 'no-cache',
        }

        timestamp, key = u.obfuscate_api_key(self.creds['key'])

        content = {
            "apiKey": key,
            "username": self.creds['username'],
            "password": self.creds['password'],
            "timestamp": timestamp
        }

        url = self.form_full_url('loginout')

        self.s = re.Session()

        self.s.headers = headers

        req = re.Request('POST', url, json=content)

        return self.send_recv(req, successful_msg='Login successful.')

    def logout(self):
        """
        Logs out and closes session.
        Returns: Nothing.

        """
        url = self.form_full_url('loginout')

        req = re.Request('DELETE', url)

        return self.send_recv(req, successful_msg='Logout successful.')

    ##############################
    # VPN RELATED FUNCTIONS #
    ##############################

    def get_vpn_creds(self):
        """Obtains the list of the existing VPN credentials in the platform.

        Raises:
            Exception: If the information retrieval was not possible.
        """

        url = self.form_full_url('vpnCreds')

        req = re.Request('GET', url)

        return self.send_recv(req, successful_msg='Obtaining VPN credentials successful.')

    def del_vpn_creds(self, vpn_id):
        """
        Delete VPN credentials.
        Args:
            vpn_id: Credential identifier.

        Returns: JSON response.

        """
        url = self.form_full_url('vpn_credentials', [vpn_id])

        req = re.Request('DELETE', url)

        return self.send_recv(req, successful_msg=f'VPN credential with id {vpn_id} removed successfully.')

    ##############################
    # LOCATION RELATED FUNCTIONS #
    ##############################

    def create_location(self, location):
        """Creates the location.

        Args:
            location (String): A dictionary representing the location. See example.
        """

        url = self.form_full_url('locs')

        req = re.Request('POST', url, json=location)

        return self.send_recv(req, successful_msg=f'Location {location["name"]} was successfully added.')

    def update_location(self, location):
        """Updates an existing location.

        Args:
            location (dict): The location information in dict format.
        """

        # Check if the locations data contains it's id.
        if 'id' not in location:
            raise ValueError('There is no "id" keyword in the location dict.')

        url = self.form_full_url('locs', [location["id"]])

        time.sleep(0.5)
        r = re.Request('PUT', url, json=location)

        return self.send_recv(r, successful_msg=f'Location {location["id"]} was successfully updated.')

    def delete_location(self, loc_id: int):
        """Deletes location given its id.

        Args:
            loc_id (int): Location identifier.

        Raises:
            Exception: If delete is unsuccessful, then it raises an exception.
        """
        url = self.form_full_url('locs', [loc_id])

        r = re.Request('DELETE', url)

        return self.send_recv(r, successful_msg=f'Location {loc_id} deleted successfully')

    def search_locations(self, search="", sslScanEnabled=None, xffEnabled=None, authRequired=None, bwEnforced=None,
                         page=None, pageSize=None, full=False):
        """Retrieves all the locations, not sub-locations that match the search.
        Could be IP address or name.

        Args:
            full: Enables a loop to retrieve all information.
            search (str, optional): The search string used to partially match against a location's name and port
                attributes. Defaults to "".
            sslScanEnabled (bool, optional): Filter based on whether the Enable SSL Scanning setting is enabled or
                disabled for a location. Defaults to None.
            xffEnabled (bool, optional): Filter based on whether the Enforce XFF Forwarding setting is enabled or
                disabled for a location. Defaults to None.
            authRequired (bool, optional): Filter based on whether the Enforce Authentication setting is enabled or
                disabled for a location. Defaults to None.
            bwEnforced (bool, optional): Filter based on whether Bandwidth Control is being enforced for a location.
                Defaults to None.
            page (int, optional): Specifies the page offset. Defaults to 1.
            pageSize (int, optional): Specifies the page size. The default size is 100, but the maximum size is 1000.
                Defaults to 100.
        """
        # Use directly args of this function as parameters on the request, but they need to be cleaned first.
        params = u.clean_args(locals())

        url = self.form_full_url('locs')

        # Key all is not recognized by the API, therefore can be removed

        return self.full_retrieval('GET', url, params, {}, 1000, "Location search successful.", full)

    def get_location_ids(self, includeSubLocations=None, includeParentLocations=None, authRequired=None,
                         bwEnforced=None, sslScanEnabled=None, xffEnabled=None, search="", page=None, pageSize=None,
                         full=False):
        """
        Gets a name and ID dictionary of locations.
        Args:
            xffEnabled (bool): Filter based on whether the Enforce XFF Forwarding setting is enabled or disabled for a
            location.
            bwEnforced (bool): Filter based on whether Bandwidth Control is being enforced for a location.
            authRequired (bool): Filter based on whether the Enforce Authentication setting is enabled or disabled for a
            location.
            full: If set to True, all location IDs will be obtained.
            includeSubLocations (bool, optional): if set to true sub-locations will be included in the response
            otherwise they will excluded. Defaults to False.
            includeParentLocations (bool, optional): if set to true locations with sub locations will be included in the
            response, otherwise only locations without sub-locations are included. Defaults to False.
            sslScanEnabled (bool, optional): Filter based on whether the Enable SSL Scanning setting is enabled or
            disabled for a location. Defaults to False.
            search (str, optional): The search string used to partially match against a location's name and port
            attributes. Defaults to "".
            page (int, optional): Specifies the page offset. Defaults to 1.
            pageSize (int, optional): Specifies the page size. The default size is 100, but the maximum size is 1000.
            Defaults to 100.

        Raises:
            Exception: There was some error in the retrieval.

        Returns:
            JSON dict: Name and ID mapping
        """

        # Use directly args of this function as parameters on the request, but they need to be cleaned first.
        args = locals()
        params = u.clean_args(args)
        params = None if not params else params

        url = self.form_full_url('locInfo')

        return self.full_retrieval('GET', url, params, {}, pageSize, "Location ids retrieval successful.", full)

    def get_location_info(self, loc_id):
        """Returns all the information of the desired location.

        Args:
            loc_id (int): Location identifier

        Returns:
            dict: A dict containing all the information. If no success, dict is empty.
        """
        url = self.form_full_url('locs', [loc_id])

        r = re.Request('GET', url)
        time.sleep(1)

        return self.send_recv(r, f'Location info for {loc_id} has been successfully retrieved.')

    def get_sublocations(self, locationId, search="", sslScanEnabled=None, xffEnabled=None, authRequired=None,
                         bwEnforced=None, enforceAup=None, enableFirewall=None):
        """
        Gets the sub-location information for the location with the specified ID. These are the sub-locations associated
        to the parent location.
        Args:
            locationId: The unique identifier for the location. The sub-location information given is based on the
            parent location's ID.
            search (str, optional): The search string used to partially match against a location's name and port
            attributes. Defaults to "".
            sslScanEnabled (bool, optional): Filter based on whether the Enable SSL Scanning setting is enabled or
            disabled for a location. Defaults to None.
            xffEnabled (bool, optional): Filter based on whether the Enforce XFF Forwarding setting is enabled or
            disabled for a location. Defaults to None.
            authRequired (bool, optional): Filter based on whether the Enforce Authentication setting is enabled or
            disabled for a location. Defaults to None.
            bwEnforced (bool, optional): Filter based on whether Bandwidth Control is being enforced for a location.
            Defaults to None.
            enforceAup: Filter based on whether Enforce AUP setting is enabled or disabled for a sub-location.
            enableFirewall: Filter based on whether Enable Firewall setting is enabled or disabled for a sub-location.

        Returns:
            A list of dictionaries.
        """

        url = self.form_full_url('locs', [locationId, 'sublocations'])

        # Use directly args of this function as parameters on the request, but they need to be cleaned first.
        args = locals()
        params = u.clean_args(args)

        return self.full_retrieval('GET', url, params, {}, 0, f"Sublocations for {locationId} obtained successfully.",
                                   False)

    ######################################
    # ADMIN MANAGEMENT RELATED FUNCTIONS #
    ######################################

    def get_admin_roles(self, includeAuditorRole=None, includePartnerRole=None):
        """Obtains the administrator roles and their ids.

        Args:
            includeAuditorRole (boolean): If True, includes auditor roles in the results.
            includePartnerRole (boolean): If True, includes partner roles in the results.

        Returns:
            dict: A dict containing the information regarding the roles: id, rank, name and role type.
        """

        url = self.form_full_url('adminRoles')

        r = re.Request('GET', url, params=u.clean_args(locals()))

        return self.send_recv(r, successful_msg="Admin roles retrieval successful.")

    def get_admin_users(self, includeAuditorUsers=False, includeAdminUsers=True, search: str = "", page=None,
                        pageSize=None, full=False):
        """Obtains the list containing all the admin users.

        Args:
            full: If set to True, all admin users will be retrieved.
            includeAuditorUsers (bool, optional): Includes auditor users. Defaults to False.
            includeAdminUsers (bool, optional): Includes admin users. Defaults to True.
            search (str, optional): The search string used to partially match against an admin/auditor user's Login ID
                or Name. Defaults to "".
            page (int, optional): Specifies the page offset. Defaults to 1.
            pageSize (int, optional): Specifies the page size. The default size is 100, but the maximum size is 1000.
                Defaults to 100.

        Returns:
            [type]: [description]
        """
        url = self.form_full_url("adminUsers")

        args = locals()
        params = u.clean_args(args)

        return self.full_retrieval('GET', url, params, {}, pageSize, "Admin usr retrieval successful.", full)

    def create_admin_user(self, userinfo):
        """Creates the user with the information contained in userinfo.

        Args:
            userinfo (JSON dict): A dictionary containing the user information.

        Returns:
            JSON dict: The created JSON dict representing the new user with all other information.
        """

        url = self.form_full_url("adminUsers")

        r = re.Request('POST', url, json=userinfo)

        return self.send_recv(r, f"Admin user '{userinfo['loginName']}' created successfully.")

    def update_admin_user(self, userinfo):
        """Updates the information of an existing admin user.

        Args:
            userinfo (JSON dict): The updated JSON representation of the user.

        Returns:
            JSON dict: The representation of the updated user as confirmation.
        """

        url = self.form_full_url("adminUsers", [userinfo['userId']])

        r = re.Request('PUT', url, json=userinfo)

        return self.send_recv(r, f"Admin user {userinfo['userId']} updated success"
                                 f"fully.")

    def delete_admin_user(self, userId):
        """Deletes the desired user.

        Args:
            userId (int): The user ID.

        Returns:
            None: None-type should be returned.
        """
        url = self.form_full_url("adminUsers", [userId])

        r = re.Request('DELETE', url)

        return self.send_recv(r, f"Successfully deleted admin user: {userId}.")

    #################################
    # STATUS AND CHANGES MANAGEMENT #
    #################################

    def get_status(self):
        """Gets the current status in the current session.
        Active means no changes must be activated. Otherwise, consider 
        calling method activate_changes() if you are not going to log off immediately
        afterwards.

        Raises:
            Exception: [description]
        """
        url = self.form_full_url('status')

        return self.send_recv(re.Request('GET', url), "Status obtained successfully.")

    def activate_changes(self):
        """Applies the changes that have been made.
        It is not necessary to call this method if you are going
        to log off.

        Raises:
            Exception: If the changes were not applied due to error.
        """
        url = self.form_full_url('activate')

        r = re.Request('POST', url)

        return self.send_recv(r, "Changes activated successfully.")

    ###################
    # USER MANAGEMENT #
    ###################
    def get_departments(self, search='', page=None, pageSize=None, full=False):
        """
        Obtains departments.
        Args:
            full: If set to true, all departments will be retrieved.
            search: Search string.
            page: Page offset.
            pageSize: Elements contained per page.

        Returns:
            List of dictionaries with depts.

        """
        url = self.form_full_url('depts')

        params = u.clean_args(locals())

        return self.full_retrieval('GET', url, params, {}, pageSize, "Departments retrieval successful.", full)

    def get_department(self, dept_id: int):
        """
        Gets department information from department id.
        Args:
            dept_id: Department id.

        Returns:
            JSON response.

        """
        url = self.form_full_url('dept', [dept_id])

        r = re.Request('GET', url)

        return self.send_recv(r, f'Information for department with id {dept_id} obtained successfully.')

    def get_groups(self, search="", page=None, pageSize=None, full=False):
        """
        Retrieves groups.
        Args:
            search (str): Search string. Name of the group.
            page (int): Page offset. Server's default is 1.
            pageSize (int): Page size. Server's default 100.
            full (bool): Default is False. If set to True, all information is returned.

        Returns:
            JSON response.

        """
        params = u.clean_args(locals())

        url = self.form_full_url('groups')

        return self.full_retrieval('GET', url, params, {}, pageSize, "Group retrieval successful.", full)

    def get_users(self, name="", dept="", group="", page=None, pageSize=None, full=False):
        """
        Gets a list of all users and allows user filtering by name, department, or group. The name search parameter
        performs a partial match. The dept and group parameters perform a 'starts with' match.
        Args:
            name (str): Filters by user name.
            dept (str): Filters by department name.
            group (str): Filters by group name.
            page (int): Defaults to 1. Specifies the page offset.
            pageSize (int): Defaults to 100. Specifies the page size.
            full (bool): Defaults to False. Set to True if complete search is wanted.

        Returns:
            JSON response.

        """
        url = self.form_full_url('usr')

        params = u.clean_args(locals())

        return self.full_retrieval('GET', url, params, {}, pageSize, "User retrieval successful.", full)

    def update_user(self, userdata):
        """
        Updates the user information for the specified ID. However, the "email" attribute is read-only.
        Args:
            userdata (dict): Dictionary that contains the user information.

        Returns:
            JSON response.

        """
        if 'id' not in userdata:
            raise ValueError('Userdata has no id key.')

        url = self.form_full_url('usr', [userdata['id']])

        r = re.Request('PUT', url, json=userdata)

        return self.send_recv(r, f"User {userdata['id']} update successful.")

    def get_user_info(self, usr_id):
        """
        Gets the user information for the specified ID.
        Args:
            usr_id (int): The unique identifer for the user.

        Returns:
            JSON dict with user's info.

        """
        url = self.form_full_url('usr', [usr_id])

        r = re.Request('GET', url)

        return self.send_recv(r, "User update successful.")

    #######################
    # AUDIT LOG FUNCTIONS #
    #######################

    def req_auditlog_entry_report(self, startTime: str, endTime: str, page=None, pageSize=500,
                                  actionTypes: list = False, category: str = "", subcategories: list = False,
                                  actionResult: str = "", actionInterface: str = "", objectName="", clientIP: str = "",
                                  adminName: str = "", targetOrgId: int = None, full=False):
        """
        Creates an audit log report for the specified time period and saves it as a CSV file. The report includes audit
        information for every call made to the cloud service API during the specified time period. Creating a new audit
        log report will overwrite a previously-generated report.

        Args:
            targetOrgId (int): Organization ID in case more than one organization were administrated.
            actionTypes (list of str): Action type for audit log entry. Recognized values:
                * SIGN_IN
                * SIGN_OUT
                * CREATE
                * UPDATE
                * DELETE
                * PATCH
                * AUDIT_OPERATION
                * ACTIVATE
                * FORCED_ACTIVATE,
                * IMPORT
                * REPORT
                * DOWNLOAD
            actionInterface (list of str): Action type for audit log entry.
            objectName: Object in question.
            full: If set to true, full retrieval.
            page: Page in offset.
            pageSize: Offset. (Maximal accepted for this action is 500)
            startTime: Start date of the admin's last login. Input should be of format 'YYYY-mm-dd HH:MM:SS TZ' or
                'YYYY-mm-dd HH:MM:SS', as in '2021-02-01 12:21:23 UTC+1'.
            endTime: End date of the admin's last logout. Input should be of format 'YYYY-mm-dd HH:MM:SS TZ' or
                'YYYY-mm-dd HH:MM:SS', as in '2021-02-01 12:21:23 UTC+1'.
            category: The location in the Zscaler Admin Portal (i.e., Admin UI) where the actionType was performed.
                (https://help.zscaler.com/zia/about-audit-logs#category)
            subcategories: The area within a category where the actionType was performed.
                (https://help.zscaler.com/zia/about-audit-logs#sub)
            actionResult: The outcome (i.e., Failure or Success) of an actionType.
            actionInterface: The interface (i.e., Admin UI or API) where the actionType was performed.
            clientIP: The source IP address for the admin.
            adminName: The admin's login ID.

        Returns:
            HTTP Response 204

        """
        startTime = int(parser.parse(startTime).timestamp()) * 1000  # Converting starttime to epoch
        endTime = int(parser.parse(endTime).timestamp()) * 1000  # Converting endtime to epoch

        parameters = locals()
        url = self.form_full_url('audit')

        parameters = u.clean_args(parameters, ['self', 'full'])

        return self.full_retrieval('POST', url, {}, parameters, pageSize,
                                   'Request to create audit log entry report sucessfully sent.', full)

    def get_auditlog_entry_report_status(self):
        """
        Gets the status of a request for an audit log report. After sending a POST request to /auditlogEntryReport to
        generate a report, you can continue to call GET /auditlogEntryReport to check whether the report has finished
        generating. Once the status is COMPLETE, you can send another GET request to /auditlogEntryReport/download to
        download the report as a CSV file.

        Returns:
            Status in JSON format.
        """

        url = self.form_full_url('audit')

        req = re.Request('GET', url)

        return self.send_recv(req, 'Obtained audit log entry report status.')

    def cncl_auditlog_entry_report(self):
        """
        Cancels the request to create an audit log report.

        Returns:
            200 OK
        """
        url = self.form_full_url('audit')

        req = re.Request('DELETE', url)

        return self.send_recv(req, 'Cancelled request to create audit log report.')

    def dwl_auditlog_entry_report(self):
        """
        Downloads the most recently created audit log report. After a call to GET /auditlogEntryReport indicates that
        the report (CSV file) was generated, you can send a GET request to /auditlogEntryReport/download to download
        the file.

        Returns:
            CSV files in string format. Must be formatted.
        """
        url = self.form_full_url('audit', ['download'])

        req = re.Request('GET', url)

        return self.send_recv(req, 'Audit log entry report downloaded.')

    #####################
    # PRIVATE FUNCTIONS #
    #####################

    def send_recv(self, request: re.Request, successful_msg='Request was sucessful.'):
        """
        Send request and handle response. Retries if 429.
        Args:
            request: Request to be sent.
            successful_msg: Message to display when verbosity set to true and success.

        Returns:
            Content or JSON. None if retries exceeded.
        """
        for i in range(self.retries):
            prep_req = self.s.prepare_request(request)
            if self.debug:
                u.pretty_print_request(prep_req)
            response = self.s.send(prep_req)
            if self.debug:
                u.pretty_print_response(response)
            content_type = response.headers.get('content-type')

            if content_type == 'application/json':
                content = response.json()
                is_json = True
            else:
                content = response.text()
                is_json = False

            try:
                response.raise_for_status()
            except re.exceptions.HTTPError as e:
                if response.status_code == 429:
                    time.sleep(self.sleep_time)
                    continue
                else:
                    content = json.dumps(content, indent=4) if is_json else content
                    raise ResponseException(str(e) + '\n' + content)
            else:
                if self.verbosity and successful_msg != '':
                    print(successful_msg)
                return content

        if self.verbosity:
            print('Maximum retries exceeded. No response was recieved.')
        return None

    def full_retrieval(self, method: str, url: str, params: dict, json_content: dict, page_size: int = 500, message="",
                       full=True):
        """
        For requests where page and pageSize can be specified, this retrieves all available pages for the given
        pageSize.
        Args:
            method (str): HTTP method.
            url (str): URL string.
            params (dict): GET parameters that will be passed through URL.
            json_content (dict): Content to be added at the end of the request. For POST and PUT requests.
            page_size (int): Defaults to 500. Page size for max result entries.
            message (str): Message to be displayed when success.
            full (bool): Defaults to True. Enables full retrieval. If set to False, simple request will be done.

        Returns:
            JSON object. Dict or list.

        """
        # If json_content {}, then put it to None
        if not json_content:
            json_content = None

        # Same goes for params
        if not params:
            params = None

        # If not full retrieval requested, then do a simple request
        if not full:
            return self.send_recv(re.Request(method, url, params=params, json=json_content), message)
        # If not
        else:
            # If no params were given, then create empty dict
            if not params:
                params = {}

            # If no 'page' in the params, then insert it to loop over
            if 'page' not in params:
                params['page'] = 1

            # If no 'pageSize' in the params, then insert it to loop over
            if 'pageSize' not in params:
                params['pageSize'] = page_size

        # List of all the results put together
        result = []

        # Previous result in the loop to compare and decide if to break the loop
        previous = None

        # Request loop
        while True:
            req = re.Request(method, url, params=params, json=json_content)
            res = self.send_recv(req, message)

            # Breaks if res was empty or if not all active
            if not res or res == previous:
                break
            else:
                # Concats results
                result += res
                # If not, counter should increase
                params['page'] += 1
                # Readjust previous
                previous = res

        return result

    def form_full_url(self, key, elements: list = None):
        """It just joins the API URI with the wanted
        URL.

        Args:
            key (String): Configured dict key that exists in the config.json file.
            elements (List of strings): List of url elements to be included

        Returns:
            String: Full URL for the wanted action.
        """
        remaining = ""
        if elements:
            for element in elements:
                remaining += f'/{element}'
        return self.host + self.urls[key] + remaining

    def my_except_hook(self, exctype, value, traceback):
        """
        Error hook to be executed when exception raised so session can be closed.
        Args:
            exctype: Exception type.
            value: Value of exception.
            traceback: Traceback.

        """
        if exctype == re.exceptions.RequestException or exctype == ResponseException:
            self.logout()

        sys.__excepthook__(exctype, value, traceback)
