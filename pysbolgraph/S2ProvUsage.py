
from .S2Identified import S2Identified

from .terms import Prov
from .terms import SBOL2

from rdflib import URIRef
from rdflib.namespace import RDF

class S2ProvUsage(S2Identified):
    def __init__(self, g, uri):
        super(S2ProvUsage, self).__init__(g, uri)

    @property
    def entity(self):
        return self.get_identified_property(Prov.entity)

    @entity.setter
    def entity(self, entity):
        self.set_identified_property(Prov.entity, entity)

    @property
    def role(self):
        return self.get_uri_property(Prov.hadRole)

    @role.setter
    def role(self, role):
        self.set_uri_property(Prov.hadRole, role)


