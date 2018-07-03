from .S2Identified import S2Identified
from .S2Component import S2ComponentDefinition

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
