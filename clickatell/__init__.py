import httplib2
import urllib
import json
import re
from .exception import ClickatellError

class Transport:
    """
    Abstract representation of a transport class. Defines
    the supported API methods
    """

    endpoint = "platform.clickatell.com"

    def __init__(self):
        """
        Construct a new transportation instance.

        :param boolean secure: Should we try and use a secure connection
        """
        pass

    def merge(self, *args):
        """
        Merge multiple dictionary objects into one.

        :param variadic args: Multiple dictionary items

        :return dict
        """
        values = []

        for entry in args:
            values = values + list(entry.items())

        return dict(values)

    def parseLegacy(self, response):
        """
        Parse a legacy response and try and catch any errors. If we have multiple
        responses we wont catch any exceptions, we will return the errors
        row by row

        :param dict response: The response string returned from request()

        :return Returns a dictionary or a list (list for multiple responses)
        """
        lines = response['body'].strip('\n').split('\n')
        result = []

        for line in lines:
            matches = re.findall('([A-Za-z]+):((.(?![A-Za-z]+:))*)', line)
            row = {}

            for match in matches:
                row[match[0]] = match[1].strip()

            try:
                error = row['ERR'].split(',')
            except KeyError:
                pass
            else:
                row['code'] = error[0] if len(error) == 2 else 0
                row['error'] = error[1].strip() if len(error) == 2 else error[0]
                del row['ERR']

                # If this response is a single row response, then we will throw
                # an exception to alert the user of any failures.
                if (len(lines) == 1):
                    raise ClickatellError(row['error'], row['code'])
            finally:
                result.append(row)

        return result if len(result) > 1 else result[0]

    def parseRest(self, response):
        """
        Parse a REST response. If the response contains an error field, we will
        raise it as an exception.
        """

        body = json.loads(response['body'])

        if not body['error']:
            return body['messages']       
        else:
            raise ClickatellError(body['error'], 400);

    def request(self, action, data={}, headers={}, method='GET'):
        """
        Run the HTTP request against the Clickatell API

        :param str  action:     The API action
        :param dict data:       The request parameters
        :param dict headers:    The request headers (if any)
        :param str  method:     The HTTP method

        :return: The request response
        """
        http = httplib2.Http()
        body = urllib.urlencode(data)
        url = 'https://' + self.endpoint + '/' + action
        url = (url + '?' + body) if (method == 'GET') else url

        resp, content = http.request(url, method, headers=headers, body=json.dumps(data))
        return self.merge(resp, {'body': content})

    def sendMessage(self, to, message, extra={}):
        """
        Send a message.

        :param list     to:         The number you want to send to (list of strings, or one string)
        :param string   message:    The message you want to send
        :param dict     extra:      Any extra parameters (see Clickatell documentation)

        :return dict
        :raises NotImplementedError
        """
        raise NotImplementedError()