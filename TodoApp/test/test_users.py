from utils import *
from TodoApp.routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# def test_return_user(test_user):
#     response = client.get('/users')
#     assert response.status_code == status.HTTP_200_OK
#     user = response.json()
#     assert user['username'] == "codingwithrobytest"
#     assert user['email'] == "codingwithrobytest@email.com"
#     assert user['first_name'] == "Eric"
#     assert user['last_name'] == "Roby"
#     assert user['role'] == "admin"
#     assert user['phone_number'] == "(111)-111-1111"

# def test_change_password_success(test_user):
#     response = client.put("/users/password", json={"current_password": "testpassword",
#                                                   "new_password": "newpassword"})
#     assert response.status_code == status.HTTP_204_NO_CONTENT


# def test_change_password_invalid_current_password(test_user):
#     response = client.put("/users/password", json={"current_password": "wrong_password",
#                                                   "new_password": "newpassword"})
#     assert response.status_code == status.HTTP_401_UNAUTHORIZED
#     assert response.json() == {'detail': 'Error on password change'}


# def test_change_phone_number_success(test_user):
#     response = client.put("/users/phone/2222222222")
#     assert response.status_code == status.HTTP_204_NO_CONTENT

