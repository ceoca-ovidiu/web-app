import re
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, DISABLED, NORMAL
from datetime import datetime

import requests

# CONSTANTS

BUTTON_HEIGHT = 33
BUTTON_WIDTH = 260
SUBMIT_BUTTON_WIDTH = 150
SMALL_TEXT_AREA_WIDTH = 175
SMALL_TEXT_AREA_HEIGHT = 31

# URLs

GET_ALL_EMPLOYEES_URL = "http://localhost:8080/getEmployees"
CREATE_EMPLOYEE_URL = "http://localhost:8080/createEmployee"
GET_EMPLOYEE_BY_FIRST_NAME_URL = "http://localhost:8080/getEmployeesByFirstName/"
GET_EMPLOYEE_BY_PLACE_URL = "http://localhost:8080/getEmployeesByPlace/"
GET_EMPLOYEE_BY_ID_URL = "http://localhost:8080/getEmployeeById/"
DELETE_EMPLOYEE_BY_ID_URL = "http://localhost:8080/deleteEmployee/"
GET_EMPLOYEE_BY_GENDER_URL = "http://localhost:8080/getEmployeesByGender/"
GET_EMPLOYEE_BY_EMAIL_URL = "http://localhost:8080/getEmployeesByEmail/"
UPDATE_EMPLOYEE_BY_ID_URL = "http://localhost:8080/updateEmployee/"
GET_WORKED_HOURS_BY_ID_URL = "http://localhost:8080/getHourlyRateById/"
GET_ALL_TIME_TRACKS_URL = "http://localhost:8080/getAllTimeTracks"
CREATE_TIME_TRACK_URL = "http://localhost:8080/createTimeTrack"
GET_TIME_TRACK_BY_EMPLOYEE_ID_URL = "http://localhost:8080/getTimeTrackByEmployeeId/"
GET_TIME_TRACK_BY_ID_URL = "http://localhost:8080/getTimeTrackById/"
DELETE_TIME_TRACK_URL = "http://localhost:8080/deleteTimeTrack/"
UPDATE_TIME_TRACK_URL = "http://localhost:8080/updateTimeTrack/"


# FUNCTIONS
def get_all_employees():
    clear_output()
    print_employee_list(requests.get(GET_ALL_EMPLOYEES_URL).json())


def get_employees_by_first_name():
    if check_input():
        clear_output()
        print_employee_list(requests.get(GET_EMPLOYEE_BY_FIRST_NAME_URL + input_entry.get()).json())
    else:
        print_to_error_text_area("\nINPUT EMPTY")


def get_employees_by_place():
    if check_input():
        clear_output()
        print_employee_list(requests.get(GET_EMPLOYEE_BY_PLACE_URL + input_entry.get()).json())
    else:
        print_to_error_text_area("\nINPUT EMPTY")


def get_employees_by_email():
    if check_input():
        clear_output()
        print_employee_list(requests.get(GET_EMPLOYEE_BY_EMAIL_URL + input_entry.get()).json())
    else:
        print_to_error_text_area("\nINPUT EMPTY")


def get_employees_by_gender():
    if check_input():
        clear_output()
        print_employee_list(requests.get(GET_EMPLOYEE_BY_GENDER_URL + input_entry.get()).json())
    else:
        print_to_error_text_area("\nINPUT EMPTY")


def get_employee_by_id():
    if check_input():
        clear_output()
        print_employee_list(requests.get(GET_EMPLOYEE_BY_ID_URL + input_entry.get()).json())
    else:
        print_to_error_text_area("\nINPUT EMPTY")


def delete_employee_by_id():
    if check_input():
        clear_output()
        print_employee_list(requests.get(GET_EMPLOYEE_BY_ID_URL + input_entry.get()).json())
        requests.delete(DELETE_EMPLOYEE_BY_ID_URL + input_entry.get())
        output_textarea.insert(END, "\n\nSUCCESSFULLY DELETED EMPLOYEE ABOVE")
    else:
        print_to_error_text_area("\nINPUT EMPTY")


