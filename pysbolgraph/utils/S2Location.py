from S2Identified import S2Identified

from meta.terms import SBOL2

class S2Location(S2Identified):
    def __init__(self, g, uri):
        super(S2Location, self).__init__(g, uri)


class S2GenericLocation(S2Location):
    def __init__(self, g, uri):
        super(S2GenericLocation, self).__init__(g, uri)

    @property
    def orientation(self):
        return self.get_uri_property(SBOL2.orientation)