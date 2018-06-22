from rdflib.namespace import ClosedNamespace
from rdflib import URIRef

Dcterms = ClosedNamespace(
    uri=URIRef("http://purl.org/dc/terms/"),
    terms=[
        "title"
    ]
)

SBOL2 = ClosedNamespace(
    uri=URIRef("http://sbols.org/v2#"),
    terms=[
        # types
        "ComponentDefinition",
        "Component",
        "ModuleDefinition",
        "Module",
        "Interaction",
        "Participation",
        "MapsTo",
        "Sequence",
        "SequenceConstraint",
        "FunctionalComponent",

        # predicates
        "component",
        "displayId",
        "type",
        "role",
        "persistentIdentity",
        "version",
        "interaction",
        "participant",
        "mapsTo",
        "sequence",
        "access",
        "definition",
        "direction",
        "refinement",
        "sequenceConstraint",
        "functionalComponent",
        "module",
        "participation",
        "encoding",
        "elements",
        "restriction",

        # terms
        "precedes",
        "local",
        "remote",
        "private",
        "public",
        "directionNone",
        "useLocal",
        "useRemote",
    ]
)

Biopax = ClosedNamespace(
    uri=URIRef("http://www.biopax.org/release/biopax-level3.owl#"),
    terms=[
        "DnaRegion",
        "RnaRegion",
        "Protein",
        "Complex"
    ]
)
