# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET - Purpose: Retrieve data from the server.| Use Case: Used when a client wants to request information from a specified resource. It should have no other effect than retrieving data.
# POST - Purpose: Submit data to be processed to a specified resource. | Use Case: Used when a client wants to send data to the server for processing, often to create a new resource.
# PUT - Purpose: Update a resource or create a new resource if it does not exist. | Use Case: Used when a client wants to update an existing resource or create a new resource at the specified URI.
# DELETE - Purpose: Request that a resource be removed. | Use Case: Used when a client wants to delete a specified resource on the server.
# HEAD - Purpose: Retrieve the headers for a specified resource without the body. | Use Case: Similar to GET, but the server should not send the message body in the response.
# PATCH - Purpose: Apply partial modifications to a resource. | Use Case: Used when a client wants to apply partial modifications to a resource on the server. It is often used for updating resources with incremental changes.
# OPTIONS - Purpose: Describe the communication options for the target resource. | Use Case: Used when a client wants to retrieve information about the communication options for the target resource. This can include supported methods or server capabilities.
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# Using the requests library, perform a GET request against your lab web server.

# # For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# # For the given URL, print response header information to the screen.

# #victor's Code'

# from urllib import response
# import requests
# a = input("Copy and Paste a URL you wish to get information on: ")
# b = input("Get, Post, Put, Delete , Head, Patch, Options: ")
# c = input("Enter Y to confirm or N to Deny: ")
# Get = requests.get(f"{a}")
# Post = requests.post(f"{a}")
# Put = requests.put(f"{a}")
# Delete = requests.delete(f"{a}")
# Head = requests.head(f"{a}")
# Patch = requests.patch(f"{a}")
# Options = requests.options(f"{a}")
# if Get.status_code == 200:
#     print("We Have Made Contact")
# elif Get.status_code == 404:
#     print("Johnson, call Houston because we might have a problem.")
# else:
#     print("Please include https:// in your URL")

# Even though I use the other commands it just gives a 405 and it still gives the contact response with the 200 if that makes sense
    
import requests

b = input("Choose an HTTP Method (Get, Post, Put, Delete, Head, Patch, Options): ").capitalize()

if b == "Get":
    response = requests.get("https://www.google.com/")
elif b == "Post":
    response = requests.post("https://www.google.com/")
elif b == "Put":
    response = requests.put("https://www.google.com/")
elif b == "Delete":
    response = requests.delete("https://www.google.com/")
elif b == "Head":
    response = requests.head("https://www.google.com/")
elif b == "Patch":
    response = requests.patch("https://www.google.com/")
elif b == "Options":
    response = requests.options("https://www.google.com/")
else:
    print("Invalid input. Exiting script.")
    quit()

answer = input("Enter yes or no: ")

if answer.lower() == "yes":
    # Print response header information
    print("\nResponse Header Information:")
    print(f"Status Code: {response.status_code}")
    print("Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
else:
    print("Cancelling")

# Print additional messages based on the HTTP method
if response.status_code == 404:
    print("Site not found")
elif response.status_code == 200:
    print("Request has succeeded")
elif response.status_code == 403:
    print("This request is forbidden")
else:
    print("Bad Request")



# #Cory's Code
#  # For the given URL, print response header information to the screen.
from urllib import response
import requests
b = input("Get, Post, Put, Delete , Head, Patch, Options:") 


# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS

# Add some comments of what these request are doing to your script

# import requests

# # Prompt the user to select an HTTP Method
# http_method = input("Choose an HTTP Method (Get, Post, Put, Delete, Head, Patch, Options): ").capitalize()

# # Prompt the user to enter a destination URL
# url = "https://github.com/CoreyGray45/SaavyCoders"

# # Print the entire request to be sent and ask for confirmation
# print(f"Request to be sent: {http_method} {url}")
# confirmation = input("Please confirm to proceed. (y/n): ")

# if confirmation.lower() == "y":
#     # Using the requests library, perform a request to your GitHub URL
#     response = requests.request(http_method, url)

#     # Translate the status code into plain terms
#     status_codes = {
#         200: "OK",
#         201: "Created",
#         204: "No Content",
#         400: "Bad Request",
#         401: "Unauthorized",
#         403: "Forbidden",
#         404: "Not Found",
#         500: "Internal Server Error",
#     }

#     status = status_codes.get(response.status_code, "Unknown")
#     print(f"Status: {status}")

# else:
#     print("Input Error.")
