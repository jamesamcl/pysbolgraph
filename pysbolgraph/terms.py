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
        "Model",
        "MapsTo",
        "Sequence",
        "SequenceConstraint",
        "FunctionalComponent",
        "Experiment",
        "ExperimentalData",

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
        "model",
        "framework",
        "source",
        "language",
        "attachment",
        "format",
        "hash",
        "size",
        "built",
        "experimentalData",
        "sourceLocation",

        # terms
        "precedes",
        "local",
        "remote",
        "private",
        "public",
        "none",
        "useLocal",
        "useRemote",
        "merge",
        "verifyIdentical",
        "design",
        "build",
        "test",
        "learn"
    ]
)

Biopax = ClosedNamespace(
    uri=URIRef("http://www.biopax.org/release/biopax-level3.owl#"),
    terms=[
        "DnaRegion",
        "RnaRegion",
        "Protein",
        "Complex",
        "SmallMolecule"
    ]
)

Prov = ClosedNamespace(
    uri=URIRef("http://www.w3.org/ns/prov#"),
    terms=[

        # types
        "Agent",
        "Association",
        "Activity",
        "Usage",
        "Plan",
        "Usage",

        # predicates
        "wasDerivedFrom",
        "wasGeneratedBy",
        "qualifiedAssociation",
        "qualifiedUsage",
        "startedAtTime",
        "endedAtTime",
        "wasInformedBy",
        "agent",
        "entity",
        "hadRole",
        "hadPlan"
    ]
)
