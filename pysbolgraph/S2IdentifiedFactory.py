from rdflib import Literal, URIRef
from rdflib.namespace import RDF
from .terms import SBOL2
from .S2Identified import S2Identified
from .terms import Dcterms

from . import CompliantURIs


class S2IdentifiedFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_top_level(graph, the_type, uri_prefix, display_id, name=None, version="1"):

        uri = graph.generate_uri(uri_prefix + display_id + '$n?$/' + version)

        graph.insert_properties(uri, {
            RDF.type: URIRef(the_type),
            SBOL2.displayId: Literal(CompliantURIs.get_display_id(uri)),
            SBOL2.persistentIdentity: URIRef(CompliantURIs.get_persistent_identity(uri)),
            SBOL2.version: Literal(CompliantURIs.get_version(uri))
        })

        if name:
            graph.insert_properties(uri, {Dcterms.title: Literal(name)})

        return S2Identified(graph, uri)

    @staticmethod
    def create_child(graph, the_type, parent, display_id, name=None):

        version = parent.version

        print("%s %s %s" % (parent.persistent_identity, display_id, version))

        uri = graph.generate_uri(parent.persistent_identity + '/' + display_id + '$n?$/' + version)

        graph.insert_properties(uri, {
            RDF.type: URIRef(the_type),
            SBOL2.displayId: Literal(CompliantURIs.get_display_id(uri)),
            SBOL2.persistentIdentity: URIRef(CompliantURIs.get_persistent_identity(uri)),
            SBOL2.version: Literal(CompliantURIs.get_version(uri))
        })

        if name is not None:
            graph.insert_properties(uri, {Dcterms.title: Literal(name)})

        return S2Identified(graph, uri)
