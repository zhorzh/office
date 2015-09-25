from behave import given, when, then
import requests
import json


@given('valid user')
def set_valid_user(context):
    context.user = {
        'data': {
            'email': 'bob@gmail.com',
            'password': '123456',
            'image': 'test_url'}}


@when('POST user')
def post_user(context):
    url = 'http://localhost/api/user'
    headers = {'content-type': 'application/json'}
    context.response = requests.post(
        url=url,
        data=json.dumps(context.user),
        headers=headers)
    if context.response.status_code == 200:
        context.id = context.response.json()['user']['id']
    else:
        context.id = None


@then('response status code is {status_code:d}')
def check_response_status_code(context, status_code):
    assert context.response.status_code == status_code


@then('response contains user')
def check_response_contents_user(context):
    assert context.response.json()['user']


@then('response contains user id')
def check_response_contents_user_id(context):
    assert context.response.json()['user']['id']
