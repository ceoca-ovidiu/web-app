from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END
import employee_requests as er
import time_track_requests as ttr

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
add_employee_submit_button = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                                    command=er.create_employee(),
                                    relief="flat")
add_employee_submit_button.place(x=170.0, y=474.0, width=150.0, height=33.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
create_time_track_submit_button = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                                         command=ttr.create_time_track(),
                                         relief="flat")
create_time_track_submit_button.place(x=150.0, y=833.0, width=150.0, height=33.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
get_employees_by_first_name_button = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                                            command=lambda: print("button_3 clicked"),
                                            relief="flat")
get_employees_by_first_name_button.place(x=500.0, y=73.0, width=260.0, height=35.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
get_all_employees_button = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                                  command=lambda: print("button_4 clicked"),
                                  relief="flat")
get_all_employees_button.place(x=500.0, y=131.0, width=260.0, height=35.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
get_all_time_tracks_button = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                                    command=lambda: print("button_5 clicked"),
                                    relief="flat")
get_all_time_tracks_button.place(x=900.0, y=73.0, width=260.0, height=35.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
get_time_track_by_id_button = Button(image=button_image_6, borderwidth=0, highlightthickness=0,
                                     command=lambda: print("button_6 clicked"),
                                     relief="flat")
get_time_track_by_id_button.place(x=900.0, y=131.0, width=260.0, height=35.0)

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
get_time_track_by_empl_id_button = Button(image=button_image_7, borderwidth=0, highlightthickness=0,
                                          command=lambda: print("button_7 clicked"),
                                          relief="flat")
get_time_track_by_empl_id_button.place(x=900.0, y=189.0, width=260.0, height=35.0)

button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
delete_time_track_by_id_button = Button(image=button_image_8, borderwidth=0, highlightthickness=0,
                                        command=lambda: print("button_8 clicked"),
                                        relief="flat")
delete_time_track_by_id_button.place(x=900.0, y=247.0, width=260.0, height=35.0)

button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
clear_output_button = Button(image=button_image_9, borderwidth=0, highlightthickness=0,
                             command=lambda: print("button_9 clicked"),
                             relief="flat")
clear_output_button.place(x=900.0, y=305.0, width=260.0, height=35.0)

button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
clear_inputs_button = Button(image=button_image_10, borderwidth=0, highlightthickness=0,
                             command=lambda: print("button_10 clicked"), relief="flat")
clear_inputs_button.place(x=900.0, y=363.0, width=260.0, height=35.0)

button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
clear_all_button = Button(image=button_image_11, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_11 clicked"), relief="flat")
clear_all_button.place(x=900.0, y=421.0, width=260.0, height=35.0)

button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))
get_employees_by_email_button = Button(image=button_image_12, borderwidth=0, highlightthickness=0,
                                       command=lambda: print("button_12 clicked"), relief="flat")
get_employees_by_email_button.place(x=500.0, y=189.0, width=260.0, height=35.0)

button_image_13 = PhotoImage(file=relative_to_assets("button_13.png"))
get_employees_by_place_button = Button(image=button_image_13, borderwidth=0, highlightthickness=0,
                                       command=lambda: print("button_13 clicked"), relief="flat")
get_employees_by_place_button.place(x=500.0, y=247.0, width=260.0, height=35.0)

button_image_14 = PhotoImage(file=relative_to_assets("button_14.png"))
get_employee_by_id_button = Button(image=button_image_14, borderwidth=0, highlightthickness=0,
                                   command=lambda: print("button_14 clicked"), relief="flat")
get_employee_by_id_button.place(x=500.0, y=305.0, width=260.0, height=35.0)

button_image_15 = PhotoImage(file=relative_to_assets("button_15.png"))
get_employees_by_gender_button = Button(image=button_image_15, borderwidth=0, highlightthickness=0,
                                        command=lambda: print("button_15 clicked"), relief="flat")
get_employees_by_gender_button.place(x=500.0, y=363.0, width=260.0, height=35.0)

