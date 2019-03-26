
from .S2Identified import S2Identified

from .terms import Prov
from .terms import SBOL2

from rdflib import URIRef
from rdflib.namespace import RDF

class S2Experiment(S2Identified):
    def __init__(self, g, uri):
        super(S2Experiment, self).__init__(g, uri)

    @property
    def experimental_data(self):
        return [self.g.uri_to_facade(uri) for uri in self.get_uri_properties(SBOL2.experimentalData)]

    def add_experimental_data(self, ed):
        self.insert_identified_property(SBOL2.experimentalData, ed)


