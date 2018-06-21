
import rdflib

from rdflib.namespace import RDF

from terms import SBOL2

from S2Component import S2Component, S2ComponentDefinition

class SBOL2Graph:
    def __init__(self):
        self.g = rdflib.Graph()
    def load(self, url):
        self.g.load(url)
    @property
    def componentDefinitions(self):
        return [ S2ComponentDefinition(self.g, triple[0]) for triple in self.g.triples( (None, RDF.type, SBOL2.ComponentDefinition) ) ]

    def getType(uri):
        triples = self.g.triples(uri, RDF.type, None)
        if len(triples) > 0:
            return triples[0][2].toPython()
        else:
            return None

    def uriToFacade(self, uri):
        type = self.getType(uri)
        if type == None:
            return None
        if type == SBOL2.ComponentDefinition:
            return S2ComponentDefinition(self, uri)
        if type == SBOL2.Component:
            return S2Component(self, uri)
        if type == SBOL2.SequenceAnnotation:
            return S2SequenceAnnotation(self, uri)
        if type == SBOL2.SequenceConstraint:
            return S2SequenceConstraint(self, uri)
        if type == SBOL2.ModuleDefinition:
            return S2ModuleDefinition(self, uri)
        if type == SBOL2.Module:
            return S2Module(self, uri)
        if type == SBOL2.Sequence:
            return S2Sequence(self, uri)
        if type == SBOL2.Model:
            return S2Model(self, uri)
        if type == SBOL2.Range:
            return S2Range(self, uri)
        if type == SBOL2.Cut:
            return S2Cut(self, uri)
        if type == SBOL2.GenericLocation:
            return S2GenericLocation(self, uri)
        return None

