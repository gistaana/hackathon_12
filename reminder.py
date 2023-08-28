import requests
#location of all the assignments
url = "https://courses.ianapplebaum.com/syllabus/4"

headers = {
    "Authorization": "Bearer {Sl9TiE5yh4JAKIJVKl7V7FpafWf03AmoSrcT2SeW}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers).json()

print(response)
