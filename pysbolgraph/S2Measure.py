
from .S2Identified import S2Identified

from .terms import SBOL2
from .terms import Measure

class S2Measure(S2Identified):
    def __init__(self, g, uri):
        super(S2Measure, self).__init__(g, uri)

    @property
    def value(self):
        return self.get_double_property(Measure.hasNumericalValue)

    @value.setter
    def value(self, value):
        self.set_double_property(Measure.hasNumericalValue, value)

    @property
    def unit(self):
        return self.get_identified_property(Measure.hasUnit)

    @unit.setter
    def unit(self, unit):
        self.set_identified_property(Measure.hasUnit, unit)

