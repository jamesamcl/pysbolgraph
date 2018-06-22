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


def serialize_sboll2(g):
    prefixes = dict()
    prefixes['rdf'] = rdfNS
    prefixes['sbol'] = sbolNS

    subject_to_element = dict()

    owned_elements = set()

    for triple in g.triples((None, RDF.type, None)):
        subject = triple[0].toPython()
        the_type = triple[2].toPython()
        subject_to_element[subject] = etree.Element(prefixify(the_type, prefixes, True),
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


def prefixify(iri, prefixes, create_new):
    for prefix in prefixes:
        prefix_iri = prefixes[prefix]
        if iri.startswith(prefix_iri):
            return QName(prefix_iri, iri[len(prefix_iri):])
    if not create_new:
        return iri
    fragment_start = iri.rfind('#')
    if fragment_start == -1:
        fragment_start = iri.rfind('/')
    if fragment_start == -1:
        return iri
    iri_prefix = iri[:fragment_start + 1]
    i = 0
    while True:
        prefix_name = 'ns' + str(i)
        if prefix_name not in prefixes:
            prefixes[prefix_name] = iri_prefix
            return QName(iri_prefix, iri[len(iri_prefix):])
        i = i + 1
