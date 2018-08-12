import requests

session = requests.Session()

base_url = 'https://www.delijn.be/{}/'

rise_api = {
    'core': 'rise-api-core'
    }


class deLijn:

    def __init__(self):

    def do_request(self, api, params=None):
        if api in rise_api:
            url = base_url.format(rise_api[api])
            if params:
                extra_url = '/'.join(params)
                url += extra_url
            try:
                response = session.get(url)
                try:
                    json_data = response.json()
                    return json_data
                except ValueError:
                    return -1
            except requests.exceptions.RequestException as e:
                print(e)
                try:
                    session.get('https://1.1.1.1/', timeout=1)
                except requests.exceptions.ConnectionError:
                    print("Your internet connection doesn't seem to be working.")
                    return -1
                else:
                    print("The undocumented API doesn't seem to be working anymore.")
                    return -1

    def convert_location(self, lat=None, long=None):
        if lat and long:
            params = ['locations', 'convert', lat, long]
            json_data = self.do_request('core', params)
            return json_data

# They seem to use x/y coordinates for all their geo-based information
# so they have an API route that converts proper lat/long coordinates into their equivalent x/y coordinates.
# Use the following route to convert lat/long to x/y where {{lat}} is your latitude and {{long}} is your longitude.

# Which will give you the x/y coordinate in a response similar to:

# {
  # "halteNummer": null,
  # "idString": null,
  # "laatstgebruikt": null,
  # "locationId": null,
  # "markedString": null,
  # "xCoordinaat": 103853,
  # "yCoordinaat": 191981
# }

# In my opinion, they should just stick to using the familiar lat/long coordinates on the frontend and silently convert them to their x/y equivalents on the backend. That way the client doesn't have to do an additional API request for the conversion and we can all work with data that we are most familiar with.

# EDIT: A reader has notified me that these are most likely Belgian Lambert 72 coordinates.
