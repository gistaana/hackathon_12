import requests

from secret import API_KEY

#location of all the assignments
url = "https://courses.ianapplebaum.com/syllabus/4"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers).json()

print(response)