def create_employee():
    clear_output()
    if check_employee_first_name():
        if check_employee_last_name():
            if check_employee_email():
                if check_email_duplicates():
                    if check_employee_place():
                        if check_employee_gender():
                            employee = {"employeeFirstName": add_employee_first_name_entry.get(),
                                        "employeeLastName": add_employee_last_name_entry.get(),
                                        "employeeEmail": add_employee_email_entry.get(),
                                        "employeePlace": add_employee_place_entry.get(),
                                        "employeeGender": add_employee_gender_entry.get()}
                            requests.post(CREATE_EMPLOYEE_URL, json=employee)
                            output_textarea.config(state=NORMAL)
                            output_textarea.insert(END, "\nSUCCESSFULLY ADDED EMPLOYEE")
                            output_textarea.config(state=DISABLED)
                            clear_employee_input_fields()
                        else:
                            print_to_error_text_area("\nGender")
                    else:
                        print_to_error_text_area("\nPlace")
                else:
                    print_to_error_text_area("\nDuplicate Email")
            else:
                print_to_error_text_area("\nEmail")
        else:
            print_to_error_text_area("\nLast Name")
    else:
        print_to_error_text_area("\nFirst Name")


def print_to_error_text_area(message):
    error_textarea.config(state=NORMAL)
    error_textarea.delete('1.0', END)
    error_textarea.insert(END, message)
    error_textarea.config(state=DISABLED)


def get_all_time_track():
    clear_output()
    output_textarea.delete('1.0', END)
    print_time_track_list(requests.get(GET_ALL_TIME_TRACKS_URL).json())


def create_time_track():
    clear_output()
    if check_time_track_employee_id():
        if check_time_track_check_in():
            if check_time_track_check_out():
                time_track = {
                    "checkInTime": time_track_check_in_entry.get(),
                    "checkOutTime": time_track_check_out_entry.get(),
                    "employeeId": time_track_employee_id_entry.get()
                }
                requests.post(CREATE_TIME_TRACK_URL, json=time_track)
                string_to_print = "\nSUCCESSFULLY CREATED TIME TRACK FOR EMPLOYEE: " + time_track_employee_id_entry.get()
                output_textarea.config(state=NORMAL)
                output_textarea.insert(END, string_to_print)
                output_textarea.config(state=DISABLED)
                clear_time_track_input_fields()
            else:
                print_to_error_text_area("\nWRONG CHECK OUT")
        else:
            print_to_error_text_area("\nWRONG CHECK IN")
    else:
        print_to_error_text_area("\nWRONG ID")


def get_time_track_by_employee_id():
    if check_input():
        clear_output()
        print_time_track_list(requests.get(GET_TIME_TRACK_BY_EMPLOYEE_ID_URL + input_entry.get()).json())
    else:
        print_to_error_text_area("\nINPUT EMPTY")


def get_time_track_by_id():
    if check_input():
        clear_output()
        print_time_track_list(requests.get(GET_TIME_TRACK_BY_ID_URL + input_entry.get()).json())
    else:
        print_to_error_text_area("\nINPUT EMPTY")


def delete_time_track():
    if check_input():
        clear_output()
        print_time_track_list(requests.get(GET_TIME_TRACK_BY_ID_URL + input_entry.get()).json())
        requests.delete(DELETE_TIME_TRACK_URL + input_entry.get())
        output_textarea.insert(END, "\n\nSUCCESSFULLY DELETED TIME TRACK ABOVE")
    else:
        print_to_error_text_area("\nINPUT EMPTY")


def clear_output():
    enable_text_areas()
    output_textarea.delete('1.0', END)
    clear_error()
    clear_result()
    disable_text_areas()


def clear_result():
    enable_text_areas()
    result_textarea.delete('1.0', END)
    disable_text_areas()


def clear_error():
    enable_text_areas()
    error_textarea.delete('1.0', END)
    disable_text_areas()


