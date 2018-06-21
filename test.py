
from SBOL2Graph import SBOL2Graph

g = SBOL2Graph()
g.load('file:///Users/james/pysbolgraph/toggleswitch.xml')


"""
for componentDefinition in g.componentDefinitions:
    print componentDefinition.displayName
    for component in componentDefinition.components:
        print "    " + component.displayName
"""


cd = g.componentDefinitions[0]

print cd.types

cd.addType('http://foo/sometype')

print cd.types


