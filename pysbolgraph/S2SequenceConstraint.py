
from S2Identified import S2Identified

from terms import SBOL2

class S2SequenceConstraint(S2Identified):
    def __init__(self, g, uri):
        super(S2SequenceConstraint, self).__init__(g, uri)
    @property
    def restriction(self):
        return self.getUriProperty(SBOL2.restriction)
    @restriction.setter
    def restriction(self, restriction):
        self.setUriProperty(SBOL2.restriction, restriction)

