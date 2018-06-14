Clickatell Python Library
================================

This library supports version **2** of Python.

------------------------------------

This library allows easy access to connecting the [Clickatell's](http://www.clickatell.com) different messenging API's.

Installation
------------------

You can install this library via PIP as part of your requirements file.

```
pip install clickatell-platform
```

[Clickatell Python PyPI](https://pypi.python.org/pypi?name=clickatell&version=0.0.1&:action=display)

Usage
------------------

The library currently supports the `Http` and `Rest` protocols.

### HTTP API

``` python
from clickatell.http import Http

clickatell = Http(apiKey)
response = clickatell.sendMessage(['1111111111'], "My Message rest")

print(response) #Returns the headers with all the messages

for entry in response['messages']:
    print(entry) #Returns all the message details per message
    #print(entry['apiMessageId'])
    #print(entry['to'])
    #print(entry['accepted'])
    #print(entry['error'])
```

### REST API

``` python
from clickatell.rest import Rest

clickatell = Rest(apiKey)
response = clickatell.sendMessage(['1111111111'], "My Message rest")

print response #Returns the headers with all the messages

for entry in response['messages']:
    print(entry) #Returns all the message details per message
    #print(entry['apiMessageId'])
    #print(entry['to'])
    #print(entry['accepted'])
    #print(entry['error'])
```

### Sending to multiple numbers

The `sendMessage` call `to` parameter can take an array of numbers. If you specify only a single number like `clickatell.sendMessage(1111111111, "Message")` the library will automatically convert it to an array for your convenience.

To send to multiple numbers, just pass a list of numbers like `clickatell.sendMessage([1111111111,2222222222], "Message")`

Supported API calls
------------------

The available calls are defined in the `clickatell.Transport` interface.

``` python

def sendMessage(self, to, message, extra={})

```

Dealing with extra parameters in sendMessage
--------------------------------------

For usability purposes the `sendMessage` call focuses on the recipients and the content. In order to specify and of the additional parameters defined
in the [Clickatell document](http://www.clickatell.com), you can use the `extra` parameter and pass them as a dictionary.

Receiving and consuming the status callback
--------------------------------------

The following will be returned from the callback in two different sets:

DELIVERED_TO_GATEWAY :
* integrationName
* messageId
* requestId
* clientMessageId
* to
* from
* statusCode
* status
* statusDescription
* timestamp

RECEIVED_BY_RECIPIENT :
* integrationName
* messageId
* requestId
* clientMessageId
* to
* from
* statusCode
* status
* statusDescription
* timestamp

There is a python test server included in the clickatell folder.
To run this server, you require the endpoints pip package:
```
pip install endpoints
```

You can run the server using the following command:
```
 endpoints --dir=clickatell/ --prefix=controller --host=<hostname>:<port>
```

This server currently prints out to the server console. Replace the print function with your function name to consume the data.
All data is returned in JSON.
