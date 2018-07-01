import rdflib
import requests
import json

from rdflib import URIRef

from rdflib.namespace import RDF

from .terms import SBOL2

from .S2Component import S2Component, S2ComponentDefinition
from .S2Module import S2Module, S2ModuleDefinition
from .S2Sequence import S2Sequence

from .S2IdentifiedFactory import S2IdentifiedFactory
from .S2SequenceAnnotation import S2SequenceAnnotation
from .S2SequenceConstraint import S2SequenceConstraint
from .S2Model import S2Model
from .S2Range import S2Range
from .S2Cut import S2Cut
from .S2GenericLocation import S2GenericLocation

from .SBOL2Serialize import serialize_sboll2


class SBOL2Graph:
    def __init__(self):
        self.g = rdflib.Graph()

    def load(self, url):
        self.g.load(url)

    @property
    def component_definitions(self):
        return [S2ComponentDefinition(self.g, triple[0]) for triple in
                self.g.triples((None, RDF.type, SBOL2.ComponentDefinition))]

    @property
    def module_definitions(self):
        return [S2ModuleDefinition(self.g, triple[0]) for triple in
                self.g.triples((None, RDF.type, SBOL2.ModuleDefinition))]


    @property
    def sequences(self):
        return [S2Sequence(self.g, triple[0]) for triple in
                self.g.triples((None, RDF.type, SBOL2.Sequence))]

    def get_type(self, uri):
        triples = self.g.triples(uri, RDF.type, None)
        if len(triples) > 0:
            return triples[0][2].toPython()
        else:
            return None

    def create_component_definition(self, uri_prefix, display_id, the_type, version="1"):
        identified = S2IdentifiedFactory.create_top_level(self, SBOL2.ComponentDefinition, uri_prefix, display_id, None,
                                                          version)
        cd = S2ComponentDefinition(self, identified.uri)
        cd.type = the_type
        return cd

    def create_module_definition(self, uri_prefix, display_id, version="1"):
        identified = S2IdentifiedFactory.create_top_level(self, SBOL2.ModuleDefinition, uri_prefix, display_id, None,
                                                          version)
        md = S2ModuleDefinition(self, identified.uri)
        return md

    def create_sequence(self, uri_prefix, display_id, elements, encoding, version="1"):
        identified = S2IdentifiedFactory.create_top_level(self, SBOL2.Sequence, uri_prefix, display_id, None, version)
        seq = S2Sequence(self, identified.uri)
        seq.encoding = encoding
        seq.elements = elements
        return seq

    def generate_uri(self, template):

        n = 1

        while True:

            if n > 1:
                foobar = '_' + str(n)
            else:
                foobar = ''

            # uri = template.replace('$rand$', shortid.generate()).replace('$^n$', '' + n).replace('$n$', '_' + n).replace('$n?$', foobar)
            uri = template.replace('$^n$', str(n)).replace('$n$', '_' + str(n)).replace('$n?$', foobar)

            n = n + 1

            # TODO!!!!
            if len(list(self.g.triples((uri, None, None)))) > 0:
                continue

            return uri

    def triples(self, pattern):
        return self.g.triples(pattern)

    def remove(self, pattern):
        self.g.remove(pattern)

    def add(self, triple):
        self.g.add(triple)

    def insert_properties(self, uri, properties):
        for predicate in properties:
            obj = properties[predicate]
            self.g.add((URIRef(uri), URIRef(predicate), obj))

    def uri_to_facade(self, uri):
        the_type = self.get_type(uri)
        if the_type is None:
            return None
        if the_type == SBOL2.ComponentDefinition:
            return S2ComponentDefinition(self, uri)
        if the_type == SBOL2.Component:
            return S2Component(self, uri)
        if the_type == SBOL2.SequenceAnnotation:
            return S2SequenceAnnotation(self, uri)
        if the_type == SBOL2.SequenceConstraint:
            return S2SequenceConstraint(self, uri)
        if the_type == SBOL2.ModuleDefinition:
            return S2ModuleDefinition(self, uri)
        if the_type == SBOL2.Module:
            return S2Module(self, uri)
        if the_type == SBOL2.Sequence:
            return S2Sequence(self, uri)
        if the_type == SBOL2.Model:
            return S2Model(self, uri)
        if the_type == SBOL2.Range:
            return S2Range(self, uri)
        if the_type == SBOL2.Cut:
            return S2Cut(self, uri)
        if the_type == SBOL2.GenericLocation:
            return S2GenericLocation(self, uri)
        return None

    def serialize_xml(self):
        return serialize_sboll2(self)

    @staticmethod
    def validate_xml(xml, check_uri_compliance=False, check_completeness=False, check_best_practices=False,
                     provide_detailed_stack_trace=False):

        # See API docs at http://synbiodex.github.io/SBOL-Validator/#introduction
        request = {'options': {'language': 'SBOL2',
                               'test_equality': False,
                               'check_uri_compliance': check_uri_compliance,
                               'check_completeness': check_completeness,
                               'check_best_practices': check_best_practices,
                               'fail_on_first_error': False,
                               'provide_detailed_stack_trace': provide_detailed_stack_trace,
                               'subset_uri': '',
                               'uri_prefix': '',
                               'version': '',
                               'insert_type': False,
                               'main_file_name': 'main file',
                               'diff_file_name': 'comparison file',
                               },
                   'return_file': True,
                   'main_file': xml
                   }

        resp = requests.post("http://www.async.ece.utah.edu/validate/", json=request)
        return json.dumps(resp.json())
