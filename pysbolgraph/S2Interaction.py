from .S2Identified import S2Identified
from .S2Participation import S2Participation
from .S2IdentifiedFactory import S2IdentifiedFactory

from .terms import SBOL2


class S2Interaction(S2Identified):
    def __init__(self, g, uri):
        super(S2Interaction, self).__init__(g, uri)

    @property
    def type(self):
        return self.get_uri_property(SBOL2.type)

    @type.setter
    def type(self, the_type):
        self.set_uri_property(SBOL2.type, the_type)

    def create_participation(self, display_id, participant, role):
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.Participation, self, display_id)
        participation = S2Participation(self.g, identified.uri)
        participation.participant = participant
        participation.add_role(role)
        self.insert_uri_property(SBOL2.participation, participation.uri)
        return participation
