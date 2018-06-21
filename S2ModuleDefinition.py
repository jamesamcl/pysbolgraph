
from S2Identified import S2Identified
from S2Module import S2Module

from terms import SBOL2, Dcterms

from rdflib import URIRef

class S2ModuleDefinition(S2Identified):
    def __init__(self, g, uri):
        super(S2ModuleDefinition, self).__init__(g, uri)

    @property
    def roles(self):
        return self.getUriProperties(SBOL2.role)
    def hasRole(self, role):
        return self.g.hasMatch(self.uri, SBOL2.role, URIRef(role))
    def addRole(self, role):
        self.insertProperties({ SBOL2.role: URIRef(role) })

    @property
    def modules(self):
        return [ S2Module(self.g, uri) for uri in self.getUriProperties(SBOL2.module) ]


