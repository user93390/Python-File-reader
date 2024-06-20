import os

File = input("What file do you wish to read? ")
FileType = input("what file type? (e.g txt) ")
Location = input("enter the file path ")

# Combine the location and file name using os.path.join()
file_path = os.path.join(Location, File + "." + FileType)
import pyautogui
import time

# Check if the file exists
if os.path.isfile(file_path):
    Reader = open(file_path, "r", encoding="utf-8")
    print("Reading '" + File + "'")
    Continue = input("do you want to continue? ")
    if Continue.__contains__("no"):
        exit()

    if Continue.__contains__("yes"):
        Print = Reader.read()
        print("'" + Print + "'")
        Reader.close()
    def LoggerEnabled(Boolean):
        Data = "Target file " + File + ", File type " + FileType + ", location " + Location + " ."
        Log = open("Log.txt", "w", encoding="utf-8")
        LoggerEnabled(True)
else:
    print("File not found")
    input()
