from S2Identified import S2Identified

from meta.terms import SBOL2
from rdflib import URIRef


class S2SequenceAnnotation(S2Identified):
    def __init__(self, g, uri):
        super(S2SequenceAnnotation, self).__init__(g, uri)

    @property
    def roles(self):
        return self.get_uri_properties(SBOL2.role)

    def has_role(self, role):
        return self.g.hasMatch(self.uri, SBOL2.role, URIRef(role))

    def add_role(self, role):
        self.insert_identified_property(SBOL2.role, URIRef(role))

    @property
    def locations(self):
        return [self.g.uri_to_facade(uri) for uri in self.get_uri_properties(SBOL2.location)]

    def add_location(self, location):
        self.insert_identified_property(SBOL2.location, location)
