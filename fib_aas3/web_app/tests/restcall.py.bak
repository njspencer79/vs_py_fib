import json
import urllib2

# This is a simple rest client that will convert the strings to a list
# and the individual elements to a long

# It does print the errors the screen if they occur.  This for the unit testing only.

def get_url(urlstr):
    response = None
    try:
        response = urllib2.urlopen( urlstr)
        html_out = response.read()
    except Exception as e:
        print(e)
        if "HTTP Error" in str(e):
            return False

    try:
        list_fibs = json.loads(html_out)
    except Exception as e:
        print(e)
        return False

    try:
        long_fibs = []
        for item in list_fibs:
            long_fibs.append(long(item))
    except Exception as e:
        print(e)
        return False

    return long_fibs
