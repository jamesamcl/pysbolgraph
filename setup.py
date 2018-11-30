from distutils.core import setup
import setuptools  # noqa

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pysbolgraph',
      version='0.1.0',
      description='A simple Python library to read and write SBOL files',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='James Alastair McLaughlin',
      author_email='james@mclgh.net',
      url='https://github.com/udp/pysbolgraph',
      packages=['pysbolgraph'],
      install_requires=['rdflib', 'lxml', 'requests'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 2",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
      ]
      )
