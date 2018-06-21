
from Facade import Facade

from terms import SBOL2, Dcterms

class S2Identified(Facade):
    def __init__(self, g, uri):
        super(S2Identified, self).__init__(g, uri)
    @property
    def name(self):
        return self.getStringProperty(Dcterms.title)
    @name.setter
    def name(self, name):
        self.setStringProperty(Dcterms.title, name)
    @property
    def displayId(self):
        return self.getStringProperty(SBOL2.displayId)
    @property
    def persistentIdentity(self):
        return self.getUriProperty(SBOL2.persistentIdentity)
    @property
    def version(self):
        return self.getUriProperty(SBOL2.version)
    @property
    def displayName(self):
        name = self.name
        if name is not None:
            return name
        definitionName = self.definition.name
        if definitionName is not None:
            return definitionName
        return self.displayId
    