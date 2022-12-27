from datetime import datetime
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, NORMAL, DISABLED

import requests

ASSETS_PATH = "assets/frame0"

# SUCCESS

SUCCESS_CREATED_TIME_TRACK = "\nSUCCESSFULLY CREATED TIME TRACK"
SUCCESS_UPDATED_TIME_TRACK = "\nSUCCESSFULLY UPDATED TIME TRACK"

# ERRORS

INVALID_EMPLOYEE_ID_ERROR = "\nINVALID EMP ID"
INVALID_TIME_TRACK_ID_ERROR = "\nINVALID TT ID"
INVALID_CHECK_OUT_TIME_ERROR = "\nINVALID CO"
INVALID_CHECK_IN_TIME_ERROR = "\nINVALID CI"

# URL

UPDATE_TIME_TRACK_URL = "http://localhost:8080/updateTimeTrack/"
GET_TIME_TRACK_BY_EMPLOYEE_ID_URL = "http://localhost:8080/getTimeTrackByEmployeeId/"
GET_TIME_TRACK_BY_ID_URL = "http://localhost:8080/getTimeTrackById/"
GET_ALL_TIME_TRACKS_URL = "http://localhost:8080/getAllTimeTracks"
CREATE_TIME_TRACK_URL = "http://localhost:8080/createTimeTrack"
GET_WORKED_HOURS_BY_ID_URL = "http://localhost:8080/getHourlyRateById/"
GET_EMPLOYEE_BY_ID_URL = "http://localhost:8080/getEmployeeById/"
GET_ALL_EMPLOYEES_URL = "http://localhost:8080/getEmployees"


# TIME TRACK METHODS

def create_time_track():
    if is_employee_id_valid():
        if is_check_in_time_valid():
            if is_check_out_time_valid():
                time_track = {
                    "checkInTime": check_in_time_entry.get(),
                    "checkOutTime": check_out_time_entry.get(),
                    "employeeId": employee_id_entry.get()
                }
                response = requests.post(CREATE_TIME_TRACK_URL, json=time_track)
                if response.status_code == 200:
                    clear_output()
                    print_to_output_text_area(SUCCESS_CREATED_TIME_TRACK)
                else:
                    print_to_error_text_area("Error " + str(response.status_code))
            else:
                print_to_error_text_area(INVALID_CHECK_OUT_TIME_ERROR)
        else:
            print_to_error_text_area(INVALID_CHECK_IN_TIME_ERROR)
    else:
        print_to_error_text_area(INVALID_EMPLOYEE_ID_ERROR)


def update_time_track():
    if is_employee_id_valid():
        if is_check_in_time_valid():
            if is_check_out_time_valid():
                if is_time_track_id_valid():
                    time_track = {
                        "checkInTime": check_in_time_entry.get(),
                        "checkOutTime": check_out_time_entry.get(),
                        "employeeId": employee_id_entry.get()
                    }
                    response = requests.put(UPDATE_TIME_TRACK_URL + time_track_id_entry.get(), json=time_track)
                    if response.status_code == 200:
                        clear_output()
                        print_to_output_text_area(SUCCESS_UPDATED_TIME_TRACK)
                    else:
                        print_to_error_text_area("Error " + str(response.status_code))
                else:
                    print_to_error_text_area(INVALID_TIME_TRACK_ID_ERROR)
            else:
                print_to_error_text_area(INVALID_CHECK_OUT_TIME_ERROR)
        else:
            print_to_error_text_area(INVALID_CHECK_IN_TIME_ERROR)
    else:
        print_to_error_text_area(INVALID_EMPLOYEE_ID_ERROR)


def get_time_track_by_id():
    if is_time_track_id_valid():
        response = requests.get(GET_TIME_TRACK_BY_ID_URL + time_track_id_entry.get())
        if response.status_code == 200:
            print_time_track_list(response.json())
        else:
            print_to_error_text_area("Error " + str(response.status_code))
    else:
        print_to_error_text_area(INVALID_TIME_TRACK_ID_ERROR)


def get_time_tracks_by_employee_id():
    if is_employee_id_valid():
        response = requests.get(GET_TIME_TRACK_BY_EMPLOYEE_ID_URL + employee_id_entry.get())
        if response.status_code == 200:
            clear_output()
            print_time_track_list(response.json())
        else:
            print_to_error_text_area("Error " + str(response.status_code))
    else:
        print_to_error_text_area(INVALID_EMPLOYEE_ID_ERROR)


# AUXILIARY METHODS

def print_time_track_list(time_track_list):
    enable_text_areas()
    for time_track in time_track_list:
        employee = requests.get(GET_EMPLOYEE_BY_ID_URL + time_track.get('employeeId')).json()
        string_to_print = f"  Time Track ID: {time_track.get('timeTrackId')}\n" \
                          f"  Check In Time: {time_track.get('checkInTime')}\n" \
                          f"  Check Out Time: {time_track.get('checkOutTime')}\n" \
                          f"  Employee ID: {time_track.get('employeeId')}\n" \
                          f"  Employee First Name: {employee[0].get('employeeFirstName')}\n" \
                          f"  Employee Last Name: {employee[0].get('employeeLastName')}\n" \
                          f"########################################\n"
        output_text_area.insert(END, string_to_print)
    result_text_area.insert(END, str(len(time_track_list)))
    disable_text_areas()


def print_to_output_text_area(text):
    output_text_area.config(state=NORMAL)
    output_text_area.insert(END, text)
    output_text_area.config(state=DISABLED)


