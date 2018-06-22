
from S2Identified import S2Identified
from S2SequenceAnnotation import S2SequenceAnnotation
from S2Sequence import S2Sequence
from S2SequenceConstraint import S2SequenceConstraint
from S2IdentifiedFactory import S2IdentifiedFactory

from terms import SBOL2

from rdflib import URIRef

class S2ComponentDefinition(S2Identified):
    def __init__(self, g, uri):
        super(S2ComponentDefinition, self).__init__(g, uri)

    @property
    def types(self):
        return self.getUriProperties(SBOL2.type)
    def hasType(self, theType):
        return self.g.hasMatch(self.uri, SBOL2.type, URIRef(theType))
    def addType(self, theType):
        self.insertProperties({ SBOL2.type: URIRef(theType) })

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

    def addSequence(self, sequence):
        self.insertIdentifiedProperty(SBOL2.sequence, sequence)
    
    def createSequenceConstraint(self, displayId, restriction, a, b):
        identified = S2IdentifiedFactory.createChild(self.g, SBOL2.SequenceConstraint, self, displayId)
        sc = S2SequenceConstraint(self.g, identified.uri)
        sc.subject = a
        sc.object = b
        sc.restriction = restriction
        self.insertUriProperty(SBOL2.sequenceConstraint, sc.uri)
        return sc


class S2Component(S2Identified):
    def __init__(self, g, uri):
        super(S2Component, self).__init__(g, uri)

    @property
    def definition(self):
        return S2ComponentDefinition(self.g, self.getUriProperty(SBOL2.definition))
