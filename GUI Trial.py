import tkinter as tk
import csv
from random import randrange

# Function to check empty rooms
def check_empty_rooms():
    with open('database.csv', 'r') as f:
        reader = csv.reader(f)
        empty_rooms = []
        for row in reader:
            if row[-1] == '0':
                empty_rooms.append(row[0])
        if empty_rooms:
            message = "Empty rooms:\n" + "\n".join(empty_rooms)
        else:
            message = "No empty rooms found."
        show_message(message, "Empty Rooms")

# Function to search for guest
def search_guest():
    room_number = input_room_number.get()
    found = False
    with open('database.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == room_number:
                found = True
                message = f"Cost: AED {row[1]}\nMembers: {row[2]}\nCheck-in Date: {row[3]}\nCheck-out Date: {row[4]}\nDuration: {row[5]} day(s)"
                break
    if not found:
        message = "Guest not found for room number " + room_number
    show_message(message, "Guest Information")

# Function to display database
def display_database():
    headers = ["Room No.", "Cost", "Members", "Check-in Date", "Check-out Date", "Duration"]
    data = []
    with open('database.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    show_table(headers, data, "Database")

# Function to explore room options
def explore_rooms():
    options = [
        ("Standard", "AED 550 per night", "Downtown view", "1 room with window", "Gym, Pool"),
        ("Deluxe", "AED 750 per night", "Sea view", "2 rooms with balcony", "Gym, Pool, Breakfast"),
        ("Luxury Suite", "AED 1450 per night", "Sea view", "3 rooms with balcony", "Gym, Pool, Breakfast, Beach access")
    ]
    headers = ["Type", "Cost", "View", "Layout", "Perks"]
    show_table(headers, options, "Room Options")

# Function to book a room
def book_room():
    name = input_name.get()
    room_type = input_room_type.get()
    duration = input_duration.get()
    if not name or not room_type or not duration:
        show_message("Please fill in all fields.", "Error")
        return
    try:
        duration = int(duration)
    except ValueError:
        show_message("Duration must be a number.", "Error")
        return
    # Calculate cost based on room type
    cost = 550 if room_type.lower() == "standard" else 750 if room_type.lower() == "deluxe" else 1450
    total_cost = cost * duration
    token_number = randrange(1111, 10000)
    message = f"Your Final amount is AED {total_cost}\nToken number: {token_number}"
    show_message(message, "Booking Confirmation")

# Function to complete payment
def complete_payment():
    token_number = input_token_number.get()
    payment_mode = input_payment_mode.get()
    if not token_number or not payment_mode:
        show_message("Please enter token number and payment mode.", "Error")
        return
    # Verify token number and process payment
    # Implement your payment processing logic here
    message = "Payment successful." if payment_mode.lower() == "card" else "Please pay by cash at reception."
    show_message(message, "Payment Status")

# Function to show message in a new window
def show_message(message, title):
    message_window = tk.Toplevel()
    message_window.title(title)
    message_label = tk.Label(message_window, text=message)
    message_label.pack(padx=20, pady=20)
    ok_button = tk.Button(message_window, text="OK", command=message_window.destroy)
    ok_button.pack(pady=10)

# Function to show table in a new window
def show_table(headers, data, title):
    table_window = tk.Toplevel()
    table_window.title(title)
    table = tk.Treeview(table_window)
    table["columns"] = headers
    for header in headers:
        table.heading(header, text=header)
    for row in data:
        table.insert("", "end", values=row)
    table.pack(fill="both", expand=True)

# Main window
window = tk.Tk()
window.title("Hotel Management System")

# Manager interface
manager_frame = tk.Frame(window)
check_empty_rooms_button = tk.Button(manager_frame, text="Check Empty Rooms", command=check_empty_rooms)
check_empty_rooms_button.pack(side="left", padx=10)
search_guest_button = tk.Button(manager_frame, text="Search for Guest", command=search_guest)
search_guest_button.pack(side="left", padx=10)
display_database_button = tk.Button(manager_frame, text="Access Database", command=display_database)
display_database_button.pack(side="left", padx=10)
manager_frame.pack(pady=10)

# Guest interface
guest_frame = tk.Frame(window)
explore_rooms_button = tk.Button(guest_frame, text="Explore Room Options", command=explore_rooms)
explore_rooms_button.pack(side="left", padx=10)
book_room_button = tk.Button(guest_frame, text="Book a Room", command=book_room)
book_room_button.pack(side="left", padx=10)
complete_payment_button = tk.Button(guest_frame, text="Complete Payment", command=complete_payment)
complete_payment_button.pack(side="left", padx=10)
guest_frame.pack(pady=10)

# Input fields for booking and payment
input_name = tk.Entry(window)
input_room_type = tk.Entry(window)
input_duration = tk.Entry(window)
input_token_number = tk.Entry(window)
input_payment_mode = tk.Entry(window)

# Place input fields and labels as needed

window.mainloop()
