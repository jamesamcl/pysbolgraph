from .S2Identified import S2Identified
from .S2Component import S2ComponentDefinition
from .S2IdentifiedFactory import S2IdentifiedFactory
from .S2MapsTo import S2MapsTo

from .terms import SBOL2


class S2FunctionalComponent(S2Identified):
    def __init__(self, g, uri):
        super(S2FunctionalComponent, self).__init__(g, uri)

    @property
    def definition(self):
        return S2ComponentDefinition(self.g, self.get_uri_property(SBOL2.definition))

    @definition.setter
    def definition(self, definition):
        self.set_identified_property(SBOL2.definition, definition)

    @property
    def access(self):
        return self.get_uri_property(SBOL2.access)

    @access.setter
    def access(self, access):
        self.set_uri_property(SBOL2.access, access)

    @property
    def direction(self):
        return self.get_uri_property(SBOL2.direction)

    @direction.setter
    def direction(self, direction):
        self.set_uri_property(SBOL2.direction, direction)

    def create_maps_to(self, display_id, refinement, local, remote):
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.MapsTo, self, display_id)
        maps_to = S2MapsTo(self.g, identified.uri)
        maps_to.local = local
        maps_to.remote = remote
        maps_to.refinement = refinement
        self.insert_uri_property(SBOL2.mapsTo, maps_to.uri)
        return maps_to

    @property
    def measure(self):
        return self.get_identified_property(SBOL2.measure)

    @measure.setter
    def measure(self, measure):
        self.set_identified_property(SBOL2.measure, measure)

    