
from .S2Identified import S2Identified

from .terms import Prov
from .terms import SBOL2

from rdflib import URIRef
from rdflib.namespace import RDF

class S2ExperimentalData(S2Identified):
    def __init__(self, g, uri):
        super(S2ExperimentalData, self).__init__(g, uri)
