
from S2Identified import S2Identified
from S2Component import S2Component
from S2SequenceAnnotation import S2SequenceAnnotation
from S2Sequence import S2Sequence

from terms import SBOL2, Dcterms

from rdflib import URIRef

class S2ComponentDefinition(S2Identified):
    def __init__(self, g, uri):
        super(S2ComponentDefinition, self).__init__(g, uri)

    @property
    def types(self):
        return self.getUriProperties(SBOL2.type)
    def hasType(self, type):
        return self.g.hasMatch(self.uri, SBOL2.type, URIRef(type))
    def addType(self, type):
        self.insertProperties({ SBOL2.type: URIRef(type) })

    @property
    def roles(self):
        return self.getUriProperties(SBOL2.role)
    def hasRole(self, role):
        return self.g.hasMatch(self.uri, SBOL2.role, URIRef(role))
    def addRole(self, role):
        self.insertProperties({ SBOL2.role: URIRef(role) })

    @property
    def components(self):
        return [ S2Component(self.g, uri) for uri in self.getUriProperties(SBOL2.component) ]

    @property
    def sequenceAnnotations(self):
        return [ S2SequenceAnnotation(self.g, uri) for uri in self.getUriProperties(SBOL2.sequenceAnnotation) ]

    @property
    def sequences(self):
        return [ S2Sequence(self.g, uri) for uri in self.getUriProperties(SBOL2.sequence) ]
    


