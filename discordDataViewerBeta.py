import os
import json
import csv
import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

def save_as_file(data_array):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                for item in data_array:
                    file.write(str(item) + '\n')
            print("Data saved successfully.")
        except IOError:
            print("Error: Unable to save data to the specified file path.")

def save_as_file_formated(data_array):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                for item in data_array:
                    file.write("<#" + str(item) + ">" + '\n')
            print("Data saved successfully.")
        except IOError:
            print("Error: Unable to save data to the specified file path.")

def open_file(file_path):
    try:
        os.startfile(file_path)
    except OSError:
        print(f"Error: Unable to open the file at {file_path}")

def create_left_frame_a(parent):
    left_frame = tk.Frame(parent)

    label1 = tk.Label(left_frame, text="Unzipped package location:")
    label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    entry1 = tk.Entry(left_frame, width=30)
    entry1.grid(row=1, column=0, padx=10, pady=10)

    label2 = tk.Label(left_frame, text="Your Discord user ID:")
    label2.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    entry2 = tk.Entry(left_frame, width=30)
    entry2.grid(row=3, column=0, padx=10, pady=10)

    run_button = tk.Button(left_frame, text="Run", command=run_page_a_get_dms)
    run_button.grid(row=4, column=0, pady=10)

    save_clean_button = tk.Button(left_frame, text="Save as file", command=save_dms_as)
    save_clean_button.grid(row=5, column=0, pady=10)

    save_formated_button = tk.Button(left_frame, text="Save as formated file <#id>", command=save_dms_as_formated)
    save_formated_button.grid(row=6, column=0, pady=10)

    return left_frame, entry1, entry2

def create_right_frame_a(parent):
    global output_text_a
    right_frame = tk.Frame(parent)

    output_label = tk.Label(right_frame, text="Output:")
    output_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    output_text_a = scrolledtext.ScrolledText(
        right_frame,
        wrap=tk.WORD,
        state=tk.DISABLED,
        width=40,
        height=10
    )
    output_text_a.grid(row=1, column=0, padx=10, pady=10)

    return right_frame, output_text_a

left_frame_a = None
entry1_a = None
entry2_a = None
output_text_a = None

def show_page_a():
    global left_frame_a, entry1_a, entry2_a, output_text_a

    page_a = tk.Toplevel(window)
    page_a.title("Get a list of all DMs")
    page_a.geometry("800x400")

    left_frame_a, entry1_a, entry2_a = create_left_frame_a(page_a)
    left_frame_a.pack(side=tk.LEFT, padx=10, pady=10)

    right_frame_a, output_text_a = create_right_frame_a(page_a)
    right_frame_a.pack(side=tk.LEFT, padx=10, pady=10)

def save_dms_as():
    run_page_a_get_dms(1)

def save_dms_as_formated():
    run_page_a_get_dms(2)

def run_page_a_get_dms(which_save):
    global totalDms, output_text_a

    file_location = entry1_a.get()
    user_id = entry2_a.get()

    totalDms = []

    for folder in os.listdir(file_location):
        folder_path = os.path.join(file_location, folder)
        channel_json_path = os.path.join(folder_path, 'channel.json')
        messages_path = os.path.join(folder_path, 'messages.csv')
        print("Folder Path:", folder_path)
        print("Channel JSON Path:", channel_json_path)
        print("Messages Path:", messages_path)

        if os.path.exists(channel_json_path):
            with open(channel_json_path, 'r', encoding='utf-8') as channel_file:
                channel_data = json.load(channel_file)
                print("Channel Data:", channel_data)

                if channel_data.get("type", 0) == 1 and channel_data.get("type", 11) != 11:
                    print("dm")
                    other_user_id = channel_data["recipients"][0] if channel_data["recipients"][0] != user_id else channel_data["recipients"][1]
                    totalDms.append(other_user_id)
                    print("Other User ID:", other_user_id)

    output_text_a.config(state=tk.NORMAL)
    output_text_a.delete(1.0, tk.END)
    output_text_a.insert(tk.END, f"Total DMs: {len(totalDms)}\n")
    for user in totalDms:
        output_text_a.insert(tk.END, f"{user}\n")
    output_text_a.config(state=tk.DISABLED)

    print("Other Users IDs:", totalDms)
    print("Running Page A")
    print("File Location:", file_location)
    print("User ID:", user_id)

    if(which_save == 1):
        save_as_file(totalDms)

    if(which_save == 2):
        save_as_file_formated(totalDms)

