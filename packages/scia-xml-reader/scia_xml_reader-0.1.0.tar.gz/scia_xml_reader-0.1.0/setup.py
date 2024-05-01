# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scia_xml_reader']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=2.7.1,<3.0.0']

setup_kwargs = {
    'name': 'scia-xml-reader',
    'version': '0.1.0',
    'description': '',
    'long_description': '# SCIA XML reader\nThis python package allows retrieval of SCIA Engineer results from an exported xml. Basic use is done in two steps: Reading the xml and parsing the data. An example is given below.\n\n```\nfrom scia_xml_reader.functions import read_xml\nfrom scia_xml_reader import parser\n\nroot = read_xml(Path("your.xml"))\n\nscia_nodes = parser.parse_nodes(root)\nscia_beams = parser.parse_beams(root)\nscia_loadcases = parser.parse_loadcases(root)\nscia_loadcombinations = parser.parse_loadcombinations(root)\nscia_results_force_1d = parse_results_force_1d(root)\n```\n\n## Objects\nCurrently the `scia_xml_reader` package is able to read the following data from the xml file:\n* Node\n* Beam\n* Loadcase\n* Loadcombination\n* ResultForce1D',
    'author': 'Marijn Drillenburg',
    'author_email': 'm.drillenburg@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
