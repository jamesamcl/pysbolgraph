from .S2Identified import S2Identified

from .terms import SBOL2


class S2MapsTo(S2Identified):
    def __init__(self, g, uri):
        super(S2MapsTo, self).__init__(g, uri)

    @property
    def local(self):
        return self.g.uri_to_facade(self.get_uri_property(SBOL2.local))

    @local.setter
    def local(self, local):
        self.set_identified_property(SBOL2.local, local)

    @property
    def remote(self):
        return self.g.uri_to_facade(self.get_uri_property(SBOL2.remote))

    @remote.setter
    def remote(self, remote):
        self.set_identified_property(SBOL2.remote, remote)

    @property
    def refinement(self):
        return self.get_uri_property(SBOL2.refinement)

    @refinement.setter
    def refinement(self, refinement):
        self.set_uri_property(SBOL2.refinement, refinement)