button_image_16 = PhotoImage(file=relative_to_assets("button_16.png"))
delete_employee_by_id_button = Button(image=button_image_16, borderwidth=0, highlightthickness=0,
                                      command=lambda: print("button_16 clicked"), relief="flat")
delete_employee_by_id_button.place(x=500.0, y=421.0, width=260.0, height=35.0)

# ENTRY

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(830.0, 705.0, image=entry_image_1)
output_entry = Text(bd=0, bg="#A7C957", fg="#000716", highlightthickness=0)
output_entry.place(x=480.0, y=530.0, width=700.0, height=348.0)
output_entry.insert(END, "entry 1")

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(245.0, 116.0, image=entry_image_2)
add_employee_first_name_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_first_name_entry.place(x=70.0, y=91.0, width=350.0, height=48.0)
add_employee_first_name_entry.insert(END, "entry 2")

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(830.0, 36.5, image=entry_image_3)
input_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
input_entry.place(x=480.0, y=20.0, width=700.0, height=31.0)
input_entry.insert(END, "entry 3")

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(245.0, 196.0, image=entry_image_4)
add_employee_last_name_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_last_name_entry.place(x=70.0, y=171.0, width=350.0, height=48.0)
add_employee_last_name_entry.insert(END, "entry 4")

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(245.0, 276.0, image=entry_image_5)
add_employee_email_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_email_entry.place(x=70.0, y=251.0, width=350.0, height=48.0)
add_employee_email_entry.insert(END, "entry 5")

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(245.0, 356.0, image=entry_image_6)
add_employee_place_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_place_entry.place(x=70.0, y=331.0, width=350.0, height=48.0)
add_employee_place_entry.insert(END, "entry 6")

entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(245.0, 437.0, image=entry_image_7)
add_employee_gender_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
add_employee_gender_entry.place(x=70.0, y=412.0, width=350.0, height=48.0)
add_employee_gender_entry.insert(END, "entry 7")

entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(243.0, 636.0, image=entry_image_8)
time_track_employee_id_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
time_track_employee_id_entry.place(x=68.0, y=611.0, width=350.0, height=48.0)
time_track_employee_id_entry.insert(END, "entry 8")

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(243.0, 716.0, image=entry_image_9)
time_track_check_in_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
time_track_check_in_entry.place(x=68.0, y=691.0, width=350.0, height=48.0)
time_track_check_in_entry.insert(END, "entry 9")

entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(243.0, 796.0, image=entry_image_10)
time_track_check_out_entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
time_track_check_out_entry.place(x=68.0, y=771.0, width=350.0, height=48.0)
time_track_check_out_entry.insert(END, "entry 10")

entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(644.5, 503.5, image=entry_image_11)
error_entry = Text(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
error_entry.place(x=557.0, y=487.0, width=175.0, height=31.0)
error_entry.insert(END, "entry_11")

entry_image_12 = PhotoImage(file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(1092.5, 503.5, image=entry_image_12)
result_entry = Text(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
result_entry.place(x=1005.0, y=487.0, width=175.0, height=31.0)
result_entry.insert(END, "entry_12")

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
canvas.create_text(70.0, 664.0, anchor="nw", text="Check in time", fill="#000000", font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(70.0, 744.0, anchor="nw", text="Check out time", fill="#000000", font=("MuktaMalar Medium", 20 * -1))
canvas.create_text(171.0, 30.0, anchor="nw", text="Add Employee", fill="#000000", font=("MuktaMalar Medium", 24 * -1))
canvas.create_text(150.0, 541.0, anchor="nw", text="Create Time Track", fill="#000000",
                   font=("MuktaMalar Medium", 24 * -1))
# RECTANGLES

canvas.create_rectangle(477.0, 60.0, 1180.0, 63.0, fill="#386641", outline="")
canvas.create_rectangle(826.9999694824219, 70.0, 830.0, 477.0, fill="#386641", outline="")
canvas.create_rectangle(837.0, 292.0, 1180.0, 295.0, fill="#386641", outline="")

window.resizable(False, False)
window.mainloop()
