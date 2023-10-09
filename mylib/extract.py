import requests

def extract(
    url="https://github.com/nogibjj/IDS706_Mini_PJT6/raw/main/youtubers.csv", 
    file_path="youtubers.csv"
):
    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path