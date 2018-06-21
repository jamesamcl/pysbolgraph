
from S2Identified import S2Identified

from terms import SBOL2, Dcterms

class S2MapsTo(S2Identified):
    def __init__(self, g, uri):
        super(S2MapsTo, self).__init__(g, uri)
    @property
    def local(self):
        return self.g.uriToFacade(self.getUriProperty(SBOL2.local))
    @local.setter
    def local(self, local):
        self.setIdentifiedProperty(SBOL2.local, local)
    @property
    def remote(self):
        return self.g.uriToFacade(self.getUriProperty(SBOL2.remote))
    @remote.setter
    def remote(self, remote):
        self.setIdentifiedProperty(SBOL2.remote, remote)



