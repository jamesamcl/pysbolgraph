from rdflib import Literal, URIRef

from terms import SBOL2, Dcterms


class Facade(object):
    def __init__(self, g, uri):
        self.g = g
        self.uri = uri

    def get_string_property(self, predicate):
        for triple in self.g.triples((URIRef(self.uri), URIRef(predicate), None)):
            return triple[2].toPython()
        return None

    def set_string_property(self, predicate, value):
        self.g.remove((URIRef(self.uri), URIRef(predicate), None))
        self.g.add((URIRef(self.uri), URIRef(predicate), Literal(value)))

    def get_integer_property(self, predicate):
        for triple in self.g.triples((URIRef(self.uri), URIRef(predicate), None)):
            return triple[2].toPython()
        return None

    def set_integer_property(self, predicate, value):
        self.g.remove((URIRef(self.uri), URIRef(predicate), None))
        self.g.add((URIRef(self.uri), URIRef(predicate), Literal(value)))

    def set_uri_property(self, predicate, value):
        self.g.remove((URIRef(self.uri), URIRef(predicate), None))
        self.g.add((URIRef(self.uri), URIRef(predicate), URIRef(value)))

    def insert_uri_property(self, predicate, value):
        self.g.add((URIRef(self.uri), URIRef(predicate), URIRef(value)))

    def get_uri_property(self, predicate):
        for triple in self.g.triples((URIRef(self.uri), URIRef(predicate), None)):
            return triple[2].toPython()
        return None

    def get_uri_properties(self, predicate):
        return [triple[2].toPython() for triple in self.g.triples((URIRef(self.uri), URIRef(predicate), None))]

    def insert_properties(self, properties):
        for predicate in properties:
            obj = properties[predicate]
            self.g.add((URIRef(self.uri), URIRef(predicate), obj))

    def set_identified_property(self, predicate, value):
        if isinstance(value, S2Identified):
            self.set_uri_property(URIRef(predicate), URIRef(value.uri))
        elif isinstance(value, str):
            self.set_uri_property(URIRef(predicate), URIRef(value))
        else:
            raise Exception()

    def get_identified_property(self, predicate):
        return self.g.uri_to_facade(self.get_uri_property(predicate))

    def insert_identified_property(self, predicate, value):
        if isinstance(value, S2Identified):
            self.insert_uri_property(URIRef(predicate), URIRef(value.uri))
        elif isinstance(value, URIRef):
            self.insert_uri_property(URIRef(predicate), value)
        elif isinstance(value, str):
            self.insert_uri_property(URIRef(predicate), URIRef(value))
        else:
            print 'you asked me to insert', value, 'but i do not know how'
            raise Exception()


class S2Identified(Facade):
    def __init__(self, g, uri):
        super(S2Identified, self).__init__(g, uri)

    @property
    def name(self):
        return self.get_string_property(Dcterms.title)

    @name.setter
    def name(self, name):
        self.set_string_property(Dcterms.title, name)

    @property
    def display_id(self):
        return self.get_string_property(SBOL2.displayId)

    @property
    def persistent_identity(self):
        return self.get_uri_property(SBOL2.persistentIdentity)

    @property
    def version(self):
        return self.get_uri_property(SBOL2.version)

    @property
    def display_name(self):
        name = self.name
        if name is not None:
            return name
        return self.display_id
