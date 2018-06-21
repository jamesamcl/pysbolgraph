
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

        # predicates
        "component",
        "displayId",
        "type",
        "role"
        ]
)     


