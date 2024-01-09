# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.
destination_url = input("Please enter the destination URL: ")
# Prompt the user to select a HTTP Method of the following options:
print("Select an HTTP Method:")
print("1. GET\n2. POST\n3. PUT\n4. DELETE\n5. HEAD\n6. PATCH\n7. OPTIONS")
http_method_options = input("Input method selection:")
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# Using the requests library, perform a GET request against your lab web server.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# For the given URL, print response header information to the screen.



# Prompt the user to type a string input as the variable for your destination URL.
#destination_url = input('Please Enter Your Destination URL:"')

# Prompt the user to select a HTTP Method of the following options:
#from urllib import response
#import requests
#b = input("Get, Post, Put, Delete , Head, Patch, Options:")

# import requests

# Prompt the user to input a destination URL


# # Prompt the user to select an HTTP Method
# print("Select an HTTP Method:")
# print("1. GET\n2. POST\n3. PUT\n4. DELETE\n5. HEAD\n6. PATCH\n7. OPTIONS")
# http_method_options = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
# selected_option = int(input("Enter the number for the desired HTTP Method: "))
# selected_http_method = http_method_options[selected_option - 1]

# # Print the entire request to be sent and ask for confirmation
# print("\nRequest to be sent:")
# print(f"HTTP Method: {selected_http_method}")
# print(f"Destination URL: {destination_url}")
# confirmation = input("Confirm sending the request? (yes/no): ")

# if confirmation.lower() == "yes":
#     # Performing the request using requests library
#     response = requests.request(selected_http_method, destination_url)

#     # Translate status codes to plain terms
#     status_codes = {
#         200: "OK",
#         404: "Not Found",
#         # Add more status codes translation as needed
#     }

#     # Printing response header information
#     print("\nResponse Header Information:")
#     if response.status_code in status_codes:
#         print(f"Status Code: {response.status_code} - {status_codes[response.status_code]}")
#     else:
#         print(f"Status Code: {response.status_code}")
#     print("Headers:")
#     for header, value in response.headers.items():
#         print(f"{header}: {value}")
# else:
#     print("Request canceled by user.")

