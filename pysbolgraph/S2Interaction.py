from utils.S2Identified import S2Identified
from utils.S2Participation import S2Participation
from utils.S2IdentifiedFactory import S2IdentifiedFactory

from utils.meta.terms import SBOL2


class S2Interaction(S2Identified):
    def __init__(self, g, uri):
        super(S2Interaction, self).__init__(g, uri)

    @property
    def type(self):
        return self.get_uri_property(SBOL2.type)

    @type.setter
    def type(self, the_type):
        self.set_uri_property(SBOL2.type, the_type)

    @property
    def participations(self):
        return [S2Participation(self.g, uri) for uri in self.get_uri_properties(SBOL2.participation)]

    def create_participation(self, display_id, participant, role):
        identified = S2IdentifiedFactory.create_child(self.g, SBOL2.Participation, self, display_id)
        participation = S2Participation(self.g, identified.uri)
        participation.participant = participant
        participation.add_role(role)
        self.insert_uri_property(SBOL2.participation, participation.uri)
        return participation
