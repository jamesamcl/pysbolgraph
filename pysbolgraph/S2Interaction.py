from S2Identified import S2Identified
from S2Participation import S2Participation
from S2IdentifiedFactory import S2IdentifiedFactory

from terms import SBOL2


class S2Interaction(S2Identified):
    def __init__(self, g, uri):
        super(S2Interaction, self).__init__(g, uri)

    @property
    def type(self):
        return self.getUriProperty(SBOL2.type)

    @type.setter
    def type(self, theType):
        self.setUriProperty(SBOL2.type, theType)

    def createParticipation(self, displayId, participant, role):
        identified = S2IdentifiedFactory.createChild(self.g, SBOL2.Participation, self, displayId)
        participation = S2Participation(self.g, identified.uri)
        participation.participant = participant
        participation.addRole(role)
        self.insertUriProperty(SBOL2.participation, participation.uri)
        return participation
