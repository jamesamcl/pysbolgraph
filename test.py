# This Python file uses the following encoding: utf-8

from __future__ import print_function
from __future__ import unicode_literals

from pysbolgraph.SBOL2Graph import SBOL2Graph
from pysbolgraph.terms import Biopax, SBOL2
from glob import glob
import json
import os
from sys import version_info
import requests


def load(f):
    file = open(f, 'r')
    s = file.read()
    file.close()
    return s


def mkdir_p_and_open(filename):
    if version_info > (3, 0):
        os.makedirs(filename.rpartition('/')[0], exist_ok=True)
        return open(filename, "wb+")
    else:
        try:
            os.makedirs(filename.rpartition('/')[0])
            return open(filename, "wb+")
        except OSError as e:
            if e.errno == os.errno.EEXIST:
                return open(filename, "wb+")
            else:
                raise e


files = glob('SBOLTestSuite/SBOL2/*.xml')

for file in files:
    print('🐍🐍🐍 ' + file)
    g = SBOL2Graph()
    g.load(file)

    new_filename = "out/" + file

    f = mkdir_p_and_open(new_filename)
    f.write(g.serialize_xml())
    f.close()

    request = {
        'options': {
            'language': 'SBOL2',
            'test_equality': True,
            'check_uri_compliance': False,
            'check_completeness': False,
            'check_best_practices': False,
            'continue_after_first_error': True,
            'provide_detailed_stack_trace': False,
            'insert_type': False,
            'uri_prefix': 'http://foo/',
            'main_file_name': 'main file',
            'diff_file_name': 'comparison file',
        },
        'return_file': False,
        'main_file': load(file),
        'diff_file': load(new_filename)
    }

    resp = requests.post(
        "http://www.async.ece.utah.edu/validate/", json=request)

    r = resp.json()

    if r['valid']:
        print('✅ Valid')
    else:
        print('❌ NOT valid')

    for e in r['errors']:
        if "Namespace" in e:
            continue
        if len(e.strip()) > 0:
            print('⚠️  ' + e)
