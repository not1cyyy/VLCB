from tkinter import *
import random
import smtplib
from dotenv import load_dotenv
import os
import requests
import json
import csv
from datetime import datetime


load_dotenv()

# Define the main window
root = Tk()
root.geometry("400x400")
root.title("Virtual Love Coupon Book")

# Define the coupon types
coupons = {
    "Romantic Dinner": "RD",
    "Infinite Kisses": "IK",
    "Weekend Getaway": "WG",
    "Picnic Date": "PD",
}

# Define the function for generating a coupon code
def generate_coupon():
    # Choose a random coupon type
    coupon_type = random.choice(list(coupons.values()))

    # Generate a random code
    coupon_code = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6))

    # Combine the coupon type and code
    return coupon_type + coupon_code

# Define the function for sending a coupon code to an email address
def send_coupon_email(name, email, coupon):
    # Define the API endpoint
    url = "https://api.sendinblue.com/v3/smtp/email"

    # Set the API key and headers
    api_key = os.getenv("SENDINBLUE_API_KEY")
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    # Define the email message
    message = {
        "sender": {
            "name": "Virtual Love Coupon Book",
            "email": os.getenv("SENDER_EMAIL")
        },
        "to": [
            {
                "email": email
            }
        ],
        "subject": "Your Virtual Love Coupon Book Coupon Code",
        "htmlContent": f"<p>Dear {name},</p><p>Your coupon code for {list(coupons.keys())[list(coupons.values()).index(coupon[:2])]} is: {coupon}</p> <p>You can redeem it by sending it to your lover!</p> <p>Enjoy!</p>"
    }

    # Send the email using the Sendinblue API
    response = requests.post(url, headers=headers, data=json.dumps(message))

    # Check if the email was sent successfully
    if response.status_code == 201:
        print("Email sent successfully!")
        print(f"Coupon code {coupon} sent to : {email} ")

        # Log the email, coupon code, and time to the file
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open('logs.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, coupon, timestamp])
    else:
        print(f"Error sending email: {response.content}")

# Define the function for sending a coupon
def send_coupon():
    # Get the input values from the form
    name = name_entry.get()
    email = email_entry.get()
    coupon = coupon_entry.get()

    # Send the coupon code to the email address
    send_coupon_email(name, email, coupon)

    # Clear the form fields
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    coupon_entry.delete(0, END)

## Define the form fields
name_label = Label(root, text="Name:", font=("Open Sans", 12))
name_entry = Entry(root, width=30, font=("Open Sans", 12))

email_label = Label(root, text="Email:", font=("Open Sans", 12))
email_entry = Entry(root, width=30, font=("Open Sans", 12))

coupon_label = Label(root, text="Coupon:", font=("Open Sans", 12))
coupon_entry = Entry(root, width=30, font=("Open Sans", 12))

# Define the generate coupon button
generate_button = Button(root, text="Generate Coupon", font=("Open Sans", 12), bg="#4CAF50", fg="white", command=lambda: coupon_entry.insert(0, generate_coupon()))

# Define the redeem coupon button
redeem_button = Button(root, text="Send Coupon", font=("Open Sans", 12), bg="#f44336", fg="white", command=send_coupon)

# Add some padding and spacing
name_label.pack(pady=5)
name_entry.pack(pady=5)

email_label.pack(pady=5)
email_entry.pack(pady=5)

coupon_label.pack(pady=5)
coupon_entry.pack(pady=5)

generate_button.pack(pady=10)
redeem_button.pack(pady=10)


# Start the main event loop
root.mainloop()
