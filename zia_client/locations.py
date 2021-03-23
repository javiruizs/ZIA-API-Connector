"""
Module for location management.
"""
import time
from typing import List

import requests as re

import zia_client._utils as u
from zia_client import ZIAConnector


def create_location(session: ZIAConnector, location):
    """Creates the location.

    Args:
        session (ZIAConnector): Logged in API client.
        location (String): A dictionary representing the location. See example.
    """

    url = session.form_full_url('locs')

    req = re.Request('POST', url, json=location)

    return session.send_recv(req, successful_msg=f'Location {location["name"]} was successfully added.')


def update_location(session: ZIAConnector, location):
    """Updates an existing location.

    Args:
        session (ZIAConnector): Logged in API client.
        location (dict): The location information in dict format.
    """

    # Check if the _locations data contains it's id.
    if 'id' not in location:
        raise ValueError('There is no "id" keyword in the location dict.')

    url = session.form_full_url('locs', location["id"])

    time.sleep(0.5)
    r = re.Request('PUT', url, json=location)

    return session.send_recv(r, successful_msg=f'Location {location["id"]} was successfully updated.')


def delete_location(session: ZIAConnector, loc_id: int):
    """Deletes location given its id.

    Args:
        session (ZIAConnector): Logged in API client.
        loc_id (int): Location identifier.

    Raises:
        Exception: If delete is unsuccessful, then it raises an exception.
    """
    url = session.form_full_url('locs', loc_id)

    r = re.Request('DELETE', url)

    return session.send_recv(r, successful_msg=f'Location {loc_id} deleted successfully')


def search_locations(session: ZIAConnector, search="", sslScanEnabled=None, xffEnabled=None, authRequired=None,
                     bwEnforced=None, page=None, pageSize=None, full=False):
    """Retrieves all the _locations, not sub-_locations that match the search.
    Could be IP address or name.

    Args:
        session (ZIAConnector): Logged in API client.
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

    url = session.form_full_url('locs')

    # Key all is not recognized by the API, therefore can be removed

    return session.full_retrieval('GET', url, params=params, page_size=1000, message="Location search successful.",
                                  full=full)


def get_location_ids(session: ZIAConnector, includeSubLocations=None, includeParentLocations=None, authRequired=None,
                     bwEnforced=None, sslScanEnabled=None, xffEnabled=None, search="", page=None, pageSize=None,
                     full=False):
    """
    Gets a name and ID dictionary of _locations.

    Args:
        session (ZIAConnector): Logged in API client.
        xffEnabled (bool): Filter based on whether the Enforce XFF Forwarding setting is enabled or disabled for a \
        location.

        bwEnforced (bool): Filter based on whether Bandwidth Control is being enforced for a location.

        authRequired (bool): Filter based on whether the Enforce Authentication setting is enabled or disabled for \
        a location.

        full: If set to True, all location IDs will be obtained.

        includeSubLocations (bool, optional): if set to true sub-_locations will be included in the response \
        otherwise they will excluded. Defaults to False.

        includeParentLocations (bool, optional): if set to true _locations with sub _locations will be included in \
        the response, otherwise only _locations without sub-_locations are included. Defaults to False.

        sslScanEnabled (bool, optional): Filter based on whether the Enable SSL Scanning setting is enabled or
        disabled for a location. Defaults to False.

        search (str, optional): The search string used to partially match against a location's name and port \
        attributes. Defaults to "".

        page (int, optional): Specifies the page offset. Defaults to 1.

        pageSize (int, optional): Specifies the page size. The default size is 100, but the maximum size is 1000. \
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

    url = session.form_full_url('locInfo')

    return session.full_retrieval('GET', url, params=params, page_size=pageSize,
                                  message="Location ids retrieval successful.", full=full)


def get_location_info(session: ZIAConnector, loc_id):
    """Returns all the information of the desired location.

    Args:
        session (ZIAConnector): Logged in API client.
        loc_id (int): Location identifier

    Returns:
        dict: A dict containing all the information. If no success, dict is empty.
    """
    url = session.form_full_url('locs', loc_id)

    r = re.Request('GET', url)
    time.sleep(1)

    return session.send_recv(r, f'Location info for {loc_id} has been successfully retrieved.')


def get_sublocations(session: ZIAConnector, locationId, search="", sslScanEnabled=None, xffEnabled=None,
                     authRequired=None, bwEnforced=None, enforceAup=None, enableFirewall=None):
    """
    Gets the sub-location information for the location with the specified ID. These are the sub-_locations associated
    to the parent location.

    Args:
        session (ZIAConnector): Logged in API client.
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

    url = session.form_full_url('locs', locationId, 'sublocations')

    # Use directly args of this function as parameters on the request, but they need to be cleaned first.
    args = locals()
    params = u.clean_args(args)

    return session.full_retrieval('GET', url, params=params, page_size=0,
                                  message=f"Sublocations for {locationId} obtained successfully.", full=False)


def bulk_del_location(session: ZIAConnector, loc_ids: List):
    """Bulk delete _locations up to a maximum of 100 _locations per request.

    Bulk delete _locations up to a maximum of 100 _users per request.
    The response returns the location IDs that were successfully deleted.

    Args:
        session (ZIAConnector): Logged in session.
        loc_ids: List of location ids.

    Returns:
        JSON Dict response.
    """

    url = session.form_full_url('locs', 'bulkDelete')

    data = {
        "ids": loc_ids
    }

    req = re.Request('POST', url, json=data)

    return session.send_recv(req, "Bulk delete of _locations done.")
