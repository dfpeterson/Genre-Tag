from html import parser
from http import client
import urllib

urllib.request.urlopen('http://rateyourmusic.com/release/album/kingcrow/something_unknown/', data, timeout)

rym = parser.HTMLParser()
album = client.HTTPConnection('rateyourmusic.com/release/album/kingcrow/something_unknown/')
rym.feed(album)