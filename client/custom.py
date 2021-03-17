"""
Custom functions
"""
import json

import client.utils as u
import client.locations as locs
import client.users as usrs
from client.session import ZIAConnector


def create_sublocations(session: ZIAConnector, sublocations):
    with open(sublocations, 'r') as f:
        config = json.load(f)

    parentIds = locs.get_location_ids(session, includeParentLocations=True)

    for parent in config['parents']:
        try:
            parentId = u.get_location_id(parentIds, parent)
        except ValueError as e:
            print(e)
            return

        location = {
            "name": config['name'],
            "parentId": parentId
        }

        location = {**location, **config['config']}
        # u.print_json(location)
        locs.create_location(session, location)


def add_users_to_group(session: ZIAConnector, user_mails: list, group_ids: list, default_dept: int):
    """
    Adds users to the specified groups. Users must be passed as emails. Groups, too. For those who don't have a
    department assigned to them, which is necessary to save the changes, a default department must be given.

    Args:
        session: An active session.
        user_mails: The list with the user mails.
        group_ids: The list with the group ids.
        default_dept: The default department.

    Returns:
        The response obtained. JSON format or a decoded string.

    """
    # Retrieve full list of user jsons
    full_user_list = usrs.get_users(session, full=True, pageSize=1000)

    # Make sure all emails are lowercase
    user_mails = [mail.lower() for mail in user_mails]

    # Filter out the ones that don't exist in the user mail list.
    filtered = list(filter(lambda usr: usr['email'].lower() in user_mails, full_user_list))

    update_count = 0
    users = []
    for user in filtered:
        # Obtain user's group list
        groups = set([g['id'] for g in user['groups']])

        # Set difference to obtain the groups to be added
        to_add = set(group_ids) - groups
        if to_add:
            for group in to_add:
                user['groups'].append({'id': group})
            update_count += 1

            if 'department' not in user or not user['department']:
                user['department'] = {'id': default_dept}
            # Update user
            usrs.update_user(session, user)
            users.append(user)

    if session.verbosity:
        print(f'Total users: {len(full_user_list)}')
        print(f'Given users: {len(user_mails)}')
        print(f'Given groups: {len(group_ids)}')
        print(f'Cross-matched users: {len(filtered)}')
        print(f'Updated users: {update_count}')

    return users


def obtain_all_locations_sublocations(session: ZIAConnector):
    parents = locs.search_locations(session, full=True)

    sublocations = [locs.get_sublocations(session, parent['id']) for parent in parents]

    print(f'Total: {len(parents) + len(sublocations)}')
    print(f'Locations: {len(parents)}')
    print(f'Sublocations: {len(sublocations)}')

    return {'parents': parents, 'sublocations': sublocations}


def update_users(session: ZIAConnector, json_file):
    with open(json_file) as f:
        users = json.load(f)

    return [usrs.update_user(session, user) for user in users]
