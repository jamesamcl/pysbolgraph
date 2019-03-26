
from .S2Identified import S2Identified

from .terms import Prov
from .terms import SBOL2

from rdflib import URIRef
from rdflib.namespace import RDF

class S2ProvActivity(S2Identified):
    def __init__(self, g, uri):
        super(S2ProvActivity, self).__init__(g, uri)

    @property
    def types(self):
        return self.get_uri_properties(SBOL2.type)

    def has_type(self, the_type):
        return self.g.hasMatch(self.uri, SBOL2.type, URIRef(the_type))

    def add_type(self, the_type):
        self.insert_properties({SBOL2.type: URIRef(the_type)})

    @property
    def plan(self):
        return self.get_identified_property(Prov.hadPlan)

    @plan.setter
    def plan(self, plan):
        self.set_identified_property(Prov.hadPlan, plan)

    @property
    def usages(self):
        return [self.g.uri_to_facade(uri) for uri in self.get_uri_properties(Prov.qualifiedUsage)]

    def add_usage(self, usage):
        self.insert_identified_property(Prov.qualifiedUsage, usage)

    @property
    def associations(self):
        return [self.g.uri_to_facade(uri) for uri in self.get_uri_properties(Prov.qualifiedAssociation)]

    def add_association(self, association):
        self.insert_identified_property(Prov.qualifiedAssociation, association)


