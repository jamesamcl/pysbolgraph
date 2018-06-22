
from rdflib import Literal, URIRef

class Facade(object):
    def __init__(self, g, uri):
        self.g = g
        self.uri = uri

    def getStringProperty(self, predicate):
        for triple in self.g.triples( (self.uri, predicate, None) ):
            return triple[2].toPython()
        return None
    def setStringProperty(self, predicate, value):
        self.g.remove( (self.uri, predicate, None) )
        self.g.add( (self.uri, predicate, Literal(obj)) )

    def getIntegerProperty(self, predicate):
        for triple in self.g.triples( (self.uri, predicate, None) ):
            return triple[2].toPython()
        return None
    def setIntegerProperty(self, predicate, value):
        self.g.remove( (self.uri, predicate, None) )
        self.g.add( (self.uri, predicate, Literal(obj)) )

    def setUriProperty(self, predicate, value):
        self.g.remove( (self.uri, predicate, None) )
        self.g.add( (self.uri, predicate, URIRef(obj)) )
    def insertUriProperty(self, predicate, value):
        self.g.add( (self.uri, predicate, URIRef(obj)) )
    def getUriProperty(self, predicate):
        for triple in self.g.triples( (self.uri, predicate, None) ):
            return triple[2].toPython()
        return None
    def getUriProperties(self, predicate):
        return [ triple[2].toPython() for triple in self.g.triples( (self.uri, predicate, None) ) ]
    def insertProperties(self, properties):
        for predicate in properties:
            obj = properties[predicate]
            self.g.add( (self.uri, predicate, obj) )

    def setIdentifiedProperty(self, predicate, value):
        if isinstance(value, S2Identified):
            self.setUriProperty(predicate, value.uri)
        elif isinstance(value, str):
            self.setUriProperty(predicate, value)
        else:
            raise Exception()
    def insertIdentifiedProperty(self, predicate, value):
        if isinstance(value, S2Identified):
            self.insertUriProperty(predicate, value.uri)
        elif isinstance(value, str):
            self.insertUriProperty(predicate, value)
        else:
            raise Exception()




        




        

