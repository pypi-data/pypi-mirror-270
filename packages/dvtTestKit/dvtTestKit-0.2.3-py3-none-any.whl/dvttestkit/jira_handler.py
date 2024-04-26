import json
import os
import re
from collections import namedtuple
from typing import Any, Optional

import requests
from requests.auth import HTTPBasicAuth

from dvttestkit import testKitUtils

logger = testKitUtils.makeLogger(__name__)


def get_ticket_components(jira_domain: str = os.getenv("JiraDomain"),
                          issue_key: str = os.getenv('DVT_TICKET')) -> Optional[str]:
    """
    Retrieve the name of the components field for a given Jira ticket.

    :param jira_domain: temp
    :param issue_key: Jira ticket key (e.g. "AUTO-770")
    :return: name of the components field, or None if the request failed
    """
    response = requests.get(
        f"{jira_domain}/rest/api/2/issue/{issue_key}",
        auth=HTTPBasicAuth(os.getenv("JiraEmail"), os.getenv("JiraToken"))
    )

    if response.status_code == 200:
        _data = response.json()
        return _data["fields"]["components"]
    else:
        logger.error(f"Failed to retrieve components for ticket {issue_key}: {response.text}")
        return None


def convert(dictionary: dict) -> Any:
    """
    Convert a dictionary to a namedtuple.

    :param dictionary: input dictionary
    :return: namedtuple with keys and values from the input dictionary
    """
    for key, value in dictionary.items():
        if isinstance(value, dict):
            dictionary[key] = convert(value)
    return namedtuple('GenericDict', dictionary.keys())(**dictionary)


def custom_decoder(obj: dict) -> Any:
    """
    Convert a dictionary to a namedtuple, replacing invalid characters in keys.

    :param obj: input dictionary
    :return: namedtuple with keys and values from the input dictionary, with invalid characters in keys replaced
    """

    def replace_invalid_chars(string: str) -> str:
        return re.sub(r'\W', '_', string)

    valid_keys = [replace_invalid_chars(key) for key in obj.keys()]
    return namedtuple('X', valid_keys)(*obj.values())


def set_status_testing(jira_domain: str = os.getenv("JiraDomain"), transition_name: str = "DVT Testing",
                       issue_key: str = os.getenv('DVT_TICKET')):
    """
    Changes the status of the specified Jira ticket to `transition_name`.

    :param jira_domain: The Jira domain.
    :type jira_domain: str
    :param transition_name: The target status name to set.
    :type transition_name: str
    :param issue_key: The Jira ticket key.
    :type issue_key: str
    :return: HTTP status code of the POST request.
    :rtype: int
    """
    # Get the current status of the ticket
    ticket_data = get_ticket_data(issue_key=issue_key)
    current_status = ticket_data.status
    # Check if the current status is already `transition_name`
    print(current_status)
    if current_status == "In Review":
        print(f"Ticket {issue_key} is already in {current_status}.")
        return 200
    if current_status == "Done":
        print(f"Ticket {issue_key} is already in {current_status}.")
        return 200

    transition_id = get_ticket_transitions(transition_name=transition_name, issue_key=issue_key)

    # Sending POST request
    logger.debug(f"{os.getenv('JiraEmail')}, {os.getenv('JiraToken')}")
    response = requests.request(
        "POST",
        f"{jira_domain}/rest/api/2/issue/{issue_key}/transitions",
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        auth=HTTPBasicAuth(os.getenv('JiraEmail'), os.getenv('JiraToken')),
        json={"transition": {"id": transition_id}}
    )

    return response.status_code


