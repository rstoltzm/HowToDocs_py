# Code is from Udemy: "The Python Mega Course: Build 10 Real World Applications" by Ardit Sulce

correct_password = "python123"

password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password! Enter again: ")

print("Logged in")
