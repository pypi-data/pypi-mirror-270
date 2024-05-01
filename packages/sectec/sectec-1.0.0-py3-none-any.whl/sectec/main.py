import requests
from bs4 import BeautifulSoup

def getTitle(url):
    """
    Fetches the title of the webpage specified by the URL.
    
    Args:
    - url (str): The URL of the webpage.
    
    Returns:
    - str: The title of the webpage.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        return title
    else:
        print("Failed to fetch title. Status code:", response.status_code)
        return None

def getHTML(url):
    """
    Fetches the entire HTML content of the webpage specified by the URL.
    
    Args:
    - url (str): The URL of the webpage.
    
    Returns:
    - str: The HTML content of the webpage.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch HTML content. Status code:", response.status_code)
        return None

def getText(url):
    """
    Extracts all the text from the webpage specified by the URL.
    
    Args:
    - url (str): The URL of the webpage.
    
    Returns:
    - str: All the text content of the webpage.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text
    else:
        print("Failed to fetch text content. Status code:", response.status_code)
        return None
