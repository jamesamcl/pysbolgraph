
from rdflib import Literal, URIRef

from terms import SBOL2, Dcterms

class Facade(object):
    def __init__(self, g, uri):
        self.g = g
        self.uri = uri

    def getStringProperty(self, predicate):
        for triple in self.g.triples( (URIRef(self.uri), URIRef(predicate), None) ):
            return triple[2].toPython()
        return None
    def setStringProperty(self, predicate, value):
        self.g.remove( (URIRef(self.uri), URIRef(predicate), None) )
        self.g.add( (URIRef(self.uri), URIRef(predicate), Literal(obj)) )

    def getIntegerProperty(self, predicate):
        for triple in self.g.triples( (URIRef(self.uri), URIRef(predicate), None) ):
            return triple[2].toPython()
        return None
    def setIntegerProperty(self, predicate, value):
        self.g.remove( (URIRef(self.uri), URIRef(predicate), None) )
        self.g.add( (URIRef(self.uri), URIRef(predicate), Literal(obj)) )

    def setUriProperty(self, predicate, value):
        self.g.remove( (URIRef(self.uri), URIRef(predicate), None) )
        self.g.add( (URIRef(self.uri), URIRef(predicate), URIRef(value)) )
    def insertUriProperty(self, predicate, value):
        self.g.add( (URIRef(self.uri), URIRef(predicate), URIRef(value)) )
    def getUriProperty(self, predicate):
        for triple in self.g.triples( (URIRef(self.uri), URIRef(predicate), None) ):
            return triple[2].toPython()
        return None
    def getUriProperties(self, predicate):
        return [ triple[2].toPython() for triple in self.g.triples( (URIRef(self.uri), URIRef(predicate), None) ) ]
    def insertProperties(self, properties):
        for predicate in properties:
            obj = properties[predicate]
            self.g.add( (URIRef(self.uri), URIRef(predicate), obj) )

    def setIdentifiedProperty(self, predicate, value):
        if isinstance(value, S2Identified):
            self.setUriProperty(URIRef(predicate), URIRef(value.uri))
        elif isinstance(value, str):
            self.setUriProperty(URIRef(predicate), URIRef(value))
        else:
            raise Exception()
    def insertIdentifiedProperty(self, predicate, value):
        if isinstance(value, S2Identified):
            self.insertUriProperty(URIRef(predicate), URIRef(value.uri))
        elif isinstance(value, URIRef):
            self.insertUriProperty(URIRef(predicate), value)
        elif isinstance(value, str):
            self.insertUriProperty(URIRef(predicate), URIRef(value))
        else:
            print 'you asked me to insert', value, 'but i do not know how'
            raise Exception()




        




        

class S2Identified(Facade):
    def __init__(self, g, uri):
        super(S2Identified, self).__init__(g, uri)
    @property
    def name(self):
        return self.getStringProperty(Dcterms.title)
    @name.setter
    def name(self, name):
        self.setStringProperty(Dcterms.title, name)
    @property
    def displayId(self):
        return self.getStringProperty(SBOL2.displayId)
    @property
    def persistentIdentity(self):
        return self.getUriProperty(SBOL2.persistentIdentity)
    @property
    def version(self):
        return self.getUriProperty(SBOL2.version)
    @property
    def displayName(self):
        name = self.name
        if name is not None:
            return name
        definitionName = self.definition.name
        if definitionName is not None:
            return definitionName
        return self.displayId
    