def get_ticket_data(jira_domain: str = os.getenv("JiraDomain"), issue_key: str = os.getenv('DVT_TICKET')):
    """
    Makes a GET request to the Jira API to retrieve data for the specified ticket.
    Returns a named tuple with the following fields: key, summary, description, due_date, components,
    status, assignee, priority, change_date, view_date

    :param jira_domain: temp
    :param issue_key: the key of the Jira ticket (e.g. "SPACE-123")
    :return: Named Tuple
    """
    response = requests.get(
        f"{jira_domain}/rest/api/2/issue/{issue_key}?detailed=true",
        auth=HTTPBasicAuth(os.getenv("JiraEmail"), os.getenv("JiraToken"))
    )
    # Check the status code of the response
    if response.status_code == 200:
        # The request was successful, so parse the response JSON and return it as a named tuple
        _data = json.loads(response.text)
        ticket_tuple = namedtuple(
            'ticket_tuple',
            ['key', 'summary', 'description',
             'due_date', 'components', 'status', 'assignee',
             'priority', 'change_date', 'view_date']
        )

        key = _data.get("key")
        summary = _data["fields"].get("summary")
        description = _data["fields"].get("description")
        due_date = _data["fields"].get("duedate")
        components = _data["fields"]["components"][0].get('name')
        status = _data["fields"]["status"].get('name')
        assignee = _data["fields"]["assignee"].get('displayName')
        priority = _data["fields"]["priority"].get('name')
        change_date = _data["fields"].get("statuscategorychangedate")
        view_date = _data["fields"].get("lastViewed")

        # Return the data as a named tuple
        return ticket_tuple(
            key, summary, description,
            due_date, components, status,
            assignee, priority, change_date,
            view_date
        )
    else:
        # The request was not successful, so print the error message
        return f"Error: {response.text}"


def get_board_data(jira_domain: str = os.getenv("JiraDomain"), board_id: str = os.getenv('BoardKey')):
    """
    Makes a GET request to the Jira API to retrieve data for issues on the specified board.
    Returns a list of named tuples, each containing data about an issue: key, summary, description, due_date, components,
    status, assignee, priority, change_date, view_date.

    :param jira_domain: The domain of your Jira instance.
    :param board_id: The ID of the board to retrieve issues from.
    :return: List of named tuples with issue data or an error message.
    """
    # Define the fields you want to fetch for each issue
    fields = "key,summary,description,duedate,components,status,assignee,priority,updated,created"

    # Make the GET request to the Jira REST API search endpoint to fetch issues by board ID
    response = requests.get(
        f"{jira_domain}/rest/api/2/search?jql=project={board_id}",
        params={'fields': fields},
        auth=HTTPBasicAuth(os.getenv("JiraEmail"), os.getenv("JiraToken"))
    )

    # Check the status code of the response
    if response.status_code == 200:
        # The request was successful, parse the response JSON
        issues = json.loads(response.text)['issues']
        IssueTuple = namedtuple('IssueTuple',
                                'key summary description due_date components status assignee priority change_date view_date')

        # Create a list of named tuples for each issue
        result = []
        for issue in issues:
            fields = issue['fields']
            assignee = fields.get('assignee')
            assignee_name = assignee.get('displayName') if assignee else None
            issue_data = IssueTuple(
                key=issue['key'],
                summary=fields.get('summary', None),
                description=fields.get('description', None),
                due_date=fields.get('duedate', None),
                components=[c['name'] for c in fields.get('components', [])],
                status=fields.get('status', {}).get('name', None),
                assignee=assignee_name,
                priority=fields.get('priority', {}).get('name', None),
                change_date=fields.get('updated', None),
                view_date=fields.get('created', None)
            )
            result.append(issue_data)
        return result
    else:
        # The request was not successful, return the error message
        return f"Error: {response.status_code} {response.text}"


