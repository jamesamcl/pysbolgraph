from lxml import etree
from lxml.etree import tostring
from lxml.etree import QName

from rdflib.namespace import RDF
from rdflib import URIRef, Literal

rdfNS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
sbolNS = "http://sbols.org/v2#"

def is_ownership_relation(g, triple):
    subject = triple[0].toPython()
    predicate = triple[1].toPython()
    obj = triple[2]

    ownership_predicates = {
        sbolNS + 'module',
        sbolNS + 'mapsTo',
        sbolNS + 'interaction',
        sbolNS + 'participation',
        sbolNS + 'functionalComponent',
        sbolNS + 'sequenceConstraint',
        sbolNS + 'location',
        sbolNS + 'sequenceAnnotation'
    }

    if predicate in ownership_predicates:
        return True
    
    # SBOL2 reuses the "component" predicate as both an ownership predicate (in
    # the case of ComponentDefinition) and a referencing one (in the case of
    # SequenceAnnotation).
    #
    if predicate == sbolNS + 'component':
        if (triple[0], RDF.type, URIRef(sbolNS + 'SequenceAnnotation')) in g.g:
            return False
        else:
            return True

    return False

def serialize_sboll2(g):
    prefixes = dict()
    prefixes['rdf'] = rdfNS
    prefixes['sbol'] = sbolNS

    subject_to_element = dict()

    owned_elements = set()

    for triple in g.triples((None, RDF.type, None)):
        subject = triple[0].toPython()
        the_type = triple[2].toPython()
        if subject in subject_to_element:
            etree.SubElement(subject_to_element[subject], prefixify(RDF.type, prefixes, True), attrib={
                QName(rdfNS, 'resource'): the_type
            })
        else:
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
        if predicate == RDF.type.toPython():
            continue
        if is_ownership_relation(g, triple):
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
            elem.text = obj
        else:
            raise Exception()

    doc = etree.Element(QName(rdfNS, 'RDF'), nsmap=prefixes)

    for subject in subject_to_element:
        if subject not in owned_elements:
            element = subject_to_element[subject]
            doc.append(element)

    return tostring(doc, pretty_print=True)


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
