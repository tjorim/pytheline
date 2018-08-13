import requests

session = requests.Session()

base_url = 'https://www.delijn.be/{}/'

rise_api = {
    'core': 'rise-api-core'
}


class deLijn:

    def __init__(self):
        pass

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
        """
        The rise-API uses x/y coordinates for all geo-based information, Belgian Lambert 72 coordinates.
        This function converts proper latitude/longitude coordinates into their equivalent x/y coordinates.

        ...

        Parameters
        ----------
        lat : float
            latitude coordinate
        long : float
            longitude coordinate

        Returns
        -------
        json which contains the following values
            xCoordinaat : int
                X coordinate
            yCoordinaat : int
                Y coordinate

        {
          "halteNummer": null,
          "idString": null,
          "laatstgebruikt": null,
          "locationId": null,
          "markedString": null,
          "xCoordinaat": 103853,
          "yCoordinaat": 191981
        }

        """
        if lat and long:
            params = ['locations', 'convert', lat, long]
            json_data = self.do_request('core', params)
            return json_data

    def haltes_doorkomendelijnen(self, halte_id=None):
        """

        ...

        Parameters
        ----------
        halte_id : int
            Halte ID

        Returns
        -------
        """
        if halte_id:
            params = ['haltes', 'doorkomendelijnen', halte_id]
            json_data = self.do_request('core', params)
            return json_data

    def haltes_indebuurt(self, xCoordinaat=None, yCoordinaat=None, radius=None):
        """

        ...

        Parameters
        ----------
        xCoordinaat : int
            X coordinate
        yCoordinaat : int
            Y coordinate
        radius : int
            Zoek radius, eenheid onbekend

        Returns
        -------
        """
        if halte_id:
            params = ['haltes', 'indebuurt', xCoordinaat, yCoordinaat, radius]
            json_data = self.do_request('core', params)
            return json_data

    def haltes_titel(self, halte_id=None):
        """

        ...

        Parameters
        ----------
        halte_id : int
            Halte ID

        Returns
        -------
        """
        if halte_id:
            params = ['haltes', 'titel', halte_id]
            json_data = self.do_request('core', params)
            return json_data

    def haltes_vertrekken(self, halte_id=None, num_results=8):
        """

        ...

        Parameters
        ----------
        halte_id : int
            Halte ID
        num_results : int, optional
            Maximum aantal resultaten

        Returns
        -------
        """
        if halte_id:
            params = ['haltes', 'vertrekken', halte_id, num_results]
            json_data = self.do_request('core', params)
            return json_data
