from .ziaSession import ZIAConnector
from . import utils as u
import json


def create_locations_sublocations(session: ZIAConnector, locations_file, sublocations_file):
    """Creates for every location in locations file all sublocations in the
    sublocations file.

    Args:
        session (ZIAConnector): ZIASession object with initiated session
        locations_file (String): Path to the locations file
        sublocations_file (String): Path to the sublocations file
    """
    location_names = session.create_locations(locations_file)

    session.get_status()
    session.activate_changes()

    location_ids = session.get_location_ids()

    with open(sublocations_file) as f:
        sublocations = json.load(f)

    url = session.__create_full_url('locations')

    for name in location_names:
        parent_id = session.__get_location_id(location_ids, name)
        for location in sublocations:
            location['parentId'] = parent_id
            r = session.s.post(url, json=location)
            if r.status_code == 200:
                print(
                    f'Sublocation {location["name"]} for {name} was successfully added.')
            else:
                print(
                    f'{r.status_code} {r.text} - Sublocation {location["name"]} for {name} was not added.')
                with open('error.html', 'w') as f:
                    f.write(r.text)


def create_sublocations(session: ZIAConnector, sublocations):
    with open(sublocations, 'r') as f:
        config = json.load(f)

    parentIds = session.get_location_ids(includeParentLocations=True)

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
        session.create_location(location)


def add_users_to_group(session: ZIAConnector, user_mails: list, group_ids: list, default_dept: int):
    # Retrieve full list of user jsons
    full_user_list = session.get_users(full=True, pageSize=1000)

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
            session.update_user(user)
            users.append(user)

    if session.verbosity:
        print(f'Total users: {len(full_user_list)}')
        print(f'Given users: {len(user_mails)}')
        print(f'Given groups: {len(group_ids)}')
        print(f'Cross-matched users: {len(filtered)}')
        print(f'Updated users: {update_count}')

    return users


def obtain_all_locations_sublocations(session: ZIAConnector):
    parents = session.search_locations(full=True)

    sublocations = [session.get_sublocations(parent['id']) for parent in parents]

    print(f'Total: {len(parents) + len(sublocations)}')
    print(f'Locations: {len(parents)}')
    print(f'Sublocations: {len(sublocations)}')

    return {'parents': parents, 'sublocations': sublocations}


def update_users(session: ZIAConnector, json_file):
    with open(json_file) as f:
        users = json.load(f)

    return [session.update_user(user) for user in users]