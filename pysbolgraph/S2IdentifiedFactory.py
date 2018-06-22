from rdflib import Literal, URIRef
from rdflib.namespace import RDF
from terms import SBOL2
from S2Identified import S2Identified
from terms import Dcterms

import CompliantURIs


class S2IdentifiedFactory:
    def __init__(self):
        pass

    @staticmethod
    def createTopLevel(graph, theType, uriPrefix, displayId, name=None, version="1"):

        uri = graph.generateURI(uriPrefix + displayId + '$n?$/' + version)

        print 'uri is ' + uri

        graph.insertProperties(uri, {
            RDF.type: URIRef(theType),
            SBOL2.displayId: Literal(CompliantURIs.getDisplayId(uri)),
            SBOL2.persistentIdentity: URIRef(CompliantURIs.getPersistentIdentity(uri)),
            SBOL2.version: Literal(CompliantURIs.getVersion(uri))
        })

        if name:
            graph.insertProperties(uri, {Dcterms.title: Literal(name)})

        return S2Identified(graph, uri)

    @staticmethod
    def createChild(graph, theType, parent, displayId, name=None):

        version = parent.version

        print parent.persistentIdentity, displayId, version

        uri = graph.generateURI(parent.persistentIdentity + '/' + displayId + '$n?$/' + version)

        graph.insertProperties(uri, {
            RDF.type: URIRef(theType),
            SBOL2.displayId: Literal(CompliantURIs.getDisplayId(uri)),
            SBOL2.persistentIdentity: URIRef(CompliantURIs.getPersistentIdentity(uri)),
            SBOL2.version: Literal(CompliantURIs.getVersion(uri))
        })

        if name is not None:
            graph.insertProperties(uri, {Dcterms.title: Literal(name)})

        return S2Identified(graph, uri)