def retrieve_wip_tickets(jira_domain: str = os.getenv("JiraDomain"),
                         board_id: str = 'AUTO'):
    """
    Retrieve Jira tickets with status 'In Progress' from Jira board 'AUTO'

    Returns:
        List of ticket summaries with status 'In Progress'
    """
    endpoint = f'{jira_domain}/rest/agile/1.0/board/{board_id}/issue'
    auth = HTTPBasicAuth(os.getenv("JiraEmail"), os.getenv("JiraToken"))
    params = {"boardId": board_id}
    response = requests.get(endpoint, auth=auth, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve tickets: {response.status_code}")

    ticket_summaries = []
    for ticket in response.json()['issues']:
        if ticket['fields']['status'].get('name') == 'In Progress':
            ticket_summaries.append(ticket['fields']['summary'])

    return ticket_summaries


def parse_jira_tickets(tickets):
    # TODO move this function back to cdrouterTestKit
    parsed_tickets = []
    for ticket in tickets:
        # Split the ticket summary by hyphen
        parts = ticket.split('-')

        # Extract the device name, package version, and test type from the ticket summary
        device = parts[0]
        package = f"{parts[1]}-{parts[2]}-{parts[3]}"
        test_type = parts[4]

        # Set the cdrouter_device, cdrouter_package, and cdrouter_tests variables
        ticket_dict = {
            'cdrouter_device': device,
            'cdrouter_package': package,
            'cdrouter_tests': test_type
        }

        # Set the cdrouter_config variable based on the test type
        if test_type == 'Run CDRouter Docsis Test':
            ticket_dict['cdrouter_config'] = f'{device}_docsis'
        elif test_type == 'Run Full IPv6 CDRouter Test':
            ticket_dict['cdrouter_config'] = f'{device}_ipv6'
        elif test_type == 'Run Full Automation Test':
            ticket_dict['cdrouter_config'] = f'{device}_automation'
        elif test_type == 'Run 2.4GHz Test':
            ticket_dict['cdrouter_config'] = f'{device}_wifi'
        elif test_type == 'Run 5GHz Test':
            ticket_dict['cdrouter_config'] = f'{device}_wifi_5GHz'

        parsed_tickets.append(ticket_dict)
    return parsed_tickets


def attach_file_to_ticket(file, jira_domain: str = os.getenv("JiraDomain"), issue_key=os.getenv('DVT_TICKET')):
    """
    Attaches file to given Jira ticket
    :type file: path
    :param jira_domain: temp
    :param file:
    :type issue_key: str
    :param issue_key:

    """
    response = requests.request(
        "POST",
        f"{jira_domain}/rest/api/2/"
        f"issue/{issue_key}/attachments",
        headers={
            "Accept": "application/json",
            "X-Atlassian-Token": "no-check"
        },
        auth=HTTPBasicAuth(os.getenv("JiraEmail"),
                           os.getenv("JiraToken")),
        files={
            "file": (
                f"{file}",
                open(f"{file}", "rb"),
                "application-type"
            )
        }
    )
    return json.dumps(
        json.loads(response.text),
        sort_keys=True,
        indent=4,
        separators=(",", ": ")
    )


def get_ticket_transitions(transition_name, jira_domain: str = os.getenv("JiraDomain"),
                           issue_key: str = os.getenv('DVT_TICKET')):
    # Make a GET request to the Xray API to get the test result
    response = requests.get(
        f"{jira_domain}/rest/api/2/issue/{issue_key}"
        f"/transitions?expand=transitions.fields",
        auth=HTTPBasicAuth(os.getenv("JiraEmail"),
                           os.getenv("JiraToken"))
    )
    # Check the status code of the response
    if response.status_code == 200:
        # If the request was successful, parse the JSON response
        transitions = response.json()["transitions"]
        for transition in transitions:
            if transition["name"] == transition_name:
                return transition["app_id"]
    else:
        # If the request was not successful, print an error message
        return f"Error getting test result: {response.status_code}"


class TicketData:

    def __init__(self, issue_key: str = os.getenv('DVT_TICKET')):
        self.data = get_ticket_data(issue_key)


def update_test_status(api_token: str, test_execution_id: str, status: str) -> requests.Response:
    """
    This function updates the test execution status using the Xray REST API.

    Args:
        api_token (str): The Jira API token.
        test_execution_id (str): The id of the test execution to update.
        status (str): The new status to set for the test execution.

    Returns:
        requests.Response: The response from the API call.
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_token}'
    }

    url = f'https://minimco.atlassian.net/rest/raven/1.0/api/testrun/{test_execution_id}/status'

    payload = {
        'status': status
    }

    return requests.post(url, headers=headers, data=json.dumps(payload))


if __name__ == '__main__':
    # You can now call this function like so:
    # response = update_test_status("your_api_token", "your_test_execution_id", "EXECUTING")
    # print(get_ticket_data(issue_key="DVD-67"))
    x = get_board_data()
    breakpoint()
