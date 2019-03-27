from .S2Identified import S2Identified

from .terms import SBOL2

from rdflib import URIRef


class S2Participation(S2Identified):
    def __init__(self, g, uri):
        super(S2Participation, self).__init__(g, uri)

    @property
    def roles(self):
        return self.get_uri_properties(SBOL2.role)

    def has_role(self, role):
        return self.g.hasMatch(self.uri, SBOL2.role, URIRef(role))

    def add_role(self, role):
        self.insert_identified_property(SBOL2.role, URIRef(role))

    @property
    def participant(self):
        return self.get_identified_property(SBOL2.participant)

    @participant.setter
    def participant(self, participant):
        self.set_identified_property(SBOL2.participant, participant)

    @property
    def measure(self):
        return self.get_identified_property(SBOL2.measure)

    @measure.setter
    def measure(self, measure):
        self.set_identified_property(SBOL2.measure, measure)
