import os
import requests

# Path to the desktop folder Extraction_Clark
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Extraction_Clark")
os.makedirs(desktop_path, exist_ok=True)

# URL of the Clark University faculty directory
url = "https://www.clarku.edu/faculty/"

# Fetching the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Saving the content to a file
    html_file_path = os.path.join(desktop_path, "clark_faculty_directory.html")
    with open(html_file_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"HTML content saved to: {html_file_path}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
