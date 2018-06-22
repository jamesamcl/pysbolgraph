from distutils.core import setup

setup(name='pysbolgraph',
      version='0.1',
      description='A simple Python library to read and write SBOL files',

      author='James Alastair McLaughlin',

      author_email='j.a.mclaughlin@ncl.ac.uk',

      url='https://github.com/udp/pysbolgraph',

      packages=['pysbolgraph'],
      
      install_requires=['rdflib', 'lxml']
      )
