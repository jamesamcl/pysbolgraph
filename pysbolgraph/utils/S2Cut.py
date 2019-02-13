from S2Location import S2Location

from meta.terms import SBOL2


class S2Cut(S2Location):
    def __init__(self, g, uri):
        super(S2Cut, self).__init__(g, uri)

    @property
    def at(self):
        return self.get_integer_property(SBOL2.at)
