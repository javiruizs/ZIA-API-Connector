"""
Module for sandbox management.
"""

import requests as re

from zia_client.session import ZIAConnector


def get_sandbox_quota(session: ZIAConnector):
    """Gets the Sandbox Report API quota information for your organization.

    The resource access quota for retrieving Sandbox Detail Reports is restricted to 1000 requests per day, with a rate
    limit of 2/sec and 1000/hour. Use GET /sandbox/report/quota to retrieve details regarding your organization's
    daily Sandbox API resource usage (i.e., used quota, unused quota).

    Args:
        session: Active API session.

    Returns:
        JSON list of dict: Example::

        [
          {
            "startTime": 0,
            "used": 0,
            "allowed": 0,
            "scale": "NANOSECONDS",
            "unused": 0
          }
        ]
    """

    url = session.form_full_url('sandbox', 'quota')

    return session.form_full_url(re.Request('GET', url), 'Sandbox Quota received.')


def get_sandbox_file_report(session: ZIAConnector, md5Hash: str, report_type: str = 'summary'):
    """
    Gets a full (i.e., complete) or summary detail report for an MD5 hash of a file that was analyzed by Sandbox.

    Args:
        session: Active API session.
        md5Hash: File MD5 Hash.
        report_type: Type of report. Either 'summary' or 'full'.

    Returns:
        JSON dict.
    """

    url = session.form_full_url('sandbox', md5Hash)

    return session.send_recv(re.Request('GET', url, params={'type': report_type}),
                             f"Sandbox report for hash {md5Hash} obtained.")