def clear_employee_input_fields():
    add_employee_gender_entry.delete(0, END)
    add_employee_place_entry.delete(0, END)
    add_employee_email_entry.delete(0, END)
    add_employee_last_name_entry.delete(0, END)
    add_employee_first_name_entry.delete(0, END)


def clear_time_track_input_fields():
    time_track_employee_id_entry.delete(0, END)
    time_track_check_in_entry.delete(0, END)
    time_track_check_out_entry.delete(0, END)


def clear_inputs():
    add_employee_gender_entry.delete(0, END)
    add_employee_place_entry.delete(0, END)
    add_employee_email_entry.delete(0, END)
    add_employee_last_name_entry.delete(0, END)
    add_employee_first_name_entry.delete(0, END)
    input_entry.delete(0, END)
    time_track_check_in_entry.delete(0, END)
    time_track_employee_id_entry.delete(0, END)
    time_track_check_out_entry.delete(0, END)


def clear_all():
    enable_text_areas()
    clear_output()
    clear_inputs()
    disable_text_areas()


def disable_text_areas():
    output_textarea.config(state=DISABLED)
    result_textarea.config(state=DISABLED)
    error_textarea.config(state=DISABLED)


def enable_text_areas():
    output_textarea.config(state=NORMAL)
    result_textarea.config(state=NORMAL)
    error_textarea.config(state=NORMAL)


def print_employee_list(employee_list):
    enable_text_areas()
    for employee in employee_list:
        string_to_print = f"  ID: {employee.get('id')}\n" \
                          f"  First Name: {employee.get('employeeFirstName')}\n" \
                          f"  Last Name: {employee.get('employeeLastName')}\n" \
                          f"  Email: {employee.get('employeeEmail')}\n" \
                          f"  Place: {employee.get('employeePlace')}\n" \
                          f"  Gender: {employee.get('employeeGender')}\n"
        output_textarea.insert(END, string_to_print)
        output_textarea.insert(END, requests.get(GET_WORKED_HOURS_BY_ID_URL + employee.get('id')).text)
        output_textarea.insert(END, "\n########################################\n")
    result_textarea.insert(END, str(len(employee_list)))
    disable_text_areas()


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
        output_textarea.insert(END, string_to_print)
    result_textarea.insert(END, str(len(time_track_list)))
    disable_text_areas()


def now_time_check_in():
    time_track_check_in_entry.delete(0, END)
    time_track_check_in_entry.insert(0, datetime.now().strftime("%Y-%d-%mT%H:%M:%S"))
    pass


def now_time_check_out():
    time_track_check_out_entry.delete(0, END)
    time_track_check_out_entry.insert(0, datetime.now().strftime("%Y-%d-%mT%H:%M:%S"))
    pass


def update_employee():
    clear_output()
    if check_input():
        if check_employee_first_name():
            if check_employee_last_name():
                if check_employee_email():
                    if check_email_duplicates():
                        if check_employee_place():
                            if check_employee_gender():
                                employee = {"employeeFirstName": add_employee_first_name_entry.get(),
                                            "employeeLastName": add_employee_last_name_entry.get(),
                                            "employeeEmail": add_employee_email_entry.get(),
                                            "employeePlace": add_employee_place_entry.get(),
                                            "employeeGender": add_employee_gender_entry.get()}
                                requests.put(UPDATE_EMPLOYEE_BY_ID_URL + input_entry.get(), json=employee)
                                output_textarea.config(state=NORMAL)
                                output_textarea.insert(END, "\nSUCCESSFULLY ADDED EMPLOYEE")
                                output_textarea.config(state=DISABLED)
                                clear_employee_input_fields()
                            else:
                                print_to_error_text_area("\nGender")
                        else:
                            print_to_error_text_area("\nPlace")
                    else:
                        print_to_error_text_area("\nDuplicate Email")
                else:
                    print_to_error_text_area("\nEmail")
            else:
                print_to_error_text_area("\nLast Name")
        else:
            print_to_error_text_area("\nFirst Name")
    else:
        print_to_error_text_area("INVALID ID")


