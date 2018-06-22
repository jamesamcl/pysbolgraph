from lxml import etree
from lxml.etree import tostring
from lxml.etree import QName

from rdflib.namespace import RDF
from rdflib import URIRef, Literal

rdfNS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
sbolNS = "http://sbols.org/v2#"

ownership_predicates = {
    sbolNS + 'component',
    sbolNS + 'module',
    sbolNS + 'mapsTo',
    sbolNS + 'mapsTo',
    sbolNS + 'interaction',
    sbolNS + 'participation',
    sbolNS + 'functionalComponent',
    sbolNS + 'sequenceConstraint'
}


def serializeSBOL2(g):
    prefixes = dict()
    prefixes['rdf'] = rdfNS
    prefixes['sbol'] = sbolNS

    subject_to_element = dict()

    owned_elements = set()

    for triple in g.triples((None, RDF.type, None)):
        subject = triple[0].toPython()
        theType = triple[2].toPython()
        subject_to_element[subject] = etree.Element(prefixify(theType, prefixes, True),
                                                    attrib={
                                                        QName(rdfNS, 'about'): subject
                                                    }
                                                    )

    for triple in g.triples((None, None, None)):
        subject = triple[0].toPython()
        predicate = triple[1].toPython()
        obj = triple[2]
        element = subject_to_element[subject]
        if predicate == RDF.type:
            continue
        if predicate in ownership_predicates:
            owned_element = subject_to_element[obj.toPython()]
            ownership_element = etree.SubElement(element, prefixify(predicate, prefixes, True))
            ownership_element.append(owned_element)
            owned_elements.add(obj.toPython())
            continue
        if isinstance(obj, URIRef):
            etree.SubElement(element, prefixify(predicate, prefixes, True), attrib={
                QName(rdfNS, 'resource'): obj.toPython()
            })
        elif isinstance(obj, Literal):
            elem = etree.SubElement(element, prefixify(predicate, prefixes, True))
            elem.text = obj.toPython()
        else:
            raise Exception()

    doc = etree.Element(QName(rdfNS, 'RDF'), nsmap=prefixes)

    for subject in subject_to_element:
        if subject not in owned_elements:
            element = subject_to_element[subject]
            doc.append(element)

    print tostring(doc, pretty_print=True)


def prefixify(iri, prefixes, createNew):
    for prefix in prefixes:
        prefixIRI = prefixes[prefix]
        if iri.startswith(prefixIRI):
            return QName(prefixIRI, iri[len(prefixIRI):])
    if not createNew:
        return iri
    fragmentStart = iri.rfind('#')
    if fragmentStart == -1:
        fragmentStart = iri.rfind('/')
    if fragmentStart == -1:
        return iri
    iriPrefix = iri[:fragmentStart + 1]
    i = 0
    while True:
        prefixName = 'ns' + str(i)
        if prefixName not in prefixes:
            prefixes[prefixName] = iriPrefix
            return QName(iriPrefix, iri[len(iriPrefix):])
        i = i + 1
