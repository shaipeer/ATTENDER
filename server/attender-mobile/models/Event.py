__author__ = 'olesya'

from google.appengine.ext import ndb


class Event(ndb.Model):
    name = ndb.StringProperty()
    date = ndb.DateProperty(auto_now_add=True)
    time = ndb.TimeProperty()
    address = ndb.StringProperty()
    description = ndb.TextProperty()
    owner = ndb.StringProperty()

