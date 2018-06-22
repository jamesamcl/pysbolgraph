
from S2Identified import S2Identified

from terms import SBOL2, Dcterms

class S2Model(S2Identified):
    def __init__(self, g, uri):
        super(S2Model, self).__init__(g, uri)

