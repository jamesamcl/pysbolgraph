
from S2Identified import S2Identified
from S2IdentifiedFactory import S2IdentifiedFactory
from S2Interaction import S2Interaction
from S2FunctionalComponent import S2FunctionalComponent
from S2MapsTo import S2MapsTo

from terms import SBOL2, Dcterms

from rdflib import URIRef

class S2ModuleDefinition(S2Identified):
    def __init__(self, g, uri):
        super(S2ModuleDefinition, self).__init__(g, uri)

    @property
    def roles(self):
        return self.getUriProperties(SBOL2.role)
    def hasRole(self, role):
        return self.g.hasMatch(self.uri, SBOL2.role, URIRef(role))
    def addRole(self, role):
        self.insertProperties({ SBOL2.role: URIRef(role) })

    @property
    def modules(self):
        return [ S2Module(self.g, uri) for uri in self.getUriProperties(SBOL2.module) ]

    def createInteraction(self, displayId, type):
        print 'ci params are', self, displayId, type
        print 'self pi and version are', self.persistentIdentity, self.version
        identified = S2IdentifiedFactory.createChild(self.g, SBOL2.Interaction, self, displayId)
        interaction = S2Interaction(self.g, identified.uri)
        interaction.type = type
        return interaction

    def createFunctionalComponent(self, displayId, access, definition, direction):
        identified = S2IdentifiedFactory.createChild(self.g, SBOL2.FunctionalComponent, self, displayId)
        fc = S2FunctionalComponent(self.g, identified.uri)
        fc.access = access
        fc.definition = definition
        fc.direction = direction
        return fc

    def createModule(self, displayId, definition):
        identified = S2IdentifiedFactory.createChild(self.g, SBOL2.Module, self, displayId)
        module = S2Module(self.g, identified.uri)
        module.definition = definition
        return module


class S2Module(S2Identified):
    def __init__(self, g, uri):
        super(S2Module, self).__init__(g, uri)

    @property
    def definition(self):
        return S2ComponentDefinition(self.g, self.getUriProperty(SBOL2.definition))

    @definition.setter
    def definition(self, definition):
        self.setIdentifiedProperty(SBOL2.definition, definition)
    
    def createMapsTo(self, displayId, refinement, local, remote):
        identified = S2IdentifiedFactory.createChild(self.g, SBOL2.MapsTo, self, displayId)
        fc = S2MapsTo(self.g, identified.uri)
        fc.local = local
        fc.remote = remote
        fc.refinement = refinement
        return fc
    


