
from S2Identified import S2Identified

from terms import SBOL2, Dcterms

class S2Module(S2Identified):
    def __init__(self, g, uri):
        super(S2Module, self).__init__(g, uri)

    @property
    def definition(self):
        return S2ComponentDefinition(self.g, self.getUriProperty(SBOL2.definition))
