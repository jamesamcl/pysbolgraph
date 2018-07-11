from .S2Identified import S2Identified
from .S2IdentifiedFactory import S2IdentifiedFactory
from .S2Interaction import S2Interaction
from .S2FunctionalComponent import S2FunctionalComponent
from .S2MapsTo import S2MapsTo
from .S2Component import S2ComponentDefinition

from .terms import SBOL2

from rdflib import URIRef


class S2ModuleDefinition(S2Identified):
    def __init__(self, g, uri):
        super(S2ModuleDefinition, self).__init__(g, uri)

    @property
    def roles(self):
        return self.get_uri_properties(SBOL2.role)

    def has_role(self, role):
        return self.g.hasMatch(self.uri, SBOL2.role, URIRef(role))

    def add_role(self, role):
        self.insert_properties({SBOL2.role: URIRef(role)})

    @property
    def functional_components(self):
        return [S2FunctionalComponent(self.g, uri) for uri in self.get_uri_properties(SBOL2.functionalComponent)]

    @property
    def interactions(self):
        return [S2Interaction(self.g, uri) for uri in self.get_uri_properties(SBOL2.interaction)]

    @property
    def modules(self):
        return [S2Module(self.g, uri) for uri in self.get_uri_properties(SBOL2.module)]

    def create_interaction(self, display_id, the_type):
        print('ci params are: %s, %s, %s' %(self, display_id, the_type))
        print('self pi and version are %s, %s' % (self.persistent_identity, self.version))
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.Interaction, self, display_id)
        interaction = S2Interaction(self.g, identified.uri)
        interaction.type = the_type
        self.insert_uri_property(SBOL2.interaction, interaction.uri)
        return interaction

    def create_functional_component(self, display_id, access, definition, direction):
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.FunctionalComponent, self, display_id)
        fc = S2FunctionalComponent(self.g, identified.uri)
        fc.access = access
        fc.definition = definition
        fc.direction = direction
        self.insert_uri_property(SBOL2.functionalComponent, fc.uri)
        return fc

    def create_module(self, display_id, definition):
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.Module, self, display_id)
        new_module = S2Module(self.g, identified.uri)
        new_module.definition = definition
        self.insert_uri_property(SBOL2.module, new_module.uri)
        return new_module


class S2Module(S2Identified):
    def __init__(self, g, uri):
        super(S2Module, self).__init__(g, uri)

    @property
    def definition(self):
        return S2ComponentDefinition(self.g, self.get_uri_property(SBOL2.definition))

    @definition.setter
    def definition(self, definition):
        self.set_identified_property(SBOL2.definition, definition)

    def create_maps_to(self, display_id, refinement, local, remote):
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.MapsTo, self, display_id)
        maps_to = S2MapsTo(self.g, identified.uri)
        maps_to.local = local
        maps_to.remote = remote
        maps_to.refinement = refinement
        self.insert_uri_property(SBOL2.mapsTo, maps_to.uri)
        return maps_to
