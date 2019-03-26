
from .S2Identified import S2Identified

from .terms import SBOL2

class S2Location(S2Identified):
    def __init__(self, g, uri):
        super(S2Location, self).__init__(g, uri)

    @property
    def sequence(self):
        return self.get_identified_property(SBOL2.sequence)

    @sequence.setter
    def sequence(self, sequence):
        self.set_identified_property(SBOL2.sequence, sequence)

    