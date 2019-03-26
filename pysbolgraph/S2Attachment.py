
from .S2Identified import S2Identified

from .terms import SBOL2

from rdflib import URIRef
from rdflib.namespace import RDF

class S2Attachment(S2Identified):
    def __init__(self, g, uri):
        super(S2Attachment, self).__init__(g, uri)

    @property
    def source(self):
        return self.get_uri_property(SBOL2.source)

    @source.setter
    def source(self, source):
        self.set_uri_property(SBOL2.source, source)

    @property
    def format(self):
        return self.get_uri_property(SBOL2.format)

    @format.setter
    def format(self, format):
        self.set_uri_property(SBOL2.format, format)

    @property
    def size(self):
        return self.get_integer_property(SBOL2.size)

    @size.setter
    def size(self, size):
        self.set_integer_property(SBOL2.size, size)

    @property
    def hash(self):
        return self.get_string_property(SBOL2.hash)

    @hash.setter
    def hash(self, hash):
        self.set_string_property(SBOL2.hash, hash)
