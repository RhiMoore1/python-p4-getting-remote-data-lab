import requests
import json
# Start by creating a GetRequester class. This class should be able to initialize with a string URL.
class GetRequester:

    def __init__(self, url):
        self.url = url
# The GetRequester class should have a get_response_body method that 
# sends a GET request to the URL passed in on initialization. 
# This method should return the body of the response.
# module get_response_body function returns response.
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

# programs = GetRequester.get_response_body()    
# The GetRequester class should have a load_json method that should use get_response_body to send a request, 
# then return a Python list or dictionary made up of data converted from the response of that request.
# module load_json function returns response
    def load_json(self):
        response = json.loads(self.get_response_body())
        return response
