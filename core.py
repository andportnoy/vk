import re
import time
import requests
import getpass

from .errors import VKError
from json.decoder import JSONDecodeError
from requests import ConnectionError


def get_token(app_id=5080984):

    login_url = 'https://m.vk.com'
    token_request_url = 'https://oauth.vk.com/authorize'
    token_request_params = {
        'client_id': app_id,
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'display': 'mobile',
        'scope': 77830,
        'response_type': 'token'
    }

    login_credentials = {'email': input('Please enter login: '),
                         'pass': getpass.getpass('Please enter password: ')}

    with requests.Session() as s:
        # login
        login_page_html = s.get(login_url).text
        login_form_action_pattern = r'<form(?= ).* action="(.+)"'
        url = re.findall(login_form_action_pattern, login_page_html)[0]
        s.post(url, login_credentials)

        # get token
        token_containing_url = s.get(token_request_url, params=token_request_params).url
        token_pattern = r'(?<=access_token=)[\w]+(?=&)'
        token = re.findall(token_pattern, token_containing_url)
    if token:
        with open('token.txt', 'w') as t:
            t.write(token[0])
        return token[0]
    else:
        print('Token not in url. Check your login info.')


def read_token():
    try:
        with open('token.txt') as t:
            token = t.read()
    except IOError:
        print('Token file not found, getting token from vk for app 5080984.')
        token = get_token(app_id=5080984)
        return token
    else:
        return token

def vdr(method, params_dict=None):

    # set API version
    params_dict['v'] = '5.8'
    api_url = "https://api.vk.com/method/" + method

    # attempt to connect
    while True:
        try:
            raw_response = requests.post(api_url, data=params_dict)
        except ConnectionError:
            print('Connection error. Retrying in 1 s.')
            time.sleep(1)
        else:
            # attempt to decode JSON from the response
            try:
                response = raw_response.json()
            except JSONDecodeError:
                print('Could not decode JSON: ')
                print('Status code:', raw_response.status_code)
            else:
                # attempt to extract response or error from JSON-decoded response
                try:
                    return response['response']
                except KeyError:
                    try:
                        raise VKError(response['error'])
                    except KeyError:
                        print('Unable to recognize a response or an error. '
                              'Got the following response:')
                        print(response)
            break

def params_dict_from_locals(locals_dict):

    return {param: value for param, value in locals_dict.items() if value is not None}