def create_left_frame_b(parent):
    global entry1_b, entry2_b
    left_frame = tk.Frame(parent)

    label1 = tk.Label(left_frame, text="Unzipped package location:")
    label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    entry1_b = tk.Entry(left_frame, width=30)
    entry1_b.grid(row=1, column=0, padx=10, pady=10)

    label2 = tk.Label(left_frame, text="Searched user ID:")
    label2.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    entry2_b = tk.Entry(left_frame, width=30)
    entry2_b.grid(row=3, column=0, padx=10, pady=10)

    run_button = tk.Button(left_frame, text="Run", command=run_page_b)
    run_button.grid(row=4, column=0, pady=10)

    return left_frame, entry1_b, entry2_b

def create_right_frame_b(parent):
    global output_text_b
    right_frame = tk.Frame(parent)

    output_label = tk.Label(right_frame, text="Output:")
    output_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    output_text_b = scrolledtext.ScrolledText(
        right_frame,
        wrap=tk.WORD,
        state=tk.DISABLED,
        width=40,
        height=10
    )
    output_text_b.grid(row=1, column=0, padx=10, pady=10)

    return right_frame, output_text_b
def show_page_b():
    page_b = tk.Toplevel(window)
    page_b.title("Messages from a specific user")
    page_b.geometry("800x400")

    left_frame, entry1_b, entry2_b = create_left_frame_b(page_b)
    left_frame.pack(side=tk.LEFT, padx=10, pady=10)

    right_frame_b, output_text_b = create_right_frame_b(page_b)
    right_frame_b.pack(side=tk.LEFT, padx=10, pady=10)

def run_page_b():
    folder_location = entry1_b.get()
    user_id_to_search = entry2_b.get()

    print(f"Folder Location: {folder_location}")
    print(f"User ID to Search: {user_id_to_search}")

    output_text_b.config(state=tk.NORMAL)

    for folder in os.listdir(folder_location):
        folder_path = os.path.join(folder_location, folder)
        channel_json_path = os.path.join(folder_path, 'channel.json')
        print(f"channel_json_path: {channel_json_path}")
        messages_path = os.path.join(folder_path, 'messages.csv')
        print(f"messages_path: {messages_path}")

        if os.path.exists(channel_json_path) and os.path.exists(messages_path):
            with open(channel_json_path, 'r', encoding='utf-8') as channel_file:
                channel_data = json.load(channel_file)

                if channel_data.get("type", 0) == 1 and user_id_to_search in channel_data.get("recipients", []):
                    output_text_b.insert(tk.END, f"File Path: {messages_path}\n")

                    with open(messages_path, 'r', encoding='utf-8') as messages_file:
                        next(messages_file)  # Skip header line if any
                        for line in messages_file:
                            columns = line.split(',')
                            if len(columns) >= 4:  # Check if there are enough columns
                                message_content = columns[2].strip()
                                attachments = columns[3].strip()
                                
                                if message_content:
                                    output_text_b.insert(tk.END, f"{message_content}\n")
                                
                                if attachments:
                                    output_text_b.insert(tk.END, f"{attachments}\n")
                            elif len(columns) == 3:
                                message_content = columns[2].strip()
                                if message_content:
                                    output_text_b.insert(tk.END, f"{message_content}\n")
                            else:
                                print("Unknown error!")
    output_text_b.config(state=tk.DISABLED)

    print("Running Page B")

    open_file(messages_path)
                                
