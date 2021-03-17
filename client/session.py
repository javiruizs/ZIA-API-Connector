"""
Class that encapsulates the session management while connecting to the Zscaler ZIA API. For each of the references that
exist (see https://help.zscaler.com/zia/api), I will try to create a specific method. Also, I'll try to create methods
that will apply on the general use that I will make of it.
"""

import json
import sys
import time

import requests as re

import client.utils as u
from client.exceptions import ResponseException


class ZIAConnector:
    """
    ZIA API REST Client
    """

    def __init__(self, config_file, verbosity=None):
        """

        Args:
            config_file (String): The path for the config file. Must be a JSON.
            verbosity (None or bool): If None, input from JSON file is taken. If True or False, then it will be
            override.
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
