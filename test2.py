
from SBOL2Graph import SBOL2Graph

g = SBOL2Graph()

prefix = 'http://thebear/'

cd = g.createComponentDefinition(prefix, 'http://sometype/DNA', 'foo')

print cd.displayId

for s,p,o in g.g.triples((None, None, None)):
    print s,p,o


