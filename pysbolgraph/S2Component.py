from utils.S2Identified import S2Identified
from utils.S2SequenceAnnotation import S2SequenceAnnotation
from utils.S2Sequence import S2Sequence
from utils.S2SequenceConstraint import S2SequenceConstraint
from utils.S2IdentifiedFactory import S2IdentifiedFactory
from utils.S2MapsTo import S2MapsTo

from utils.meta.terms import SBOL2

from rdflib import URIRef
from rdflib.namespace import RDF


class S2ComponentDefinition(S2Identified):
    def __init__(self, g, uri):
        super(S2ComponentDefinition, self).__init__(g, uri)

    @property
    def types(self):
        return self.get_uri_properties(SBOL2.type)

    def has_type(self, the_type):
        return self.g.hasMatch(self.uri, SBOL2.type, URIRef(the_type))

    def add_type(self, the_type):
        self.insert_properties({SBOL2.type: URIRef(the_type)})

    @property
    def roles(self):
        return self.get_uri_properties(SBOL2.role)

    def has_role(self, role):
        return self.g.hasMatch(self.uri, SBOL2.role, URIRef(role))

    def add_role(self, role):
        self.insert_properties({SBOL2.role: URIRef(role)})

    @property
    def components(self):
        return [S2Component(self.g, uri) for uri in self.get_uri_properties(SBOL2.component)]

    def create_component(self, display_id, definition):
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.Component, self, display_id)
        new_component = S2Component(self.g, identified.uri)
        new_component.definition = definition
        new_component.access = SBOL2.public
        self.insert_uri_property(SBOL2.component, new_component.uri)
        return new_component

    @property
    def sequence_annotations(self):
        return [S2SequenceAnnotation(self.g, uri) for uri in self.get_uri_properties(SBOL2.sequenceAnnotation)]

    @property
    def sequences(self):
        return [S2Sequence(self.g, uri) for uri in self.get_uri_properties(SBOL2.sequence)]

    def add_sequence(self, sequence):
        self.insert_identified_property(SBOL2.sequence, sequence)

    def create_sequence_constraint(self, display_id, restriction, a, b):
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.SequenceConstraint, self, display_id)
        sc = S2SequenceConstraint(self.g, identified.uri)
        sc.subject = a
        sc.object = b
        sc.restriction = restriction
        self.insert_uri_property(SBOL2.sequenceConstraint, sc.uri)
        return sc

    @property
    def instances(self):
        triples = list(self.g.triples((None, SBOL2.definition, URIRef(self.uri))))
        return [S2Component(self.g, triple[0].toPython()) for triple in triples]

class S2Component(S2Identified):
    def __init__(self, g, uri):
        super(S2Component, self).__init__(g, uri)

    @property
    def definition(self):
        return S2ComponentDefinition(self.g, self.get_uri_property(SBOL2.definition))

    @definition.setter
    def definition(self, definition):
        self.set_uri_property(SBOL2.definition, definition.uri)

    def create_maps_to(self, display_id, refinement, local, remote):
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.MapsTo, self, display_id)
        maps_to = S2MapsTo(self.g, identified.uri)
        maps_to.local = local
        maps_to.remote = remote
        maps_to.refinement = refinement
        self.insert_uri_property(SBOL2.mapsTo, maps_to.uri)
        return maps_to

    @property
    def access(self):
        return self.get_uri_property(SBOL2.access)

    @access.setter
    def access(self, access):
        self.set_uri_property(SBOL2.access, access)

    @property
    def containing_component_definition(self):
        triples = list(self.g.triples((None, SBOL2.component, URIRef(self.uri))))
        for triple in triples:
            if (triple[0], RDF.type, SBOL2.ComponentDefinition) in self.g.g:
                return S2ComponentDefinition(self.g, triple[0].toPython())
        raise Exception('component ' + self.uri + ' not contained by a definition?')
        


