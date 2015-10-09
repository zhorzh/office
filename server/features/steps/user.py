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


@given('invalid user, no email')
def set_invalid_user_no_email(context):
    context.user = {
        'data': {
            'password': '123456',
            'image': 'test_url'}}


@given('user id is {id:d}')
def set_user_id(context, id):
    context.id = id


@given('invalid user, no password')
def set_invalid_user_no_password(context):
    context.user = {
        'data': {
            'email': 'bob@gmail.com',
            'image': 'test_url'}}


@given('email is "{email}"')
def set_email(context, email):
    context.email = {'data': {'email': email}}


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


@when('GET user')
def get_user(context):
    url = 'http://localhost/api/user/' + str(context.id)
    context.response = requests.get(url=url)


@when('DELETE user')
def delete_user(context):
    url = 'http://localhost/api/user/' + str(context.id)
    context.response = requests.delete(url=url)
    if context.response.status_code == 200:
        context.id = context.response.json()['user']['id']
    else:
        context.id = None


@when('PATCH user email')
def update_user_email(context):
    url = 'http://localhost/api/user/' + str(context.id)
    headers = {'content-type': 'application/json'}
    context.response = requests.patch(
        url=url,
        data=json.dumps(context.email),
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


@then('user email is "{email}"')
def check_user_email(context, email):
    assert context.response.json()['user']['email'] == email
