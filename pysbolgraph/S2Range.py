from S2Location import S2Location

from terms import SBOL2


class S2Range(S2Location):
    def __init__(self, g, uri):
        super(S2Range, self).__init__(g, uri)

    @property
    def start(self):
        return self.getIntegerProperty(SBOL2.start)

    @property
    def end(self):
        return self.getIntegerProperty(SBOL2.end)

    @property
    def orientation(self):
        return self.getUriProperty(SBOL2.orientation)
