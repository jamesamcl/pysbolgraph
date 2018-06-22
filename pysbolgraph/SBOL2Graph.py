
import rdflib

from rdflib import URIRef

from rdflib.namespace import RDF

from terms import SBOL2

from S2Component import S2Component, S2ComponentDefinition
from S2Module import S2Module, S2ModuleDefinition
from S2Sequence import S2Sequence

from S2IdentifiedFactory import S2IdentifiedFactory
import S2SequenceAnnotation, S2SequenceConstraint, S2Model, S2Range, S2Cut, S2GenericLocation

class SBOL2Graph:
    def __init__(self):
        self.g = rdflib.Graph()
    def load(self, url):
        self.g.load(url)
    @property
    def componentDefinitions(self):
        return [ S2ComponentDefinition(self.g, triple[0]) for triple in self.g.triples( (None, RDF.type, SBOL2.ComponentDefinition) ) ]

    def getType(self, uri):
        triples = self.g.triples(uri, RDF.type, None)
        if len(triples) > 0:
            return triples[0][2].toPython()
        else:
            return None

    def createComponentDefinition(self, uriPrefix, theType, displayId, version="1"):
        identified = S2IdentifiedFactory.createTopLevel(self, SBOL2.ComponentDefinition, uriPrefix, displayId, None, version)
        cd = S2ComponentDefinition(self, identified.uri)
        cd.type = theType
        return cd

    def createModuleDefinition(self, uriPrefix, displayId, version="1"):
        identified = S2IdentifiedFactory.createTopLevel(self, SBOL2.ModuleDefinition, uriPrefix, displayId, None, version)
        md = S2ModuleDefinition(self, identified.uri)
        return md

    def createSequence(self, uriPrefix, displayId, version="1"):
        identified = S2IdentifiedFactory.createTopLevel(self, SBOL2.Sequence, uriPrefix, displayId, None, version)
        md = S2Sequence(self, identified.uri)
        return md


    def generateURI(self, template):
        
        n = 1

        while True:

            if n > 1:
                foobar = '_' + str(n)
            else:
                foobar = ''

            # uri = template.replace('$rand$', shortid.generate()).replace('$^n$', '' + n).replace('$n$', '_' + n).replace('$n?$', foobar)
            uri = template.replace('$^n$', str(n)).replace('$n$', '_' + str(n)).replace('$n?$', foobar)

            n = n + 1

            # TODO!!!!
            if len(list(self.g.triples( (uri, None, None ) ))) > 0:
                continue

            return uri

    def triples(self, pattern):
        return self.g.triples(pattern)

    def remove(self, pattern):
        self.g.remove(pattern)

    def add(self, triple):
        self.g.add(triple)

    def insertProperties(self, uri, properties):
        for predicate in properties:
            obj = properties[predicate]
            self.g.add( (URIRef(uri), URIRef(predicate), obj) )

    def uriToFacade(self, uri):
        theType = self.getType(uri)
        if theType is None:
            return None
        if theType == SBOL2.ComponentDefinition:
            return S2ComponentDefinition(self, uri)
        if theType == SBOL2.Component:
            return S2Component(self, uri)
        if theType == SBOL2.SequenceAnnotation:
            return S2SequenceAnnotation(self, uri)
        if theType == SBOL2.SequenceConstraint:
            return S2SequenceConstraint(self, uri)
        if theType == SBOL2.ModuleDefinition:
            return S2ModuleDefinition(self, uri)
        if theType == SBOL2.Module:
            return S2Module(self, uri)
        if theType == SBOL2.Sequence:
            return S2Sequence(self, uri)
        if theType == SBOL2.Model:
            return S2Model(self, uri)
        if theType == SBOL2.Range:
            return S2Range(self, uri)
        if theType == SBOL2.Cut:
            return S2Cut(self, uri)
        if theType == SBOL2.GenericLocation:
            return S2GenericLocation(self, uri)
        return None


    

