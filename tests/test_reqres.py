import requests
from pytest_voluptuous import S
from schemas.reqres_schemas import new_user_schema, update_user_schema, login_schema
import pytest_check as check


def test_create_user():
    payload = {
        "name": "john",
        "job": "qa"
    }

    response = requests.post(url='https://reqres.in/api/users', data=payload)

    check.equal(response.status_code, 201)
    check.equal(response.json()['name'], 'john')
    check.equal(response.json()['job'], 'qa')
    check.equal(S(new_user_schema), response.json())


def test_update_user():
    payload = {
        "name": "rembo",
        "job": "poet"
    }

    response = requests.put(url='https://reqres.in/api/users/2', data=payload)

    check.equal(response.status_code, 200)
    check.equal(response.json()['name'], 'rembo')
    check.equal(response.json()['job'], 'poet')
    check.equal(S(update_user_schema), response.json())


def test_delete_user():
    response = requests.delete(url='https://reqres.in/api/users/2')

    assert response.status_code == 204


def test_login():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url='https://reqres.in/api/login', data=payload)

    check.equal(response.status_code, 200)
    check.equal(response.json()['token'], 'QpwL5tke4Pnpja7X4')
    check.equal(S(login_schema), response.json())

def test_resource_not_found():
    response = requests.get(url='https://reqres.in/api/unknown/1234')

    assert response.status_code == 404