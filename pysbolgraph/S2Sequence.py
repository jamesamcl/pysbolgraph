from S2Identified import S2Identified

from terms import SBOL2


class S2Sequence(S2Identified):
    def __init__(self, g, uri):
        super(S2Sequence, self).__init__(g, uri)

    @property
    def encoding(self):
        return self.getUriProperty(SBOL2.encoding)

    @encoding.setter
    def encoding(self, encoding):
        self.setUriProperty(SBOL2.encoding, encoding)

    @property
    def elements(self):
        return self.getStringProperty(SBOL2.elements)

    @elements.setter
    def elements(self, elements):
        self.setUriProperty(SBOL2.elements, elements)
