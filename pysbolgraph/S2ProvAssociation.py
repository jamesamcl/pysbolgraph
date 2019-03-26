
from .S2Identified import S2Identified

from .terms import Prov
from .terms import SBOL2

from rdflib import URIRef
from rdflib.namespace import RDF

class S2ProvAssociation(S2Identified):
    def __init__(self, g, uri):
        super(S2ProvAssociation, self).__init__(g, uri)

    @property
    def agent(self):
        return self.get_identified_property(Prov.agent)

    @agent.setter
    def agent(self, agent):
        self.set_identified_property(Prov.agent, agent)

    @property
    def plan(self):
        return self.get_identified_property(Prov.hadPlan)

    @plan.setter
    def plan(self, plan):
        self.set_identified_property(Prov.hadPlan, plan)

    @property
    def role(self):
        return self.get_uri_property(Prov.hadRole)

    @role.setter
    def role(self, role):
        self.set_uri_property(Prov.hadRole, role)
