from .S2Identified import S2Identified


class S2Location(S2Identified):
    def __init__(self, g, uri):
        super(S2Location, self).__init__(g, uri)
