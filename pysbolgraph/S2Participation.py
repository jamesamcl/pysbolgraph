
from S2Identified import S2Identified

from terms import SBOL2

from rdflib import URIRef

class S2Participation(S2Identified):
    def __init__(self, g, uri):
        super(S2Participation, self).__init__(g, uri)
    @property
    def roles(self):
        return self.getUriProperties(SBOL2.role)
    def hasRole(self, role):
        return self.g.hasMatch(self.uri, SBOL2.role, URIRef(role))
    def addRole(self, role):
        self.insertIdentifiedProperty(SBOL2.role, URIRef(role))

    @property
    def participant(self):
        return self.getIdentifiedProperty(SBOL2.participant)
    @participant.setter
    def participant(self, participant):
        self.setIdentifiedProperty(SBOL2.participant, participant)

