"""
Module for audit log report.
"""
import requests as re
from dateutil.parser import parse

import zia_client._utils as u
from zia_client import ZIAConnector


def req_auditlog_entry_report(session: ZIAConnector, startTime: str, endTime: str, page=None, pageSize=500,
                              actionTypes: list = False, category: str = "", subcategories: list = False,
                              actionResult: str = "", actionInterface: str = "", objectName="", clientIP: str = "",
                              adminName: str = "", targetOrgId: int = None, full=False):
    """
    Creates an audit log report for the specified time period and saves it as a CSV file. The report includes audit
    information for every call made to the cloud service API during the specified time period. Creating a new audit
    log report will overwrite a previously-generated report.

    Args:
        session (ZIAConnector): Logged in API client.
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
    startTime = int(parse(timestr=startTime).timestamp()) * 1000  # Converting starttime to epoch
    endTime = int(parse(timestr=endTime).timestamp()) * 1000  # Converting endtime to epoch

    parameters = locals()
    url = session.get_url('audit', 'main')

    parameters = u.clean_args(parameters, 'session', 'full')

    return session.full_retrieval('POST', url, json_content=parameters, page_size=pageSize,
                                  message='Request to create audit log entry report sucessfully sent.', full=full)


def get_auditlog_entry_report_status(session):
    """
    Gets the status of a request for an audit log report. After sending a POST request to /auditlogEntryReport to
    generate a report, you can continue to call GET /auditlogEntryReport to check whether the report has finished
    generating. Once the status is COMPLETE, you can send another GET request to /auditlogEntryReport/download to
    download the report as a CSV file.

    Returns:
        Status in JSON format.
    """

    url = session.get_url('audit', 'main')

    req = re.Request('GET', url)

    return session.send_recv(req, 'Obtained audit log entry report status.')


def cncl_auditlog_entry_report(session):
    """
    Cancels the request to create an audit log report.

    Returns:
        200 OK
    """
    url = session.get_url('audit', 'main')

    req = re.Request('DELETE', url)

    return session.send_recv(req, 'Cancelled request to create audit log report.')


def dwl_auditlog_entry_report(session):
    """
    Downloads the most recently created audit log report. After a call to GET /auditlogEntryReport indicates that
    the report (CSV file) was generated, you can send a GET request to /auditlogEntryReport/download to download
    the file.

    Returns:
        CSV files in string format. Must be formatted.
    """
    url = session.get_url('audit', 'dwl')

    req = re.Request('GET', url)

    return session.send_recv(req, 'Audit log entry report downloaded.')