def update_time_track():
    clear_output()
    if check_input():
        if check_time_track_employee_id():
            if check_time_track_check_in():
                if check_time_track_check_out():
                    time_track = {
                        "checkInTime": time_track_check_in_entry.get(),
                        "checkOutTime": time_track_check_out_entry.get(),
                        "employeeId": time_track_employee_id_entry.get()
                    }
                    requests.post(UPDATE_TIME_TRACK_URL + input_entry.get(), json=time_track)
                    string_to_print = "\nSUCCESSFULLY UPDATED TIME TRACK FOR EMPLOYEE: " + time_track_employee_id_entry.get()
                    output_textarea.config(state=NORMAL)
                    output_textarea.insert(END, string_to_print)
                    output_textarea.config(state=DISABLED)
                    clear_time_track_input_fields()
                else:
                    print_to_error_text_area("\nWRONG CHECK OUT")
            else:
                print_to_error_text_area("\nWRONG CHECK IN")
        else:
            print_to_error_text_area("\nWRONG ID")
    else:
        print_to_error_text_area("INVALID ID")


# EMPLOYEE VALIDATION

def check_employee_first_name():
    if add_employee_first_name_entry.get() == '':
        return False
    return add_employee_first_name_entry.get().isalpha()


def check_employee_last_name():
    if add_employee_last_name_entry.get() == '':
        return False
    print(add_employee_last_name_entry.get().isalpha())
    return add_employee_last_name_entry.get().isalpha()


def check_employee_email():
    employee_email = add_employee_email_entry.get()
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if employee_email == '':
        return False
    return re.fullmatch(regex, employee_email)


def check_employee_place():
    if add_employee_place_entry.get() == '':
        return False
    return add_employee_place_entry.get().isalpha()


def check_employee_gender():
    if add_employee_gender_entry.get() == '':
        return False
    if add_employee_gender_entry.get() == "MALE" or add_employee_gender_entry.get() == "FEMALE":
        return True
    return False


def check_email_duplicates():
    employee_list = requests.get(GET_EMPLOYEE_BY_EMAIL_URL + add_employee_email_entry.get()).json()
    if len(employee_list) != 0:
        return False
    return True


# TIME TRACK VALIDATION

def check_time_track_employee_id():
    if time_track_employee_id_entry.get() == '':
        return False
    employee_list = requests.get(GET_EMPLOYEE_BY_ID_URL + time_track_employee_id_entry.get()).json()
    if len(employee_list) == 0:
        return False
    return True


def check_time_track_check_in():
    if time_track_check_in_entry.get() == '':
        return False
    return True


def check_time_track_check_out():
    if time_track_check_out_entry.get() == '':
        return False
    return True


def check_input():
    if input_entry.get() == '':
        return False
    return True


# FRAME


window = Tk()
window.geometry("1200x900")
window.configure(bg="#F2E8CF")

# CANVAS