def print_to_error_text_area(text):
    error_text_area.config(state=NORMAL)
    error_text_area.delete('1.0', END)
    error_text_area.insert(END, text)
    error_text_area.config(state=DISABLED)


def now_time_check_in():
    check_in_time_entry.delete(0, END)
    check_in_time_entry.insert(0, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))


def now_time_check_out():
    check_out_time_entry.delete(0, END)
    check_out_time_entry.insert(0, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))


def clear_inputs():
    employee_id_entry.delete(0, END)
    check_in_time_entry.delete(0, END)
    check_out_time_entry.delete(0, END)
    time_track_id_entry.delete(0, END)


def clear_output():
    enable_text_areas()
    output_text_area.delete('1.0', END)
    error_text_area.delete('1.0', END)
    result_text_area.delete('1.0', END)
    disable_text_areas()


def disable_text_areas():
    output_text_area.config(state=DISABLED)
    result_text_area.config(state=DISABLED)
    error_text_area.config(state=DISABLED)


def enable_text_areas():
    output_text_area.config(state=NORMAL)
    error_text_area.config(state=NORMAL)
    result_text_area.config(state=NORMAL)


# VALIDATION

def is_employee_id_valid():
    if employee_id_entry.get() == '':
        return False
    else:
        return True


def is_check_in_time_valid():
    if check_in_time_entry.get() == '':
        return False
    else:
        return True


def is_check_out_time_valid():
    if check_out_time_entry.get() == '':
        return False
    else:
        return True


def is_time_track_id_valid():
    if time_track_id_entry.get() == '':
        return False
    else:
        return True


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x642")
window.configure(bg="#D9DCD6")

canvas = Canvas(
    window,
    bg="#D9DCD6",
    height=642,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    239.0,
    13.0,
    anchor="nw",
    text="Create Time Track",
    fill="#000000",
    font=("Inter Bold", 36 * -1)
)

canvas.create_text(
    46.0,
    77.0,
    anchor="nw",
    text="Employee ID",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    581.0,
    341.0,
    anchor="nw",
    text="Error",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    568.0,
    407.0,
    anchor="nw",
    text="Result",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    27.0,
    143.0,
    anchor="nw",
    text="Check In Time",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    10.0,
    209.0,
    anchor="nw",
    text="Check Out Time",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    33.0,
    275.0,
    anchor="nw",
    text="Time Track ID",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    480.0,
    89.0,
    image=entry_image_1
)
employee_id_entry = Entry(
    bd=0,
    bg="#81C3D7",
    fg="#000716",
    highlightthickness=0
)
employee_id_entry.place(
    x=180.0,
    y=74.0,
    width=600.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    405.0,
    155.0,
    image=entry_image_2
)
check_in_time_entry = Entry(
    bd=0,
    bg="#81C3D7",
    fg="#000716",
    highlightthickness=0
)
check_in_time_entry.place(
    x=180.0,
    y=140.0,
    width=450.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    405.0,
    221.0,
    image=entry_image_3
)
check_out_time_entry = Entry(
    bd=0,
    bg="#81C3D7",
    fg="#000716",
    highlightthickness=0
)
check_out_time_entry.place(
    x=180.0,
    y=206.0,
    width=450.0,
    height=28.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    480.0,
    287.0,
    image=entry_image_4
)
time_track_id_entry = Entry(
    bd=0,
    bg="#81C3D7",
    fg="#000716",
    highlightthickness=0
)
time_track_id_entry.place(
    x=180.0,
    y=272.0,
    width=600.0,
    height=28.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    711.5,
    353.0,
    image=entry_image_5
)
error_text_area = Text(
    bd=0,
    bg="#81C3D7",
    fg="#000716",
    highlightthickness=0
)
error_text_area.place(
    x=643.0,
    y=338.0,
    width=137.0,
    height=28.0
)
error_text_area.config(state=DISABLED)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    205.0,
    485.0,
    image=entry_image_6
)
output_text_area = Text(
    bd=0,
    bg="#81C3D7",
    fg="#000716",
    highlightthickness=0
)
output_text_area.place(
    x=10.0,
    y=338.0,
    width=390.0,
    height=292.0
)
output_text_area.config(state=DISABLED)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    711.5,
    419.0,
    image=entry_image_7
)
result_text_area = Text(
    bd=0,
    bg="#81C3D7",
    fg="#000716",
    highlightthickness=0
)
result_text_area.place(
    x=643.0,
    y=404.0,
    width=137.0,
    height=28.0
)
result_text_area.config(state=DISABLED)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: now_time_check_out(),
    relief="flat"
)
button_1.place(
    x=643.0,
    y=206.0,
    width=137.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear_inputs(),
    relief="flat"
)
button_2.place(
    x=415.0,
    y=602.0,
    width=137.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear_output(),
    relief="flat"
)
button_3.place(
    x=643.0,
    y=602.0,
    width=137.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_time_tracks_by_employee_id(),
    relief="flat"
)
button_4.place(
    x=415.0,
    y=470.0,
    width=367.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_time_track_by_id(),
    relief="flat"
)
button_5.place(
    x=415.0,
    y=536.0,
    width=367.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: create_time_track(),
    relief="flat"
)
button_6.place(
    x=415.0,
    y=338.0,
    width=137.0,
    height=30.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_time_track(),
    relief="flat"
)
button_7.place(
    x=415.0,
    y=404.0,
    width=137.0,
    height=30.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: now_time_check_in(),
    relief="flat"
)
button_8.place(
    x=643.0,
    y=140.0,
    width=137.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()
