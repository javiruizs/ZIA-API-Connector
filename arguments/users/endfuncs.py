import pandas as pd

import zia_api_client
import zia_api_client.custom as c


def search_groups(client: zia_api_client.ZIAConnector, args):
    return client.get_groups(args.search, args.page, args.pageSize, args.all)


def search_depts(client: zia_api_client.ZIAConnector, args):
    return client.get_departments(args.search, args.page, args.pageSize, args.all)


def search_usrs(client: zia_api_client.ZIAConnector, args):
    return client.get_users(args.search, args.dept, args.group, args.page, args.pageSize, args.all)


def update_usrs(client: zia_api_client.ZIAConnector, args):
    return c.update_users(client, args.file)


def add_u2g(client: zia_api_client.ZIAConnector, args):
    # Take first column for both files and convert them to list
    users = pd.read_csv(args.users).iloc[:, 0].to_list()
    groups = pd.read_csv(args.groups).iloc[:, 0].to_list()

    return c.add_users_to_group(client, users, groups, args.dft_dept)