canvas = Canvas(window, bg="#F2E8CF", height=900, width=1200, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
canvas.create_rectangle(20.0, 20.0, 470.0, 520.0, fill="#A7C957", outline="")
canvas.create_rectangle(19.0, 530.0, 470.0, 880.0, fill="#A7C957", outline="")

# BUTTONS

add_employee_submit_button = Button(text="Submit", borderwidth=0, highlightthickness=0,
                                    command=lambda: create_employee(),
                                    relief="flat")
add_employee_submit_button.place(x=170.0, y=474.0, width=SUBMIT_BUTTON_WIDTH, height=BUTTON_HEIGHT)

create_time_track_submit_button = Button(text="Submit", borderwidth=0, highlightthickness=0,
                                         command=lambda: create_time_track(),
                                         relief="flat")
create_time_track_submit_button.place(x=170.0, y=833.0, width=SUBMIT_BUTTON_WIDTH, height=BUTTON_HEIGHT)

get_employees_by_first_name_button = Button(text="Get Employees By First Name", borderwidth=0, highlightthickness=0,
                                            command=lambda: get_employees_by_first_name(),
                                            relief="flat")
get_employees_by_first_name_button.place(x=500.0, y=73.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

get_all_employees_button = Button(text="Get All Employees", borderwidth=0, highlightthickness=0,
                                  command=lambda: get_all_employees(),
                                  relief="flat")
get_all_employees_button.place(x=500.0, y=131.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

get_all_time_tracks_button = Button(text="Get All Time Tracks", borderwidth=0, highlightthickness=0,
                                    command=lambda: get_all_time_track(),
                                    relief="flat")
get_all_time_tracks_button.place(x=900.0, y=73.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

get_time_track_by_id_button = Button(text="Get Time Track By ID", borderwidth=0, highlightthickness=0,
                                     command=lambda: get_time_track_by_id(),
                                     relief="flat")
get_time_track_by_id_button.place(x=900.0, y=131.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

get_time_track_by_empl_id_button = Button(text="Get Time Track By Employee ID", borderwidth=0, highlightthickness=0,
                                          command=lambda: get_time_track_by_employee_id(),
                                          relief="flat")
get_time_track_by_empl_id_button.place(x=900.0, y=189.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

delete_time_track_by_id_button = Button(text="Delete Time Track By ID", borderwidth=0, highlightthickness=0,
                                        command=lambda: delete_time_track(),
                                        relief="flat")
delete_time_track_by_id_button.place(x=900.0, y=247.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

clear_output_button = Button(text="Clear Output", borderwidth=0, highlightthickness=0,
                             command=lambda: clear_output(),
                             relief="flat")
clear_output_button.place(x=900.0, y=305.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

clear_inputs_button = Button(text="Clear Inputs", borderwidth=0, highlightthickness=0,
                             command=lambda: clear_inputs(), relief="flat")
clear_inputs_button.place(x=900.0, y=363.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

clear_all_button = Button(text="Clear All", borderwidth=0, highlightthickness=0,
                          command=lambda: clear_all(), relief="flat")
clear_all_button.place(x=900.0, y=421.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

get_employees_by_email_button = Button(text="Get Employees By Email", borderwidth=0, highlightthickness=0,
                                       command=lambda: get_employees_by_email(), relief="flat")
get_employees_by_email_button.place(x=500.0, y=189.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

get_employees_by_place_button = Button(text="Get Employees By Place", borderwidth=0, highlightthickness=0,
                                       command=lambda: get_employees_by_place(), relief="flat")
get_employees_by_place_button.place(x=500.0, y=247.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

get_employee_by_id_button = Button(text="Get Employee By ID", borderwidth=0, highlightthickness=0,
                                   command=lambda: get_employee_by_id(), relief="flat")
get_employee_by_id_button.place(x=500.0, y=305.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

get_employees_by_gender_button = Button(text="Get Employees By Gender", borderwidth=0, highlightthickness=0,
                                        command=lambda: get_employees_by_gender(), relief="flat")
get_employees_by_gender_button.place(x=500.0, y=363.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

delete_employee_by_id_button = Button(text="Delete Employee By ID", borderwidth=0, highlightthickness=0,
                                      command=lambda: delete_employee_by_id(), relief="flat")
delete_employee_by_id_button.place(x=500.0, y=421.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

now_time_check_in_button = Button(text="T", borderwidth=0, highlightthickness=0,
                                  command=lambda: now_time_check_in(), relief="flat")
now_time_check_in_button.place(x=430.0, y=700.0, width=30, height=BUTTON_HEIGHT)

now_time_check_out_button = Button(text="T", borderwidth=0, highlightthickness=0,
                                   command=lambda: now_time_check_out(), relief="flat")
now_time_check_out_button.place(x=430.0, y=780.0, width=30, height=BUTTON_HEIGHT)

update_employee_button = Button(text="Update Employee", borderwidth=0, highlightthickness=0,
                                command=lambda: update_employee(), relief="flat")
update_employee_button.place(x=500.0, y=840.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

update_time_track_button = Button(text="Update Time Track", borderwidth=0, highlightthickness=0,
                                  command=lambda: update_time_track(), relief="flat")
update_time_track_button.place(x=900.0, y=840.0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# ENTRY

add_employee_first_name_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_first_name_entry.place(x=70.0, y=91.0, width=350.0, height=48.0)

input_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
input_entry.place(x=480.0, y=20.0, width=700.0, height=31.0)

add_employee_last_name_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_last_name_entry.place(x=70.0, y=171.0, width=350.0, height=48.0)

add_employee_email_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_email_entry.place(x=70.0, y=251.0, width=350.0, height=48.0)

add_employee_place_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_place_entry.place(x=70.0, y=331.0, width=350.0, height=48.0)

add_employee_gender_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_gender_entry.place(x=70.0, y=412.0, width=350.0, height=48.0)

time_track_employee_id_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
time_track_employee_id_entry.place(x=68.0, y=611.0, width=350.0, height=48.0)

time_track_check_in_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
time_track_check_in_entry.place(x=68.0, y=691.0, width=350.0, height=48.0)
time_track_check_in_entry.insert(0, "YYYY-DD-MMTHH:MM:SS.000")

time_track_check_out_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
time_track_check_out_entry.place(x=68.0, y=771.0, width=350.0, height=48.0)
time_track_check_out_entry.insert(0, "YYYY-DD-MMTHH:MM:SS.000")

# TEXTAREAS

output_textarea = Text(bd=0, bg="#A7C957", fg="#000716", highlightthickness=0)
output_textarea.place(x=480.0, y=530.0, width=700.0, height=300.0)
output_textarea.config(state=DISABLED)

error_textarea = Text(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
error_textarea.place(x=557.0, y=487.0, width=SMALL_TEXT_AREA_WIDTH, height=SMALL_TEXT_AREA_HEIGHT)
error_textarea.config(state=DISABLED)

result_textarea = Text(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
result_textarea.place(x=1005.0, y=487.0, width=SMALL_TEXT_AREA_WIDTH, height=SMALL_TEXT_AREA_HEIGHT)
result_textarea.config(state=DISABLED)

# TEXT

canvas.create_text(480.0, 487.0, anchor="nw", text="ERROR", fill="#000000", font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(923.0, 487.0, anchor="nw", text="RESULT", fill="#000000", font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(70.0, 64.0, anchor="nw", text="First Name", fill="#000000", font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(70.0, 144.0, anchor="nw", text="Last Name", fill="#000000", font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(70.0, 224.0, anchor="nw", text="Email", fill="#000000", font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(70.0, 304.0, anchor="nw", text="Place", fill="#000000", font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(70.0, 384.0, anchor="nw", text="Gender (MALE/FEMALE)", fill="#000000",
                   font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(70.0, 584.0, anchor="nw", text="Employee ID", fill="#000000", font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(70.0, 664.0, anchor="nw", text="Check in (YYYY-DD-MMTHH:MM:SS.000)", fill="#000000",
                   font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(70.0, 744.0, anchor="nw", text="Check out (YYYY-DD-MMTHH:MM:SS.000)", fill="#000000",
                   font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(171.0, 30.0, anchor="nw", text="Add Employee", fill="#000000", font=("MuktaMalar Medium", 24 * -1))
canvas.create_text(150.0, 541.0, anchor="nw", text="Create Time Track", fill="#000000",
                   font=("MuktaMalar Medium", 24 * -1))
# RECTANGLES

canvas.create_rectangle(477, 60.0, 1180.0, 63.0, fill="#386641", outline="")
canvas.create_rectangle(827, 70.0, 830.0, 477.0, fill="#386641", outline="")
canvas.create_rectangle(837, 292.0, 1180.0, 295.0, fill="#386641", outline="")

window.resizable(False, False)
window.mainloop()
