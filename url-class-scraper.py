import requests
from bs4 import BeautifulSoup

def get_elements_by_css_class(url, css_class):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all elements with the specified CSS class
            elements = soup.find_all(class_=css_class)

            # Extract the text content of the elements and store them in an array
            result_array = [element.get_text() for element in elements]

            return result_array
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
url = 'https://example.com'  # Replace with the URL you want to scrape
css_class = 'example-class'  # Replace with the CSS class you want to extract
result = get_elements_by_css_class(url, css_class)

if result:
    for item in result:
        print(item)
