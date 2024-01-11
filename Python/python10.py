import requests

def print_request_details(method, url):
    print("\nRequest to be sent:")
    print(f"HTTP Method: {method}")
    print(f"Destination URL: {url}")

def translate_status_code(status_code):
    status_codes = {
        200: "OK",
        201: "Created",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        500: "Internal Server Error",
    }
    return status_codes.get(status_code, f"Unknown Status Code: {status_code}")

def print_response_headers(response):
    print("\nResponse Header Information:")
    print(f"Status Code: {response.status_code} - {translate_status_code(response.status_code)}")
    print("Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

# Prompt the user to select an HTTP Method
http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
selected_method = input(f"Choose an HTTP Method ({', '.join(http_methods)}): ").upper()

# Validate the selected method
if selected_method not in http_methods:
    print("Invalid HTTP Method selected. Exiting script.")
    exit()

# Prompt the user to enter a destination URL
destination_url = input("Please enter the destination URL: ")

# Print the entire request to be sent and ask for confirmation
print_request_details(selected_method, destination_url)
confirmation = input("Confirm sending the request? (yes/no): ")

if confirmation.lower() == "yes":
    # Performing the request using requests library
    if selected_method == "GET":
        response = requests.get(destination_url)
    # Add additional conditions for other HTTP methods if needed

    # Printing response header information
    print_response_headers(response)
else:
    print("Request canceled by user.")
