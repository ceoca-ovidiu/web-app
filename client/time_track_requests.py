import requests

GET_ALL_TIME_TRACKS_URL = "http://localhost:8080/getAllTimeTracks"
CREATE_TIME_TRACK_URL = "http://localhost:8080/createTimeTrack"
GET_TIME_TRACK_BY_EMPLOYEE_ID_URL = "http://getTimeTrackByEmployeeId/"
DELETE_TIME_TRACK_URL = "http://localhost:8080/deleteTimeTrack/"


def get_all_time_tracks():
    return requests.get(GET_ALL_TIME_TRACKS_URL).json()


def create_time_track(time_track):
    requests.post(CREATE_TIME_TRACK_URL, params=time_track)


def get_time_track_by_employee_id(employee_id):
    requests.get(GET_TIME_TRACK_BY_EMPLOYEE_ID_URL, params={"employeeId": employee_id}).json()


def delete_time_track(time_track_id):
    requests.delete(DELETE_TIME_TRACK_URL, params={"timeTrackId": time_track_id})
