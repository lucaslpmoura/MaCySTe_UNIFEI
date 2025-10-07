import tkinter as tk
from tkinter import messagebox

import subprocess

hasStarted = False

def start_macyste():
    disable_buttons()
    start_button["text"] = "Starting..."
    print('Starting Macyste...')

    subprocess.run(["make", "up"])
    print("Macyste Started.")
    global hasStarted
    hasStarted = True

  
    print("Opening User GUI..")
    subprocess.run(["make", "open-home"])
    print("Starting Bridge Command....")
    subprocess.run(["make", "run-bc"])
    toggle_buttons()

def stop_macyste():
    disable_buttons()
    stop_button["text"] = "Stopping..."
    

    print("Stopping Macyste...")
    subprocess.run(["make", "down"])
    global hasStarted
    hasStarted = False

    print("Macyste Stopped.")
    toggle_buttons()

def toggle_buttons():
    if hasStarted:
        start_button["state"] = "disabled"
        start_button["text"] = "Started"

        stop_button["text"] = "Stop Macyste"
        stop_button["state"] = "normal"
    else:
        start_button["state"] = "normal"
        start_button["text"] = "Start Macyste"

        stop_button["text"] =  "Stopped"
        stop_button["state"] = "disabled"

def disable_buttons():
    start_button["state"] = "disabled"
    stop_button["state"] = "disabled"

def quit():
    if hasStarted:
        messagebox.showerror(message="Please stop the simulator before closing the GUI")
    else:
        window.destroy()


window = tk.Tk()
window.title("Macyste UNIFEI GUI")
#tk.Button(window, text="Quit", command=window.destroy).pack()
window.protocol("WM_DELETE_WINDOW", quit)
window.geometry("300x150")

start_button = tk.Button(window, text="Start Macyste", 
                          command=start_macyste, 
                          width=20, height=2, bg="green", fg="white")
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Macyste", command=stop_macyste, width=20, height=2, bg="red", fg="white")
stop_button.pack(pady=10)

toggle_buttons()
window.mainloop()
