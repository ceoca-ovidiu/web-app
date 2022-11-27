import requests

GET_ALL_EMPLOYEES_URL = "http://localhost:8080/getEmployees"
CREATE_EMPLOYEE_URL = "http://localhost:8080/createEmployee"
GET_EMPLOYEE_BY_FIRST_NAME_URL = "http://localhost:8080/getEmployeesByFirstName/"
GET_EMPLOYEE_BY_PLACE_URL = "http://localhost:8080/getEmployeesByPlace/"
GET_EMPLOYEE_BY_ID_URL = "http://localhost:8080/getEmployeeById/"
DELETE_EMPLOYEE_BY_ID_URL = "http://localhost:8080/deleteEmployee/"
GET_EMPLOYEE_BY_GENDER_URL = "http://localhost:8080/getEmployeesByGender/"


def get_all_employees():
    return requests.get(GET_ALL_EMPLOYEES_URL).json()  # returns a list of JSON data where each element is a dictionary


def create_employee(employee):
    requests.post(CREATE_EMPLOYEE_URL, params=employee)


def get_employee_by_first_name(first_name):
    requests.get(GET_EMPLOYEE_BY_FIRST_NAME_URL, params={"employeeFirstName": first_name}).json()


def get_employee_by_place(place):
    requests.get(GET_EMPLOYEE_BY_PLACE_URL, params={"employeePlace": place}).json()


def get_employee_by_id(get_id):
    requests.get(GET_EMPLOYEE_BY_ID_URL, params={"id": get_id}).json()


def get_employee_by_gender(gender):
    requests.get(GET_EMPLOYEE_BY_GENDER_URL, params={"employeeGender": gender}).json()


def delete_employee_by_id(delete_id):
    requests.delete(DELETE_EMPLOYEE_BY_ID_URL, params={"id": delete_id})
