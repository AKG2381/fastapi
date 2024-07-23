from fastapi import status

from .utils import *
from ..routers.users import get_db,get_current_user


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'ajeetkumarguptatest'
    assert response.json()['email'] == 'ajeettest@gmail.com'
    assert response.json()['first_name'] == 'ajeettest'
    assert response.json()['last_name'] == 'guptatest'
    assert response.json()['phone_number'] == '+91-7440885722'

def test_changes_passowrd_success(test_user):
    response = client.put("/user/password",json = {'password' : 'testpassword','new_password' : 'newtestpassword'})
    assert response.status_code == status.HTTP_204_NO_CONTENT



def test_changes_passowrd_invalid_current_password(test_user):
    response = client.put("/user/password",json = {'password' : 'testpasswords','new_password' : 'newtestpassword'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail' :'Error on password change'}

def test_changes_change_phone_numer_success(test_user):
    response = client.put("/user/phone_number/29374678249")
    assert response.status_code == status.HTTP_204_NO_CONTENT
