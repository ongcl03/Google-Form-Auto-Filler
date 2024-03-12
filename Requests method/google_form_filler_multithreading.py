import requests
import json
import time
import threading


# THREADING:

# A daemon thread in Python is a thread that runs in the background and does not block the main program from exiting. When the main program exits, all daemon threads are killed automatically. This behavior makes daemon threads useful for tasks that run in the background without needing explicit management by the program to shut them down.

# The key characteristics of daemon threads are:

# Background Execution: Daemon threads run in the background, performing tasks without interfering with the main execution flow of the program.
# Automatic Termination: They are automatically terminated by the Python runtime when the main program exits, even if they are still running or in the middle of an operation.
# Non-critical Tasks: Due to their nature of being abruptly terminated, daemon threads are generally used for non-critical background tasks that can be safely killed at any time.


# Using threading can submit the forms concurrently (faster) (because using 1 thread for each post submit requests) 


start_time = time.time()
number_of_forms = 50


def fill(url, form_data):
    print(requests.post(url, data = form_data))                     # send data


url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScVQYmVsplrGh7rdFXxCuKp5cZwCTLB2rOhHYni240a3g4BWg/formResponse"

form_data = {
    "entry.1074015215": "Option 1",
    "entry.505645925": "acaca",
    "entry.841756088": "acac",
    "pageHistory": "0",
    }

def do_request():
    fill(url, form_data)


# Create threads array 
threads = []

# Create n numbers of threads based on the number of forms (50 forms will have 50 threads)
for i in range(number_of_forms):
    t = threading.Thread(target=do_request, daemon=True)
    threads.append(t)

# Start the thread (each form will be submitted concurrently)
for i in range(number_of_forms):
    threads[i].start()


# Wait for all the created threads to completed their works before the main program proceeds
for i in range(number_of_forms):
    threads[i].join()


end_time = time.time()
total_time = end_time- start_time
total_time = round(total_time, 2)


print(f"Used {total_time} seconds to fill {number_of_forms} forms")



