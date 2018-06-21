
from S2Identified import S2Identified
from S2ComponentDefinition import S2ComponentDefinition

from terms import SBOL2, Dcterms

class S2Component(S2Identified):
    def __init__(self, g, uri):
        super(S2Component, self).__init__(g, uri)

    @property
    def definition(self):
        return S2ComponentDefinition(self.g, self.getUriProperty(SBOL2.definition))


