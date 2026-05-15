import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "http://www.omdbapi.com/"

def search_movie(title):
    url = f"{BASE_URL}?s={title}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Search"):
        return data["Search"]
    return []

def get_movie_details(imdb_id):
    url = f"{BASE_URL}?i={imdb_id}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        return data
    return None