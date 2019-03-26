
from .S2Identified import S2Identified

class S2Model(S2Identified):
    def __init__(self, g, uri):
        super(S2Model, self).__init__(g, uri)

    @property
    def framework(self):
        return self.get_uri_property(SBOL2.framework)

    @framework.setter
    def framework(self, framework):
        self.set_uri_property(SBOL2.framework, framework)

    @property
    def language(self):
        return self.get_uri_property(SBOL2.language)

    @language.setter
    def language(self, language):
        self.set_uri_property(SBOL2.language, language)

    @property
    def source(self):
        return self.get_uri_property(SBOL2.source)

    @source.setter
    def source(self, source):
        self.set_uri_property(SBOL2.source, source)
