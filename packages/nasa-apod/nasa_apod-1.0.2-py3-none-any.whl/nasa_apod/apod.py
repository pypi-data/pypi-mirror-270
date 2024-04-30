import requests

class APODService:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/planetary/apod"
    
    def get_picture(self, date=None):
        params = {'api_key': self.api_key}
        if date:
            params['date'] = date

        response = requests.get(self.base_url, params=params)
        return response.json()