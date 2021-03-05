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
        #u.print_json(location)
        session.create_location(location)


def add_users_to_group(session: ZIAConnector, user_mails: list, group_ids: list):
    # Retrieve full list of user jsons
    full_user_list = session.get_users(full=True)

    # Filter out the ones that don't exist in the user mail list.
    filtered = list(filter(lambda usr: usr['email'] in user_mails, full_user_list))

    for user in filtered:
        # Obtain user's group list
        groups = set([g['id'] for g in user['groups']])

        # Set difference to obtain the groups to be added
        to_add = set(group_ids) - groups
        for group in to_add:
            user['groups'].append({'id': group})

        #Update user
        session.update_user(user)