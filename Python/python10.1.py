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

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# For the given URL, print response header information to the screen.

#victor's Code'

from urllib import response
import requests
a = input("Copy and Paste a URL you wish to get information on: ")
b = input("Get, Post, Put, Delete , Head, Patch, Options: ")
c = input("Enter Y to confirm or N to Deny: ")
Get = requests.get(f"{a}")
Post = requests.post(f"{a}")
Put = requests.put(f"{a}")
Delete = requests.delete(f"{a}")
Head = requests.head(f"{a}")
Patch = requests.patch(f"{a}")
Options = requests.options(f"{a}")
if Get.status_code == 200:
    print("We Have Made Contact")
elif Get.status_code == 404:
    print("Johnson, call Houston because we might have a problem.")
else:
    print("Please include https:// in your URL")

# Even though I use the other commands it just gives a 405 and it still gives the contact response with the 200 if that makes sense
    
#Anthony's Code
 from urllib import response
import requests
a = input("Copy and Paste a URL you wish to get information on: ")
b = input("Get, Post, Put, Delete , Head, Patch, Options: ")
If b == "Post":
    response = requests.get(https://github.com/)