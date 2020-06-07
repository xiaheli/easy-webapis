#Please first read the README.md
import urllib.request
def pagedown(url):
    response = urllib.request.urlopen(url)
    result = response.read()
    return result