from django import template
import urllib,base64,base64
from io import StringIO

register = template.Library()

@register.filter(name='get64')
def get64(url):
    """
    Method returning base64 image data instead of URL
    """
    print('*****Outside if')
    print('Url value is:'+str(url))
    if url.startswith("http"):
        print('*****Is getting called')
        image = StringIO.StringIO(urllib.urlopen(url).read())
        return 'data:image/jpg;base64,' + base64.b64encode(image.read())

    return url