"""
                    with open(messages_path, 'r', encoding='utf-8') as messages_file:
                        next(messages_file)
                        for line in messages_file:
                            columns = line.split(',')
                            message_content = columns[2].strip()
                            attachments = columns[3].strip()
                            
                            if message_content:
                                output_text_b.insert(tk.END, f"{message_content}\n")
                            
                            if attachments:
                                output_text_b.insert(tk.END, f"{attachments}\n")
"""
                    

    
    

def create_left_frame_c(parent):
    left_frame = tk.Frame(parent)

    label1 = tk.Label(left_frame, text="Unzipped package location:")
    label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    entry1 = tk.Entry(left_frame, width=30)
    entry1.grid(row=1, column=0, padx=10, pady=10)

    run_button = tk.Button(left_frame, text="Run", command=run_page_c)
    run_button.grid(row=2, column=0, pady=10)

    return left_frame, entry1

def create_right_frame_c(parent):
    right_frame = tk.Frame(parent)

    output_label = tk.Label(right_frame, text="Output:")
    output_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    output_text = scrolledtext.ScrolledText(
        right_frame,
        wrap=tk.WORD,
        state=tk.DISABLED,
        width=40,
        height=10
    )
    output_text.grid(row=1, column=0, padx=10, pady=10)

    return right_frame, output_text

def show_page_c():
    page_c = tk.Toplevel(window)
    page_c.title("All links and attachments you've ever sent")
    page_c.geometry("800x400")

    left_frame, entry1_c = create_left_frame_c(page_c)
    left_frame.pack(side=tk.LEFT, padx=10, pady=10)

    right_frame_c, output_text_c = create_right_frame_c(page_c)
    right_frame_c.pack(side=tk.LEFT, padx=10, pady=10)

def run_page_c():
    print("Running Page C")

def show_info_window():
    info_window = tk.Toplevel(window)
    info_window.title("Instructions")
    info_window.geometry("500x250")

    info_text = scrolledtext.ScrolledText(
        info_window,
        wrap=tk.WORD,
        width=120,
        height=52,
    )
    
    info_text.insert(tk.END, "In order to use this program, you first need to request your data from Discord, then wait a few days until you get an email with your data. After you get the email, download the package.zip file and unzip it. Save the unzipped package folder location somewhere for ease of use.")
    info_text.insert(tk.END,"\n\nExample of proper package folder location:\nC:\\Users\\You\\Desktop\\package\\messages")
    info_text.insert(tk.END,"\n\nAll dms function notes:\n\nHow to get your discord ID?\nYou can left click on yourself in the discord app on bottom right when you have developer mode enabled and you should see a 'Copy User ID' button. Click that and the ID will be stored in your clipboard. Alternatively just check for duplicates in dm folderns for the ID you're looking for. You do you.")
    info_text.insert(tk.END,"\n\nMessages from a specific user notes:\n\nHow to get the specific user ID?\nFor that please use the first function or if you can, you can copy that persons ID off of discord with developer mode enabled. Simply right click on the user and you should see a 'Copy User ID' button.")
    info_text.insert(tk.END,"\n\nKnown bugs:\n\nThe program sometimes stuggles with reading certain lines of messages in 'Messages from a specific user' screen due to them being\nwritten\nlike\nthis\nI reccomend fully checking the csv file if you're looking for something specific!")
    info_text.pack(padx=10, pady=10)

def show_info_button():
    show_info_window()

def quit_app():
    window.destroy()

window = tk.Tk()
window.title("Discord data viewer")
window.geometry("600x400")

info_button = tk.Button(window, text="Info", command=show_info_button)
info_button.pack(side=tk.TOP, pady=10)

button_a = tk.Button(window, text="Total DMs", command=show_page_a)
button_b = tk.Button(window, text="Messages from someone special <3", command=show_page_b)
button_c = tk.Button(window, text="All links and attachments", command=show_page_c)

button_a.pack(side=tk.LEFT, padx=10, pady=10,)
button_b.pack(side=tk.LEFT, padx=10, pady=10,)
button_c.pack(side=tk.LEFT, padx=10, pady=10,)

quit_button = tk.Button(window, text="Quit", command=quit_app)
quit_button.pack(side=tk.BOTTOM, pady=10)

window.mainloop()